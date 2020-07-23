#import os
#import shutil
#exten_dict={
#"Audio": (".mp3",".m4a",".wav",".flac"),
#"Video":(".mp4",".mkv",".alv",".mpeg","3gp"),
#"doc" : (".docx",".pdf","csv","txt")
#}

#path=input("Enter folder path : ")
#def file_separator(Path,Extension):
#    files=[]
#    for file in os.listdir(Path):
#        for exten in Extension:
#            if file.endswith(exten):
#                files.append(file)
#    return files
#                
#print(file_separator(path,docs))
#for key,value in exten_dict.items():
#    
#    os.mkdir(key)
#    newpath=path+"/"+key
#    for item in file_separator(path,value):
#        item_path=os.path.join(path,item)
#        item_newpath=os.path.join(path,item)
#        newpath=path+"/"+key+"/"+item
#        shutil.copy(item,item_path)
#    print(f"{key}s are --->")
#    print(file_separator (path,value))
#/storage/emulated/0/python