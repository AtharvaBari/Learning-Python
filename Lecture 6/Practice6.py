def prt(list, idx=0):
    if (idx == len(list)):
        return 0
    print(list[idx])
    prt(list, idx+1)

list =[1,2,3,4,5,6,7,8,9]

prt(list)