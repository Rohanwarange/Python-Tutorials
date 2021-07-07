with open(r"Read and Write txt Files\exersise1.txt","r") as rf:
    with open(r"Read and Write txt Files\exersise1a.py","a") as wf:
        for line in rf.readlines():
            name,salary=line.split(",")
            wf.write(f"{name} salary is {salary}")
