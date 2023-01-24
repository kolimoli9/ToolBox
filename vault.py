from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import requests
def login():
    pwd=input('Password: ')
    r = requests.post('http://127.0.0.1:8000/login/', json={
        "username":'kolimoli9',
        "password":pwd
            })
    data=r.json()
    return data['access']

def safeKeeping():
        text = input('Enter Record: ')
        time = datetime.now(ZoneInfo('Israel')).strftime('%Y-%m-%d %H:%M:%S')
        desc = input('Description: (/leave blank) \n')
        if desc=='':
            desc='None was given'
        r = requests.post('http://127.0.0.1:8000/add/', json={
        "text": text,
        "time": time,
        "desc":desc
        })
        return r.status_code
        
def showVault():
    token =login()
    r = requests.get('http://127.0.0.1:8000/withdraw/',headers={'Authorization': f'Bearer {token}' })
    print(r.json())