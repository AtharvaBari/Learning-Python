class acc:

    def __init__(self, acc, bal):
        self.acc = acc
        self.bal = bal

    def debit(self, amt):
        self.bal -= amt
        print(f"A Amount of {amt} was debited from your account.")
        print("Current Bal: ", self.balance())

    def credit(self, amt):
        self.bal += amt
        print(f"A Amount of {amt} was credited to your account.")
        print("Current Bal: ", self.balance())

    def balance(self):
        return self.bal



c1 = acc(1234512345, 10000)
c1.debit(5000)
c1.credit(50000)
c1.debit(15000)
c1.debit(-5000) #flaw!




        