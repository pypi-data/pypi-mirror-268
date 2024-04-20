import requests

API_URL = "https://api.codeflex.com.co/mysql_connector"

HEADERS = {
    "Content-Type": "application/json"
}
 
def CREATEDB(username, database):
    jsonData = {
        "action": "CREATEDB",
        "username": username,
        "database": database
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
     

def DELETEDB(username, database):
    jsonData = {
        "action": "DELETEDB",
        "username": username,
        "database": database
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err


def DBQUERY(username, password):
    jsonData = {
        "action": "DBQUERY",
        "username": username,
        "pass": password
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
     

def CREATETABLE(username, password, database, tablename):
    jsonData = {
        "action": "CREATETABLE",
        "username": username,
        "pass": password,
        "database": database,
        "tablename": tablename
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err


def CREATETABLE_CUSTOM(username, password, database, sql):
    jsonData = {
        "action": "CREATETABLE_CUSTOM",
        "username": username,
        "pass": password,
        "database": database,
        "sql": sql
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
    

def TABLEQUERY(username, password, database, tablename):
    jsonData = {
        "action": "TABLEQUERY",
        "username": username,
        "pass": password,
        "database": database,
        "tablename": tablename
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
    

def TABLEQUERY_CUSTOM(username, password, database, sql):
    jsonData = {
        "action": "TABLEQUERY_CUSTOM",
        "username": username,
        "pass": password,
        "database": database,
        "sql": sql
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
    

def TABLEINSERT_CUSTOM(username, password, database, sql):
    jsonData = {
        "action": "TABLEINSERT_CUSTOM",
        "username": username,
        "pass": password,
        "database": database,
        "sql": sql
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
    

def DELETETABLE(username, password, database, tablename):
    jsonData = {
        "action": "DELETETABLE",
        "username": username,
        "pass": password,
        "database": database,
        "tablename": tablename
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
    

def DELETETABLE_CUSTOM(username, password, database, sql):
    jsonData = {
        "action": "DELETETABLE_CUSTOM",
        "username": username,
        "pass": password,
        "database": database,
        "sql": sql
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
    

def UPDATETABLE_CUSTOM(username, password, database, sql):
    jsonData = {
        "action": "UPDATETABLE_CUSTOM",
        "username": username,
        "pass": password,
        "database": database,
        "sql": sql
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err


def CONNECTOR(username, password, database, sql):
    jsonData = {
        "action": "CONNECTOR",
        "username": username,
        "password": password,
        "database": database,
        "sql": sql
    }
    try:
        response = requests.post(API_URL, json=jsonData, headers=HEADERS)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.HTTPError as http_err:
        return http_err
    except Exception as err:
        return err
 