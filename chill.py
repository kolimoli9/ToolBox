import webbrowser as w
import os
m1="""
What is our pick for this evening ?
    1) Netflix
    2) Disney

3)Back
"""
m2= """
What Janere ?
    1) Horror
    2) Comedy
    3) Thrillers
    4) Adventure
"""


def netflix(type):
    w.open(f'https://www.netflix.com/search?q={type}',new=1)
    return
 
def disney(type):
    w.open(f'https://www.apps.disneyplus.com/il/explore?search_query={type}',new=1)
    return










def WhatToWatch():
    os.system('cls')
    while True:
        action=input(m1)
        if action =='1':
            os.system('cls')
            action=input(m2)
            os.system('cls') 
            if action=='1':
                netflix('horror')
                return
            if action=='2':
                netflix('comedy')
                return
            if action=='3':
                netflix('thriller')
                return
            if action=='4':
                netflix('adventure')
            
        if action == '2':
            os.system('cls')
            action=input(m2)
            os.system('cls') 
            if action=='1':
                disney('horror')
                return
            if action=='2':
                disney('comedy')
                return
            if action=='3':
                disney('thriller')
                return
            if action=='4':
                disney('adventure')
        else:
            os.system('cls')
            return
