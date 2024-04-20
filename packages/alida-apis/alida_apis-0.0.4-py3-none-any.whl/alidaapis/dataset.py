from .utils import read_var
from .auth import _get_token
import requests, json
from .minio_utils import download_folder, upload_folder
import os, shutil
import uuid
import pandas as pd
import alidaapis.datasource as ds

def get_metadata(dataset_id):

    url = read_var("URL_BASE") + read_var("URL_DATASETS") + "/" + str(dataset_id)

    payload = {}
    headers = {
        'authorization': 'Bearer ' + _get_token(),
    }

    return requests.request("GET", url, headers=headers, data=payload)


# Starting from a CSV file, infer metadata
def get_cols_metadata_from_csv(path):
    df = pd.read_csv(path)

    pd_types_to_platform_types = {
        "int64": "Number",
        "float64": "Number",
        "object": "String",
        "bool": "String",
        "datatime": "Date"
    }

    col_types = dict(df.dtypes)

    columns = []
    for col in col_types.keys():
        columns.append({"name": col, "type": pd_types_to_platform_types[str(col_types[col])]})

    return columns
    

def register_tabular(path, remote_path, name, description=None, columns_metadata=None, datasource_id=None, datasource_name=None, tags=[]):
    if columns_metadata is None:
        columns_metadata = get_cols_metadata_from_csv(path=path)
    
    if datasource_id is None:
        datasource = ds.get_by_name(datasource_name)
    else: 
        datasource = ds.get_by_id(datasource_id)
    
    url = read_var("URL_BASE") + read_var("URL_DATASETS")

    payload = {
        "datasetFileType": {
            "type": "table",
            "columns": columns_metadata,
            "tableName": remote_path,
            "path": None
        },
        "datasource": datasource,
        "name": name,
        "description": description,
        "tags": tags
    }
    headers = {
        'authorization': 'Bearer ' + _get_token(),
        'content-type': 'application/json'
    }
    return requests.request("POST", url, headers=headers, data=json.dumps(payload))



def upload_and_register_tabular_from_file(path, name, description=None, datasource_id=None, datasource_name=None, tags=[]):
    if datasource_id is None:
        datasource = ds.get_by_name(datasource_name)
    else: 
        datasource = ds.get_by_id(datasource_id)

    # create tmp folder
    folder_id = str(uuid.uuid4())
    os.mkdir(folder_id)
    shutil.copy(src=path, dst = folder_id + "/")
    remote_path = os.path.join(datasource['prefixPath'], folder_id)
    
    endpoint_url = datasource['host'] + ":" + str(datasource['port'])

    # Check if ssl or not
    if not endpoint_url.startswith('http'):
        if datasource['secure']== True:
            endpoint_url = "https://" + endpoint_url
        else:
            endpoint_url = "http://" + endpoint_url
    
    # Upload dataset to Minio
    for result in upload_folder(minio_address=endpoint_url, 
                                minio_access_key=datasource['accessKey'], 
                                minio_secret_key=datasource['secretKey'], 
                                bucket_name=datasource['bucket'], 
                                local_path=folder_id, 
                                remote_path=remote_path):
        pass
    
    # Remove tmp folder
    shutil.rmtree(folder_id)
    
    response = register_tabular(path=path, remote_path=remote_path, name=name, description=description, datasource_id=datasource_id, datasource_name=datasource_name)
    return response



def download(dataset_id, local_path="./tmp/data/"):
    
    metadata = json.loads(get_metadata(dataset_id=dataset_id).text)
    datasource = metadata['datasource']
    access_key = datasource['accessKey']
    secret_key = datasource['secretKey']
    bucket_name = datasource['bucket']
    endpoint_url = datasource['host'] + ":" + str(datasource['port'])
    if not endpoint_url.startswith('http'):
        if datasource['secure']== True:
            endpoint_url = "https://" + endpoint_url
        else:
            endpoint_url = "http://" + endpoint_url
    if 'path' in metadata['datasetFileType'] and metadata['datasetFileType']['path'] is not None:
        path = metadata['datasetFileType']['path']
    else:
        path = metadata['datasetFileType']['tableName']

    if path[-1]!="/":
        path+="/"
            
    for result in download_folder(minio_address=endpoint_url, minio_access_key=access_key, minio_secret_key=secret_key, bucket_name=bucket_name, local_path=local_path, remote_path=path):
        pass
