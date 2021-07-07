from csv import reader
with open(r"work with csv Files\file1.csv","r") as f:
    csv_reader=reader(f)
    # itterator
# print(csv_reader)    
# print(type(csv_reader))   
    next(csv_reader) 
    for rows in csv_reader:
        print(rows)