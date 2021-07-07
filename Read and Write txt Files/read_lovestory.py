with open(r"Read and Write txt Files\love.txt","r",encoding="utf-8") as rf:
    print(rf.encoding)
    read_love=rf.read()
    print(read_love)