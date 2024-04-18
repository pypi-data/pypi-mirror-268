from __future__ import annotations
import datetime
import pandas as pd
import os
import abc

from vdf_io.util import extract_data_hash
from vdf_io.constants import ID_COLUMN


class ExportVDB(abc.ABC):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "DB_NAME_SLUG"):
            raise TypeError(
                f"Class {cls.__name__} lacks required class variable 'DB_NAME_SLUG'"
            )

    def __init__(self, args):
        self.file_structure = []
        self.file_ctr = 1
        self.hash_value = extract_data_hash(args)
        self.args = args
        self.args["hash_value"] = self.hash_value
        self.args["exported_count"] = 0
        self.timestamp_in_format = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.vdf_directory = f"vdf_{self.timestamp_in_format}_{self.hash_value}"
        os.makedirs(self.vdf_directory, exist_ok=True)

    @abc.abstractmethod
    def get_data(self) -> ExportVDB:
        """
        Get data from vector database
        """
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def make_parser(cls, subparsers):
        raise NotImplementedError()

    @classmethod
    @abc.abstractmethod
    def export_vdb(cls, args):
        raise NotImplementedError()

    def save_vectors_to_parquet(self, vectors, metadata, vectors_directory):
        vectors_df = pd.DataFrame(list(vectors.items()), columns=[ID_COLUMN, "vector"])

        if metadata:
            metadata_list = [{**{ID_COLUMN: k}, **v} for k, v in metadata.items()]
            metadata_df = pd.DataFrame.from_records(metadata_list)

            # Check for duplicate column names and rename as necessary
            common_columns = set(vectors_df.columns) & set(metadata_df.columns) - {
                ID_COLUMN
            }
            metadata_df.rename(
                columns={col: f"metadata_{col}" for col in common_columns}, inplace=True
            )

            df = vectors_df.merge(metadata_df, on=ID_COLUMN, how="left")
        else:
            df = vectors_df

        parquet_file = os.path.join(vectors_directory, f"{self.file_ctr}.parquet")
        df.to_parquet(parquet_file)
        self.file_structure.append(parquet_file)
        self.file_ctr += 1

        vectors = {}
        metadata = {}
        return len(df)
