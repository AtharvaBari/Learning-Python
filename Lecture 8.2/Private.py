class bank_acc:
    
    def __hello(self): # this is a private function 
        print("Hello, World")

    def hello2(self): # this is a public funtion that uses private function 
        self.__hello()


c1 = bank_acc()
c1.hello2()