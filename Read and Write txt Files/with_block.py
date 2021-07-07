with open(r"Read and Write txt Files\file1.txt") as f:
    data=f.read()
    print(data)
print(f.closed)    