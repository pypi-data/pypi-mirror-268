from enum import Enum


class HTTPMethod(Enum):
    """
    Enum class to represent HTTP methods
    """

    GET = "GET"
    PUT = "PUT"
    POST = "POST"
    PATCH = "PATCH"
    DELETE = "DELETE"


class DataCategory(Enum):
    """
    **Fields:**

        - INPUT
        - PREDICTION
        - TARGET
        - INPUT_MAPPING
        - TARGET_MAPPING
        - PREDICTION_MAPPING
    """

    PREDICTION = "prediction"
    TARGET = "target"
    INPUT = "input"
    INPUT_MAPPING = "input_mapping"
    TARGET_MAPPING = "target_mapping"
    PREDICTION_MAPPING = "prediction_mapping"


class RawDataSourceType(Enum):
    """
    Enumeration of raw data source types.
    """

    AWS_S3 = "aws_s3"
    GCS = "gcs"
    ABS = "azure_blob_storage"
    LOCAL = "local"
