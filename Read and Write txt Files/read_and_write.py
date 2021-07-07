with open(r"D:\python tutorials\Read and Write txt Files\file1.txt","r") as rf:
    data=rf.read()
    with open(r"D:\python tutorials\Read and Write txt Files\file2.txt","a") as wf:
         data=wf.write(data)