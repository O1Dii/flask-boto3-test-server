from io import StringIO

import boto3
import pandas as pd


def file_download(file_name, bucket_name):
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket_name, file_name)

    return pd.read_csv(StringIO(obj.get()['Body'].read().decode('utf-8')),
                       low_memory=False, index_col=0)


def file_upload(file_name, bucket_name, s3_file_name=''):
    s3 = boto3.client('s3')

    s3.upload_file(file_name, bucket_name, s3_file_name or file_name)
