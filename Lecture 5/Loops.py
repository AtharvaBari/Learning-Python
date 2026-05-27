i = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 9
for el in i:
    if (el == x):
        print(el, "found")
        # break
    print(el)
    el += 1
    continue
else: 
    print("End of Program")