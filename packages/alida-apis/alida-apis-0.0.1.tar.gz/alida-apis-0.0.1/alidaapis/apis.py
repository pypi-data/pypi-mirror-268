import requests
import json
import datetime
import time
from .minio_utils import download_folder,upload_folder
from .utils import read_var, update_config_property
import os, shutil
import uuid
import pandas as pd

def _get_token():
    if read_var("token") is not None:
        return read_var("token")
    else:
        if read_var("username") is not None and read_var("password") is not None: 
            token, _ = get_token(read_var("username"), read_var("password"))
            return token
        else:
            print("WARKING: no token found, please set user and password ENV variables!")

def get_token(user, password):

    payload = 'client_secret=' + read_var('INSTANCE_CLIENT_SECRET') + '&client_id=' + read_var('INSTANCE_CLIENT_ID') + '&grant_type=password&scope=openid&username='+ user +'&password=' + password
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url=read_var("url_login"), headers=headers, data=payload)

    try:
        token = json.loads(response.text)['access_token']
    except:
        token = None
    
    update_config_property(prop="token", value=token)
    
    return token, response


def start_bda(bda_id):
    url = read_var("url_base") + read_var("url_apps") + "/" + bda_id + "/start/" + str(int(bda_id)+1)
    
    payload = json.dumps({})
    headers = {
    'authorization': 'Bearer ' + _get_token(),
    'content-type': 'application/json'
    }

    return requests.request("POST", url, headers=headers, data=payload)

def get_bda_info(bda_id):

    url = read_var('URL_BASE') + read_var('URL_APPS') +"/" + bda_id

    payload = json.dumps({})
    headers = {
    'authorization': 'Bearer ' + _get_token(),
    'content-type': 'application/json'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    return json.loads(response.text)

def latest_run_status(bda_id):
    info = get_bda_info(bda_id)
    
    dateOfLastStatus = datetime.datetime.strptime("2000-01-01T00:00:00", '%Y-%m-%dT%H:%M:%S')

    for element in info['workflows']:
        for run in element['runs']:
            curr_date = datetime.datetime.strptime(run['dateOfLastStatus'][:-10], '%Y-%m-%dT%H:%M:%S')
            if curr_date>dateOfLastStatus:
                dateOfLastStatus = curr_date
                id = run['k8sRunId']
                
    for element in info['workflows']:
        for run in element['runs']:
            if run['k8sRunId'] == id:
                return run['currentStatus']

def synchronous_wait_till_bda_ends(bda_id, timeout = 60):
    time.sleep(4) # Remove this with a better way of checking that the app is running first
    start = time.time()
    # Wait while BDA is running or until the defined timeout
    while latest_run_status(bda_id=bda_id) == "RUNNING":
        time.sleep(10)
        print("App is running, wait...")
        if time.time() - start > int(timeout):
            break

def start_with_parameters(params, bda_id, wf_id = None):

    if wf_id is None:
        wf_id = str(int(bda_id)+1)

    url = read_var('URL_BASE') + read_var('URL_APPS') + "/" + bda_id + "/start/" + wf_id
    print(bda_id, wf_id)
    print(url)
    payload = json.dumps({
        "services": params
    })
    
    headers = {
        'authorization': 'Bearer ' + _get_token(),
        'content-type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
        
    return response 

def get_dataset_metadata(dataset_id):

    url = read_var("URL_BASE") + read_var("URL_DATASETS") + "/" + str(dataset_id)

    payload = {}
    headers = {
        'authorization': 'Bearer ' + _get_token(),
    }

    return requests.request("GET", url, headers=headers, data=payload)

def get_datasources_list():
    
    url = read_var("url_base") + read_var("url_datasources")
    
    payload = {}
    headers = {
        'authorization': 'Bearer ' + _get_token(),
    }

    return requests.request("GET", url, headers=headers, data=payload)

def get_datasource_by_id(id):
    datasources = json.loads(get_datasources_list().text)
    for datasource in datasources:
        if datasource['id'] == id:
            return datasource


def get_datasource_by_name(name):
    datasources = json.loads(get_datasources_list().text)
    for datasource in datasources:
        if datasource['name'] == name:
            return datasource

def download_dataset(dataset_id, local_path="./tmp/data/"):
    
    metadata = json.loads(get_dataset_metadata(dataset_id=dataset_id).text)
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

def get_bdas(order="id"):

    payload = {}
    headers = {
        'authorization': 'Bearer ' + _get_token(),
    }

    response = requests.request("GET", url = read_var('URL_BASE') + read_var('URL_APPS') + "?order="+order, headers=headers, data=payload)

    return response

def get_bdas_with_name(name):
    bdas = []
    response = get_bdas()

    for element in json.loads(response.text)['collection']:
        if element['name'].lower()==name.lower():
            bdas.append(element)

    return bdas, response

def create_bda(bda):
    payload = bda
    headers = {
        'authorization': 'Bearer ' + _get_token(),
        'content-type': 'application/json'
    }
    response = requests.request("POST", url = read_var('URL_BASE') + read_var('URL_APPS'), headers=headers, data=json.dumps(payload))
    return response
    
def get_services(order = "id"):
    url = read_var("url_base") + read_var("url_services")+ "?order="+order

    payload = {}
    headers = {
        'authorization': 'Bearer ' + _get_token()
    }
    return requests.request("GET", url, headers=headers, data=payload)

def get_services_by_name(name):
    result = []
    services = json.loads(get_services().text)['collection']
    
    for service in services:
        if service['name'] == name:
            result.append(service)
    return result

def get_service_by_id(id):
    url = read_var("URL_ADD_SERVICES") + "/" + str(id)
    payload = {}
    headers = {
        'authorization': 'Bearer ' + _get_token()
    }
    return requests.request("GET", url, headers=headers, data=payload)

def add_service(service_metamodel):
    
    url = read_var("url_add_services")

    payload = service_metamodel
    headers = {
        'authorization': 'Bearer ' + _get_token(),
        'content-type': 'application/json'
    }
    return requests.request("POST", url, headers=headers, data=json.dumps(payload))

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
    

def register_tabular_dataset(path, remote_path, name, description=None, columns_metadata=None, datasource_id=None, datasource_name=None, tags=[]):
    if columns_metadata is None:
        columns_metadata = get_cols_metadata_from_csv(path=path)
    
    if datasource_id is None:
        datasource = get_datasource_by_name(datasource_name)
    else: 
        datasource = get_datasource_by_id(datasource_id)
    
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



def upload_and_register_tabular_dataset_from_file(path, name, description=None, datasource_id=None, datasource_name=None, tags=[]):
    if datasource_id is None:
        datasource = get_datasource_by_name(datasource_name)
    else: 
        datasource = get_datasource_by_id(datasource_id)

    # create tmp folder
    folder_id = str(uuid.uuid4())
    os.mkdir(folder_id)
    shutil.copy(src="example_dataset.csv", dst = folder_id + "/")
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
    
    response = register_tabular_dataset(path=path, remote_path=remote_path, name=name, description=description, datasource_id=datasource_id, datasource_name=datasource_name)
    return response
