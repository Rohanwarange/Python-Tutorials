from csv import DictReader,DictWriter
with open(r"work with csv Files\file1.csv","r") as fr:
    with open(r"work with csv Files\file3.csv","w",newline="") as fw:
        csv_read=DictReader(fr)
        csv_write=DictWriter(fw,fieldnames=["First_name","last_name","age"]) 
        csv_write.writeheader()
        for rows in csv_read:
            First_name,last_name,age= rows["name"],rows["email"],rows["phome"]
            csv_write.writerow({
                "First_name":First_name.upper(),
                "last_name":last_name.upper(),
                "age":age
            })

