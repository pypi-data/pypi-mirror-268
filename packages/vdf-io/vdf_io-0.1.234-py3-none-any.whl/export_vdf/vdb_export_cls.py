import datetime
import pandas as pd
import os
import abc
from typing import Any, Dict

from util import extract_data_hash


class ExportVDB(abc.ABC):
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "DB_NAME_SLUG"):
            raise TypeError(
                f"Class {cls.__name__} lacks required class variable 'DB_NAME_SLUG'"
            )

    def __init__(self, args):
        self.args = args
        self.file_structure = []
        self.file_ctr = 1
        self.hash_value = extract_data_hash(self.args)
        self.timestamp_in_format = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        self.vdf_directory = f"vdf_{self.timestamp_in_format}_{self.hash_value}"
        os.makedirs(self.vdf_directory, exist_ok=True)

    @abc.abstractmethod
    def get_data(self) -> Dict[str, Any]:
        """
        Get data from vector database
        """
        raise NotImplementedError

    def save_vectors_to_parquet(self, vectors, metadata, vectors_directory):
        vectors_df = pd.DataFrame(list(vectors.items()), columns=["id", "vector"])
        # Store the vector in values as a column in the parquet file, and store the metadata as columns in the parquet file
        # Convert metadata to a dataframe with each of metadata_keys as a column
        # Convert metadata to a list of dictionaries
        metadata_list = [{**{"id": k}, **v} for k, v in metadata.items()]
        # Convert the list to a DataFrame
        metadata_df = pd.DataFrame.from_records(metadata_list)
        # Now merge this metadata_df with your main DataFrame
        df = vectors_df.merge(metadata_df, on="id", how="left")

        # Save the DataFrame to a parquet file
        parquet_file = os.path.join(vectors_directory, f"{self.file_ctr}.parquet")
        df.to_parquet(parquet_file)
        self.file_structure.append(parquet_file)
        self.file_ctr += 1

        # Reset vectors and metadata
        vectors = {}
        metadata = {}
        return len(df)
