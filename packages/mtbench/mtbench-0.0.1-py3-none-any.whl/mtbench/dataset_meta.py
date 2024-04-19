from typing import Tuple, Dict, Optional, List
from enum import Enum
import pydantic

__all__ = [
    "TIMESTAMP_FEATURE_NAME",
    "MTBColumnDType",
    "DTYPE_EXTRA_FIELDS",
    "MTBColumnSchema",
    "MTBTableDataFormat",
    "MTBTableSchema",
    "MTBTaskType",
    "TASK_EXTRA_FIELDS",
    "MTBTaskEvalMetric",
    "MTBTaskMeta",
    "MTBColumnID",
    "MTBRelationship",
    "MTBRDBDatasetMeta",
]

TIMESTAMP_FEATURE_NAME = '__timestamp__'

class MTBColumnDType(str, Enum):
    """Column data type model."""
    float_t = 'float'            # np.float32
    category_t = 'category'      # object
    datetime_t = 'datetime'      # np.datetime64
    text_t = 'text'              # str
    timestamp_t = 'timestamp'    # np.int64
    foreign_key = 'foreign_key'  # object
    primary_key = 'primary_key'  # object

DTYPE_EXTRA_FIELDS = {
    # in_size : An integer tells the size of the feature dimension.
    MTBColumnDType.float_t : ["in_size"],
    # num_categories : An integer tells the total number of categories.
    MTBColumnDType.category_t : ["num_categories"],
    # link_to : A string in the format of <TABLE>.<COLUMN>
    # capacity : The number of unique keys.
    MTBColumnDType.foreign_key : ["link_to", "capacity"],
    # capacity : The number of unique keys.
    MTBColumnDType.primary_key : ["capacity"],
}

class MTBColumnSchema(pydantic.BaseModel):
    """Column schema model.

    Column schema allows extra fields other than the explicitly defined members.
    See `DTYPE_EXTRA_FIELDS` dictionary for more details.
    """
    class Config:
        extra = pydantic.Extra.allow
        use_enum_values = True

    # Column name.
    name : str
    # Column data type.
    dtype : MTBColumnDType

class MTBTableDataFormat(str, Enum):
    PARQUET = 'parquet'
    NUMPY = 'numpy'

class MTBTableSchema(pydantic.BaseModel):
    """Table schema model."""

    # Name of the table.
    name : str
    # On-disk data path (relative to the root data folder) to load this table.
    source: str
    # On-disk format for storing this table.
    format: MTBTableDataFormat
    # Column schemas.
    columns: List[MTBColumnSchema]
    # Time column name.
    time_column: Optional[str]

    @property
    def column_dict(self) -> Dict[str, MTBColumnSchema]:
        """Get column schemas in a dictionary where the keys are column names."""
        return {col_schema.name : col_schema for col_schema in self.columns}

class MTBTaskType(str, Enum):
    classification = 'classification'
    regression = 'regression'
    retrieval = 'retrieval'

TASK_EXTRA_FIELDS = {
    MTBTaskType.classification : ['num_classes'],
    MTBTaskType.retrieval : [
        'key_prediction_label_column',
        'key_prediction_query_idx_column',
    ],
    MTBTaskType.regression : [],
}

class MTBTaskEvalMetric(str, Enum):
    auroc = 'auroc'
    ap = 'ap'
    accuracy = 'accuracy'
    f1 = 'f1'
    hinge = 'hinge'
    recall = 'recall'
    mae = 'mae'
    mse = 'mse'
    msle = 'msle'
    pearson = 'pearson'
    rmse = 'rmse'
    r2 = 'r2'
    mrr = 'mrr'
    hr = 'hr'
    ndcg = 'ndcg'

class MTBTaskMeta(pydantic.BaseModel):
    class Config:
        extra = pydantic.Extra.allow
        use_enum_values = True

    name : str
    source : str
    format : MTBTableDataFormat
    columns : List[MTBColumnSchema]
    time_column : Optional[str] = None

    evaluation_metric : MTBTaskEvalMetric
    target_column : str
    target_table : str
    task_type : Optional[MTBTaskType]
    key_prediction_label_column: Optional[str] = "label"
    key_prediction_query_idx_column: Optional[str] = "query_idx"

    @property
    def column_dict(self) -> Dict[str, MTBColumnSchema]:
        return {col_schema.name : col_schema for col_schema in self.columns}

class MTBColumnID(pydantic.BaseModel):
    table : str
    column : str

class MTBRelationship(pydantic.BaseModel):
    fk : MTBColumnID
    pk : MTBColumnID

class MTBRDBDatasetMeta(pydantic.BaseModel):
    """Dataset metadata model."""
    # Dataset name.
    dataset_name : str
    # Table schemas.
    tables : List[MTBTableSchema]
    # Task metadata.
    tasks : List[MTBTaskMeta]

    @property
    def relationships(self) -> List[MTBRelationship]:
        """Get all relationships in a list."""
        rels = []
        for table in self.tables:
            for col in table.columns:
                if col.dtype == MTBColumnDType.foreign_key:
                    link_tbl, link_col = col.link_to.split('.')
                    fk = {'table' : table.name, 'column' : col.name}
                    pk = {'table' : link_tbl, 'column' : link_col}
                    rels.append(MTBRelationship.parse_obj({
                        'fk' : fk, 'pk' : pk}))
        return rels

    column_groups : Optional[List[List[MTBColumnID]]] = None
