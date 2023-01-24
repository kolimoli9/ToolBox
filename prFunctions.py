import wmi
import json
import sys



def terminate_process_id(process_name):
    p = wmi.WMI()
    for process in p.Win32_Process (Name=process_name):
        print(process.ProcessId, process.Name)

    try:
        process.Terminate()
        print("Process terminated successfully: %d" % process.ProcessId)
    except:
        print("There is no process running with id: %d" % process_name)

def createRecords():
    try:
        f=open('records.json','r')
        f.close()
    except:    
        f = wmi.WMI()
        ProcessRecord = []
        for process in f.Win32_Process():
            pr = {
                'pName':process.Name
            }
            ProcessRecord.append(pr)
        with open('records.json','w') as jsonFile:
            j = json.dump(ProcessRecord,jsonFile)



def serializer():
    processIdList=[]
    recordsIdList=[]
    with open('records.json','r') as r: records = json.load(r)
    p = wmi.WMI()
    for d in records:
        recordsIdList.append(d['pName'])
    for process in p.Win32_Process():
        processIdList.append(process.Name)

    newProcess = list(set(processIdList) - set(recordsIdList))   
    susList=[]
    for process in p.Win32_Process():
        for newp in newProcess:
            if newp == process.Name: 
                sus={
                    'pid':process.ProcessId,
                    'pname':process.Name
                }
                susList.append(sus)
    if len(susList)>1:
        i=1
        for dic in susList:
            dic[i]=i
            i+=1
            
        return susList
    
def SaftyCheck():
    sus=serializer()
    while True:
        print("Here's the suspicious runing programs that i have found: \n")
        print(f'Process ID      Process Name \n')
        try:
            for s in sus:
                print(s['pid'],'      ',s['pname'])
            q1=""" 
                To >
                1) terminate a process
                2) go back 
            """
            action = input(q1)
            if action=='1':
                i=1
                for s in sus:
                    print(s[i],')',s['pid'],'      ',s['pname'])
                    i+=1
                select=input('Which process woudl you like to terminate ?')
                i=1
                for s in sus:
                    if select == str(s[i]):
                        process_name=s['pname']
                        terminate_process_id(process_name)
                        sus=serializer()   
                    i+=1

        except:print('THERE ARE NO MORE SUSPICIOUS PROGRAMS RUNING IN THE BACKGROUND');return
        
        if action=='2':
            return
        


# with open('records.json','r') as r:
#         records = json.load(r)
#     count , bcount= 0 , 0
#     p = wmi.WMI()
    
#     for d in records:
#         for process in p.Win32_Process():
#             if process.ProcessId == d['pID']:
#                 count+=1
#         bcount+=1
#     print('Done','\n',count,'\n',bcount)
        
        
#         # if process.ProcessId == d['pID']:
#         #     count+=1