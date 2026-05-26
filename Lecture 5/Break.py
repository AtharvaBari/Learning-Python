tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

i = 0
x = int(input("Enter a no. : "))
while i < 10:
    if (tup[i] == x):
        print("Element found at ", i)
        break
    else:
        print("Finding...")
    i += 1

print("End of loop")