from salestodjango import gettoken
import requests
import json
token=gettoken.get_token()
def get_data_from_sf(action, parameters = {}, method = 'get', data = {}):
    headers = {
        'Content-type': 'application/json',
        'Accept-Encoding': 'gzip',
        'Authorization': 'Bearer %s' % token[0]
    }
    if method == 'get':
        r = requests.request(method, token[1]+action, headers=headers, params=parameters, timeout=30)
    elif method in ['post', 'patch']:
        r = requests.request(method, token[1]+action, headers=headers, json=data, params=parameters, timeout=10)
    else:
        raise ValueError('Method should be get or post or patch.')
    if r.status_code < 300:
        if method=='patch':
            return None
        else:
            return r.json()
    else:
        raise Exception('API error when calling %s : %s' % (r.url, r.content))
def Insertusers():
    context={}
    at=gettoken.get_token()
    context["token"]=at[0]
    re=json.dumps(get_data_from_sf('/services/data/v39.0/query/', {
    'q': 'SELECT Username,Firstname,Email,Lastname FROM User'
    }), indent=2)
    lo=json.loads(re)
    for i in lo["records"]:
        del i["attributes"]
    loo=json.dumps(lo,indent=1)
    dic=json.loads(loo)
    return dic
def InsertAccount():
    context={}
    at=gettoken.get_token()
    context["token"]=at[0]
    re=json.dumps(get_data_from_sf('/services/data/v39.0/query/', {
    'q': 'SELECT Name,Accountnumber,AnnualRevenue,LastActivityDate FROM account'
    }), indent=2)
    lo=json.loads(re)
    for i in lo["records"]:
        del i["attributes"]
    loo=json.dumps(lo,indent=1)
    dic=json.loads(loo)
    return dic
def InsertContact():
    context={}
    at=gettoken.get_token()
    context["token"]=at[0]
    re=json.dumps(get_data_from_sf('/services/data/v39.0/query/', {
    'q': 'SELECT Name,Email,AccountID,Phone  FROM contact'
    }), indent=2)
    lo=json.loads(re)
    for i in lo["records"]:
        del i["attributes"]
    loo=json.dumps(lo,indent=1)
    dic=json.loads(loo)
    return dic