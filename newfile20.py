#file=open('newfile8.py','r')
#print(file.tell())
#print(file.read())
#file.seek(0)
#print("Duplicate ------>\n\n")
#print(file.read())
#print(file.tell())
#file=open('newfile8.py','r')
#print(file.readline())
#lines=file.readlines()
#print(lines)
#file.close()
#file=open('newfile8.py','r')
#print(file.name)
#print(file.closed)
#for line in file.readlines()[:4]:
#    print(line)
#file.close()
#print(file.closed)
#with open("pythonDebugger.py") as f:
#    file = f.read ()
#    print(file)
#with open("virus.py","r") as rf:
#    with open("newfile20.py","w") as wf:
#        wf.write(rf.read())
#with open("names.py","r") as f:
#    with open("virus.py","a") as wf:
#        for line in f.readlines():
#            name,age=line.split(",")
#            wf.write(f"{name} is {age} years old.")
#            for name,age in line:
#                name=f"{name} is {age} years old."
#f=open("virus.py","r")
#f.read()
#f.close()
#with open("names.py","r") as f:
#    with open("new.py","a") as n:
#        for line in f.readlines():
#            if "<a href=" in line:
#                pos=line.find("<a href=")
#                start=line.find("\"",pos)
#                end=line.find("\"",start+1)
#                url=line[start+1:end+1]
#                print(url)
#                n.write(url+"\n")
#with open("names.py","r") as f:
#    with open("new.py","a") as n:
#        link_exist=True
#        while link_exist:
#            page=f.read()
#            pos=page.find("<a href=")
#            if pos==-1:
#                link_exist=False
#            else:
#                start=page.find("\"",pos)
#                end=page.find("\"",start+1)
#                url=page[start+1:end-1]
#                page=page[end:]
#with open("minute.txt","r",encoding="utf-8") as f:
#    print(f.encoding)
#    print(f.read())
#with open("untitled.txt","r",encoding="utf-8") as f:
#    print(f.encoding)
#    print(f.read())