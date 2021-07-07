from csv import DictReader
# order dics 
with open(r"work with csv Files\file1.csv","r") as f:
    csv_reader=DictReader(f)
    for rows in csv_reader:
        print(rows)
        print(rows["email"])