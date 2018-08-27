class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def giveRaise(self):
        print("Giving Raise to Employee")
    def __str__(self):
        return self.name + " " + str(self.job) + " " + str(self.pay)

class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'Manager', pay)
    def giveRaise(self):
        print("Giving Raise to Engineer")

if __name__ == "__main__":
    e = Person("Bob", "Assistant", 10000)
    f = Person("Jack")
    g = Person("Greg", job="Developer", pay=30000)
    m = Manager("Smith", 20000)
    print(e)
    print(f)
    print(g)
    print(m)
