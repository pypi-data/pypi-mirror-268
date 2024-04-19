from finter.settings import get_api_client, logger
from finter.rest import ApiException
import finter

import pandas as pd
import s3fs


def get_aws_credentials():
    api_instance = finter.AWSCredentialsApi(get_api_client())

    try:
        api_response = api_instance.aws_credentials_retrieve()
        return api_response
    except ApiException as e:
        print("Exception when calling AWSCredentialsApi->aws_credentials_retrieve: %s\n" % e)


def get_parquet_df(identity_name):

    credentials = get_aws_credentials()
    fs = s3fs.S3FileSystem(
        key=credentials.aws_access_key_id,
        secret=credentials.aws_secret_access_key,
        token=credentials.aws_session_token,
    )

    model_type = identity_name.split(".")[0]
    s3_bucket_name = "cm-parquet"
    file_name = f"{identity_name}.parquet"
    s3_uri = f"s3://{s3_bucket_name}/{model_type}/{file_name}"  # model_type

    with fs.open(s3_uri, "rb") as f:
        df = pd.read_parquet(f, engine="pyarrow")

    logger.info(f"Loading {model_type} model by reading parquet: {identity_name}")
    return df
