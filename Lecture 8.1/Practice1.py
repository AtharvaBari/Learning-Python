class students:
    def __init__(self, name, mrks):
        self.name = name
        self.mrks = mrks

    def avg1(self):
        # avg = (self.mrks[0] + self.mrks[1] + self.mrks[2]) / len(self.mrks)
        # print(avg)
        avg = 0
        for val in self.mrks:
            avg += val
        print(avg / len(self.mrks))
    
s1 = students("Karan", [10, 20, 30])
s1.avg1()
print(s1.name, s1.mrks)

s2 = students("Rohan", [50, 50, 50])
s2.avg1()
print(s2.name, s2.mrks)
