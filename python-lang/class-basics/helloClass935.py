class Dog:
    # class variable shared by all instances
    message = "Dog Barking"
    def __init__(self, name='', **kwargs):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)

class SubDog(Dog):
    def __init__(self,name='', title='', **kwargs):
        if kwargs:
            print(kwargs)
        super().__init__(name, **kwargs)
        self.title = title

if __name__ == '__main__':
    d = Dog("Fido")
    e = Dog("Buddy")
    d.add_trick("roll over")
    e.add_trick("play dead")
    print(e.tricks)
    d.add_trick("Jump Over Fence")
    print(d.tricks)
    s = SubDog("SubDog Name", "SubDog Title")
    print(s.name)
    print(s.title)
    s1 = SubDog()
    print(s1.name)
    print(s1.name)
    s2 = SubDog("S2 Name", "S2 Title", p1="param1", p2="param2")
    print(s2.name)
    print(s2.title)





