try:
    Read = open("first.txt", "r")
    r1 = Read.readlines()
    Write = open("Second.txt", "w")
    Write.writelines(r1)
    Write.close()
    ReadWrite = open("Second.txt", "r")
    for i in ReadWrite:
        print(i)
    #print(ReadWrite.readlines())
except FileNotFoundError:
    print("Error: File not found")



