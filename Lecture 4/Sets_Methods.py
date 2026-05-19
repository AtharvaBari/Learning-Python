set1 = set()

set1.add(2)
set1.add(1)
set1.add(3)
set1.add(2)
set1.add((5,6,7,7))
set1.add((5,6,7))
# set1.add([5,6,7,7]) # This is a list that is mutable 

set1.remove(3)
# set1.remove(6) # element does not exist

print(set1)
print(len(set1))

set1.pop()
print(set1)
print(len(set1))

set1.clear()
print(len(set1))

