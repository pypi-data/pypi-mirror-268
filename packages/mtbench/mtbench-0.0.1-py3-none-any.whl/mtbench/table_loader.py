from typing import Tuple, Dict, Optional, List
import pandas as pd
import numpy as np

from .dataset_meta import (
    MTBTableDataFormat
)

def get_table_data_loader(format : MTBTableDataFormat):
    if format not in LOADER_MAP:
        raise ValueError(f"Unsupported table format: {format}")
    return LOADER_MAP[format]

def parquet_loader(path : str) -> Dict[str, np.ndarray]:
    df = pd.read_parquet(str(path))
    return { col : df[col].to_numpy() for col in df }

def numpy_loader(path : str) -> Dict[str, np.ndarray]:
    npz = np.load(path, allow_pickle=True)
    return { name : npz[name] for name in npz.files }

LOADER_MAP = {
    MTBTableDataFormat.PARQUET : parquet_loader,
    MTBTableDataFormat.NUMPY : numpy_loader,
}
