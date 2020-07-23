#d=dict.fromkeys(['name','age','pass1'],)
#print(d)
#d=dict.fromkeys("shubham",)
#print(d)
#names={1 : 'shubham',1 : 'amit',3 : 'satish'}
#name="shubham"
#d=dict.fromkeys(range(1,4),name)
#print(d)
#print(names.get(1))
#print(names.get(2))
#print(names.get(31,'not found'))
#d.clear()
#d1=d.copy()
#print(d1)
#n1=input("Enter any no. b/w 1-10 : ")
#n=int(n1)
#i=0
#def cube(n):
#    cubes={}
#    for i in range(1,n+1):
#        cubes[i]=i**3
#    return cubes
#print(cube(n))
#name=input("Enter your name : ")
#def words(name):
#    wordcount={}
#    for i in range(0,len(name)):
#        wordcount[name[i]]=name.count(name[i])
#    return wordcount
#print(words(name))
#user={}
#user['name']=input("Enter your name : ")
#user['age']=input("Enter your age : ")
#user['pass1']=input("Enter your password : ")
#user['email']=input("Enter your email : ")
#for key,value in user.items():
#    print(f"{key} : {value}")
#print(user)
#n2=[1,2,3,4,5,6,6,6,6,7,7,7,8]
#n={1,2,3,4,5,6,6,6,6,7,7,7,8}
#n1=list(n2)
#n3=list(set(n1))
#n.add(9)
#n.add(10)
#n.remove(10)
#n.discard(10)
#n4=n.copy()
#n4.remove(3)
#n4.remove(4)
#n.clear()
#print(n)
#print(n1)
#print(n2)
#print(n3)
#print(n4)
#if 5 in n4:
#    print("present")
#else:
#    print("absent")
#for i in n4:
#    print(i)
#union= n | n4
#intersection= n & n4
#print(union)
#print(intersection)