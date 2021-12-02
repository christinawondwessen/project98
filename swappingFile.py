def swapFileData():
    fileName=input("Enter the file name")
    #count=0
    #file=open(fileName,'w')
    with open(sample 1, 'r') as a:
        data_a=a.read()
    with open(sample 1, 'w') as a:
        a.write(data_b)
    with open(sample 2, 'r') as b:
        data_b=b.read()
    with open(sample 2, 'w') as b:
        b.write(data_a)