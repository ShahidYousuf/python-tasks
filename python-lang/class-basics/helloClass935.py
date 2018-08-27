class Dog:
    # class variable shared by all instances
    message = "Dog Barking"
    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)

class SubDog(Dog):
    def __init__()
if __name__ == '__main__':
    d = Dog("Fido")
    e = Dog("Buddy")
    d.add_trick("roll over")
    e.add_trick("play dead")
    print(e.tricks)
    d.add_trick("Jump Over Fence")
    print(d.tricks)
    print(d.message)
    print(e.message)



