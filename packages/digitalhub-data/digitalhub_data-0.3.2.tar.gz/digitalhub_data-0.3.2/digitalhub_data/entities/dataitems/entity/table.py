from __future__ import annotations

import shutil
import typing
from pathlib import Path

from digitalhub_core.stores.builder import get_default_store, get_store
from digitalhub_core.utils.exceptions import EntityError
from digitalhub_data.entities.dataitems.entity._base import Dataitem

if typing.TYPE_CHECKING:
    import pandas as pd


class DataitemTable(Dataitem):

    """
    Table dataitem.
    """

    def as_df(self, file_format: str | None = None, **kwargs) -> pd.DataFrame:
        """
        Read dataitem as a pandas DataFrame. If the dataitem is not local, it will be downloaded
        to a temporary folder and deleted after the method is executed. If no file_format is passed,
        the function will try to infer it from the dataitem.spec.path attribute.
        The path of the dataitem is specified in the spec attribute, and must be a store aware path.
        If the dataitem is stored on s3 bucket, the path must be s3://<bucket>/<path_to_dataitem>.
        If the dataitem is stored on database (Postgres is the only one supported), the path must
        be sql://postgres/<database>/<schema>/<table/view>.

        Parameters
        ----------
        file_format : str
            Format of the file. (Supported csv and parquet).
        **kwargs
            Keyword arguments.

        Returns
        -------
        pd.DataFrame
            Pandas DataFrame.
        """
        if self.spec.path is None:
            raise EntityError("Path is not specified.")

        store = get_store(self.spec.path)
        tmp_path = False

        # Download dataitem if not local
        if not self._check_local(self.spec.path):
            path = store.download(self.spec.path)
            tmp_path = True
        else:
            path = self.spec.path

        # Check file format and get dataitem as DataFrame
        extension = self._get_extension(self.spec.path, file_format)
        df = store.read_df(path, extension, **kwargs)

        # Delete tmp folder
        if tmp_path:
            pth = Path(path)
            if pth.is_file():
                pth = pth.parent
            shutil.rmtree(pth)

        return df

    def write_df(self, target_path: str | None = None, df: pd.DataFrame | None = None, **kwargs) -> str:
        """
        Write pandas DataFrame as parquet.
        If no target_path is passed, the dataitem will be written into the default store.
        If no DataFrame is passed, the dataitem will be written into the target_path.

        Parameters
        ----------
        target_path : str
            Path to write the dataframe to
        df : pd.DataFrame
            DataFrame to write.
        **kwargs
            Keyword arguments.

        Returns
        -------
        str
            Path to the written dataframe.
        """
        if target_path is None:
            target_path = f"{self.project}/dataitems/{self.kind}/{self.name}.parquet"
            store = get_default_store()
        else:
            store = get_store(target_path)
        if df is None:
            df = self.as_df()
        return store.write_df(df, target_path, **kwargs)
