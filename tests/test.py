class Test1:
    var1 = 'class var'

    def test1(self):
        var2 = 'inside var'
        self.var3 = 'instance var'

print(Test1.var3)

print(Test1().var3)