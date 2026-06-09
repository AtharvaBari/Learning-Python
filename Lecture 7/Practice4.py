word = "learning"

with open("/Users/atharvabari/Main/Code/Learning-Python/Lecture 7/practice.txt", "r") as f:
    data = f.read()
    if (word in data):
        print("Found")
    else:
        print("Not Found")

def check_line():
    word = "learning"
    data = True 
    line = 1
    with open("/Users/atharvabari/Main/Code/Learning-Python/Lecture 7/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if (word in data):
                print("Found at line", line)
        line += 1
    return -1

print(check_line())