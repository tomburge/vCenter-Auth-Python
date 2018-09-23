import requests
import configparser

class Config:
    config = configparser.ConfigParser()
    config.read('config.ini')
    host = config['vCenter']['host']
    api_url = config['vCenter']['api_url']
    user = config['vCenter']['user']
    password = config['vCenter']['password']


def authvcconfig():
    auth = Config()
    r = requests.post(auth.host + auth.api_url, auth=(auth.user, auth.password), verify=False)
    if r.status_code == 200:
        print(f'Authentication Success for {auth.user}')
        return r.json()['value']
    else:
        return print(f'Authentication Failure for {auth.user}.')


def authvcman():
    host = input('Enter vCenter FQDN (Ex. https://vc01.home.lab): ')
    api_url = '/rest/com/vmware/cis/session'
    user = input('Enter vCenter Username: ')
    password = input('Enter vCenter Password: ')
    r = requests.post(host + api_url, auth=(user, password), verify=False)
    if r.status_code == 200:
        print(f'Authentication Success for {user}')
        return r.json()['value']
    else:
        return print(f'Authentication Failure for {user}.')