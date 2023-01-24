from chill import *
from prFunctions import *
from vault import safeKeeping, showVault
import os
import psutil
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
menu = """
    ______________ 
    ||          ||
    || Tool Box ||
    ______________

    Choose Your Action : 
        1) Malware Check 
        2) Netflix & Chill
        3) CMD
        V) Vault
        S ) Save
        """








def mainLoop():
    createRecords()
    while True:
        print(f'\n CPU: {psutil.cpu_percent(4)}% || RAM: {psutil.virtual_memory()[2]}%')
        action = input(menu)
        if action == '1':
            SaftyCheck()
            os.system('cls')
        if action == '2':
            mv=WhatToWatch()
            if mv==False:mv=True
            os.system('cls')
        if action=='3':
            os.system("start cmd")
            return
        if action =='s':
            response=safeKeeping()
            print(response)
        if action =='v':
            showVault()
        
        else:return 




if __name__=='__main__':
    mainLoop()