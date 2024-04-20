import requests
import json
from .auth import _get_token
from .utils import read_var


def get(order = "id"):
    url = read_var("url_base") + read_var("url_services")+ "?order="+order

    payload = {}
    headers = {
        'authorization': 'Bearer ' + _get_token()
    }
    return requests.request("GET", url, headers=headers, data=payload)

def get_services_by_name(name):
    result = []
    services = json.loads(get().text)['collection']
    
    for service in services:
        if service['name'] == name:
            result.append(service)
    return result

def get_by_id(id):
    url = read_var("URL_ADD_SERVICES") + "/" + str(id)
    payload = {}
    headers = {
        'authorization': 'Bearer ' + _get_token()
    }
    return requests.request("GET", url, headers=headers, data=payload)

def add(service_metamodel):
    
    url = read_var("url_add_services")

    payload = service_metamodel
    headers = {
        'authorization': 'Bearer ' + _get_token(),
        'content-type': 'application/json'
    }
    return requests.request("POST", url, headers=headers, data=json.dumps(payload))

