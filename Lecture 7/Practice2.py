with open("/Users/atharvabari/Main/Code/Learning-Python/Lecture 7/practice.txt", "r") as f:
    data = f.read()

    new_data = data.replace("Java", "Python")
    print(new_data)