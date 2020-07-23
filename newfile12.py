#n=[2,4,6,70,8,10]
#n1=[2,3,4,5,6,7]
#even=[]
#for num in n1:
#    even.append(num%2==0)
#print(even)
#print(any(even))
#print(all(even))
#even=[i%2==0 for i in n1]
#print(all(even))
#print(any(even))
#n1=[2,3,4,5,6,7]
#def sums(*args):
#    if all([type(i)==type(4) or type(i)==type(4.5) for i in args]):
#        total=0
#        for i in args:
#            total+=i
#            i=i+1
#        print(total)
#    else:
#        print("Wrong input!!!")
#sums(*n1)
#name=["shubham","Amit","satish","nikhil"]
#length=[]
#for i in name:
#    length.append(len(i))    
#print(max(length))
#def fun(item):
#    return len(item)
#print(max(name,key=fun))
#name=["shubham","Amit","satish","nikhil"]
#print(min(name,key=lambda item:len(item)))
#scores=[
#{"name":"shubham","score":92,"age":20},
#{"name":"amit","score":80,"age":22},
#{"name":"satish","score":72,"age":21}
#]
#print(max(scores,key=lambda item:item.get("score"))["name"])
#print(min(scores,key=lambda item:item.get("score"))["name"])
#scores1={
#"harshit":{"score":82,"age":24},
#"Shubham":{"score":92,"age":20},
#"amit":{"score":85,"age":22}
#}
#print(min(scores1,key=lambda item:scores1[item]["score"]))
#name=["shubham","Amit","satish","nikhil"]
#names=("shubham","Amit","satish","nikhil")
#name.sort()
#print(name)
#print(sorted(names))
#print(sorted(name))
#print("1) "+sum.__doc__+"\n")
#print("2) "+len.__doc__+"\n")
#print("3) "+max.__doc__+"\n")
#print("4) "+min.__doc__+"\n")
#def add(a,b):
#    '''This is function which takes 2 arguments and return their sum.'''
#    return a+b
#print(add.__doc__)
#print(help(sum))