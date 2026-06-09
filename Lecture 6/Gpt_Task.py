def prt(n):
    if (n == 0):
        return 0
    prt(n-1)
    print(n)

prt(10)