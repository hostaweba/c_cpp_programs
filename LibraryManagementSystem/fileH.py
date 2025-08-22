fh= open("projects.txt","r")#open file in read mode

curtext=fh.read(); # Read the file an store as string
txtArr=curtext.split("\n")#Split string  at new line feeds
#declare arrays
Projects=[]
ProjID=[]
ProjEmp=[]
ProjAss=[]
txtAss=""
proj="\t"
#fill array with projects, Project ID, Project member details
for i in range(10):
    Projects.append(txtArr[i])
for i in range(10, 16,1):
    ProjEmp.append(txtArr[i])
for i in range(16,26,1):
    ProjID.append(txtArr[i])
for i in range(26,32,1):
    ProjAss.append(txtArr[i])    


ch=0
while ch<8:
    #create Menu and Read option entered
    print("___________________________________________________________ ")
    print("Menu.. ")
    print("___________________________________________________________ ")
    print("1. Display Project Title by Project ID")
    print("2. Display Project ID by Project Title")
    print("3. Display Employees working on a project with given ID")
    print("4. Display Projects an employee is working ")
    print("5. Display Employees working on X number of projects")
    print("6. Display All Projects with IDs")
    print("7. Display all Details")
    print("8. Exit Program")
    ch=int(input("enter your choice--->"))
    if (ch<0 or ch>7):
        print("Wrong Choice")
        ch=1
        continue
    if ch==1:
        projID=input("Enter Project ID--->")
        try:
            print(Projects[ProjID.index(projID)])
        except ValueError:        
            print("No such project ID exists")
    if ch==2:
        projName=input("Enter Project Name--->")
        try:
            print(ProjID[Projects.index(projName)])
        except ValueError:        
            print("No such project Name exists")    
    if ch==3:
        empNames=""
        projID=input("Enter Project ID--->")
        try:
            pind= ProjID.index(projID)
        except ValueError:        
            print("No such project ID exists")
            continue
        for i in range(len(ProjEmp)):
            pa=ProjAss[i]
            if pa[pind]=='1':
                empNames=empNames+(ProjEmp[i])+","
        
        if empNames=="":
            print("No One is Working on this project")
        else:    
            print(empNames[0:len(empNames)-1])
    if ch==4:
        eind=""
        proNames=""
        empName=input("Enter Employee Name--->")
        try:
            eind= ProjEmp.index(empName)
        except ValueError:        
            print("No Employee with this name exists")
            continue
        for i in range(len(Projects)):
            el=ProjAss[eind]
            if el[i]=='1':
                proNames=proNames+(Projects[i])+","
        if proNames=="":
            print("No Project Assigned")
        else:    
            print(proNames[0:len(proNames)-1])
    if ch==5:
        proNames=""
        empCnt=int(input("Enter count of projects--->"))
        cnt=0
        for i in range(len(ProjEmp)):
            premp=ProjAss[i]
            cnt=0
            for j in range(len(Projects)):
                if premp[j]=='1':
                    cnt=cnt+1
            if cnt==empCnt:
                proNames=proNames+(ProjEmp[i])+","

        if proNames=="":
            print("Data Not Available")
        else:    
            print(proNames[0:len(proNames)-1])
    if ch==6:
        #Display all project IDs in First Row and names in second row
        for i in range(len(ProjID)):
            print(ProjID[i]+"\t"+Projects[i])
             
    if ch==7:
        #Display all project IDs in First Row
        for i in range(len(ProjID)):
            proj=proj+ProjID[i]+"\t"
        #Display Employees and projects they are working on    
        print("\t"+proj)
        txtpp="\t"
        for i in range(len(ProjEmp)):
            txtAss=ProjAss[i]
            txtAss=txtAss.replace("1","Y\t")
            txtAss=txtAss.replace("0","N\t")
            print(ProjEmp[i]+"\t"+txtAss) 

