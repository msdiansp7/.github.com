#from csv import reader
#from csv import DictReader

#with open("untitled.csv","r") as f:
#    csv_reader=DictReader(f)
#    csv_reader=DictReader(f,delimiter="#")
#    csv_reader=reader(f)
#    next(csv_reader)
#    for row in csv_reader:
#        print(row)
#        print(row["name"])
#        print(row["email"])
#        print(row["phone"])
#    print(csv_reader)
#from csv import writer

#with open("create.csv","w") as f:
#    csv_writer=writer(f)
#    csv_writer.writerow(["Name","Age","Password"])
#    csv_writer.writerow(["shubham",20,"shubham@123"])
#    csv_writer.writerow(["amit","22","amit@123"])
#    csv_writer.writerows([["Name","Age","Password"],["shubham",20,"shubham@123"],["amit","22","amit@123"]])
#from csv import DictWriter
#with open("final.csv","w",newline="") as f:
#    csv_writer=DictWriter(f,fieldnames=["name","age","pass"])
#    csv_writer.writeheader()
#    csv_writer.writerow({"name":"Shubham","age":20,"pass":"shubham@123"})
#    csv_writer.writerow({"name":"amit","age":22,"pass":"amit@123"})
#    csv_writer.writerows([{"name":"Shubham","age":20,"pass":"shubham@123"},{"name":"amit","age":22,"pass":"amit@123"}]
#    )
#from csv import DictReader,DictWriter

#with open("final.csv","r") as rf:
#    with open("Rewrite.csv","w") as wf:
#        csv_reader=DictReader(rf)
#        csv_writer=DictWriter(wf,fieldnames=["fname","age","pass"])
#        csv_writer.writeheader()
#        for row in csv_reader:
#            fN,A,Pass=row["name"],row["age"],row["pass"]
#            csv_writer.writerow({"fname": fN,"age":A,"pass":Pass})