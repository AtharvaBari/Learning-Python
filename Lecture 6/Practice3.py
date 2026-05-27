def take_input():
    x = int(input("Enter a no.: "))
    return x

def fact(x):
    a = 1
    for i in range(1, x+1):
        a *= i
    print(a)

x = take_input()
fact(x)