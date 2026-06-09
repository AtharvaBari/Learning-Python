word = "alearning"
with open("/Users/atharvabari/Main/Code/Learning-Python/Lecture 7/practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")