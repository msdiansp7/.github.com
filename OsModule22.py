#import os
#import shutil

#os.mkdir("python2")
#print(os.path.exists ("python2"))
#if os.path.exists("python3"):
#    print("file already exists.")
#else:
#    os.mkdir("python3")
#open("new.txt","a").close()

#print(os.getcwd())
#os.chdir("/storage/emulated/0")
#print(os.getcwd())
#os.mkdir("python2")
#open("python2/python.txt","a").close()
#print(os.listdir())
#for file in os.listdir():
#    print(file)
#print(os.listdir("/storage/emulated/0"))
#print(len(os.listdir("/storage/emulated/0")))
#for item in os.listdir():
#    print(os.path.join(os.getcwd(),item))
#    print("/storage/emulated/0/python"+"\\"+item)
#os.chdir("/storage/emulated/0/python")
#files = os.walk(os.getcwd())
#for A,B,C in files:
#    print(f"path = {A} ")
#    print(f"folder = {B} ")
#    print(f"files = {C} ")
#os.makedirs("shubham/patil")
#shutil.rmtree("shubham")
#shutil.copytree("python2","python3/shubham")
#os.chdir("/storage/emulated/0")
#shutil.copy("form.html","python/virus.html")
#shutil.move("form.html","python2/form.html")
#shutil.move("python2","python4/python5")