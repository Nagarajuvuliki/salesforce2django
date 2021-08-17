import requests
import json
def get_token():
    ls=[]
    login_details = {
        "grant_type": "password",
        "client_id": "3MVG9fe4g9fhX0E52uj8SdOHGubOlhne1nRq6GeYugQQqnJhX5ChSsHyZbVliHKZXAZSjbJUc9DgLpAAAtX7L",
        "client_secret": "6FD4DF54C15ED3FF82BDCED744C5FDD67179B728A7E1460BDAD01DE2E2424D32",
        "username": "",
        "password": "nagaswrn1hhTf8InXk4kKl8wP6tMtQ6tO" 
    }
    r = requests.post("https://login.salesforce.com/services/oauth2/token", params=login_details)
    user_token = ls.append(r.json().get("access_token"))
    instance_url = ls.append(r.json().get("instance_url"))
    return ls
l=get_token()
print(l[0])
