from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import requests
import os

m4=""" 

Type the item's number for more details:                a) To ABORT

"""


def AV(vault):
    while True:
        for item in vault:
            print('\n ',item['index'],': ',item['desc'])
        action = input(m4)
        try:
            if int(action) in range(0,100):
                os.system('cls')
                for item in vault:
                    if item['index']==int(action):
                        pick=item
                print('========================')        
                print('Description: \n')
                print('   ',pick['desc'],'\n')
                print('Content: \n')
                print('   ',pick['text'],'\n')        
                print('Time: \n')
                print('   ',pick['time'],'\n')
                print('========================')
            else:
                print('! Chosen Index Does Not Exist !')
        except:return
        





def login():
    pwd=input('Password: ')
    os.system('cls')
    r = requests.post('http://toolbox-sr.azurewebsites.net/login/', json={
        "username":'kolimoli9',
        "password":pwd
            })
    data=r.json()
    if r.status_code!=401:return data['access']
    else:return False
    

def safeKeeping():
        text = input('Enter Record: ')
        time = datetime.now(ZoneInfo('Israel')).strftime('%Y-%m-%d %H:%M:%S')
        desc = input('Description: (/leave blank) \n')
        if desc=='':
            desc='None was given'
        r = requests.post('http://toolbox-sr.azurewebsites.net/add/', json={
        "text": text,
        "time": time,
        "desc":desc
        })
        return r.status_code
        
def showVault():
    token =login()
    if type(token)==str:
        r = requests.get('http://toolbox-sr.azurewebsites.net/withdraw/',headers={'Authorization': f'Bearer {token}' })
        data=r.json()
        i=1
        vault=[]
        
        for d in data:
            d['index']=i
            i+=1
            vault.append(d)
        
        return vault
                   
    else:
        print('!!!!!!!!\nPwd is incorrect\n!!!!!!!!')