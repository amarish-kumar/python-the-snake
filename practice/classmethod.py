class A:
    counter = 0
    
    def __init__(self, a, b):
        self. a = a
        self .b = b
        A.counter += 1

    @classmethod
    def clsmethod(cls):
        obj = cls(12, 13)
        print(type(obj), obj.a, obj.b)
        return obj

    def show(self):
        print "A:", self.a, ", B:",self.b

    @staticmethod
    def number_of_instances():
        return A.counter

o = A(12, 45)
o.show()

p = A.clsmethod()
print p.a

print p.number_of_instances()
print A.number_of_instances()
