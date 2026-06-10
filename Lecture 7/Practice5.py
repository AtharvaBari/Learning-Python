with open("/Users/atharvabari/Main/Code/Learning-Python/Lecture 7/no.txt", "r") as f:
    data = f.read()
    print(data)


    num = ""
    for i in range (len(data)):
        if (data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
