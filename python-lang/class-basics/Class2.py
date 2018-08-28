class Person:
    # all persons, shared by all instances -- class variable
    all_persons = []
    def __init__(self, name='', job=None, pay=0, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.job = job
        self.pay = pay
        Person.all_persons.append(self)
    def giveRaise(self):
        print("Giving Raise to Employee")
    def __str__(self):
        return self.name + " " + str(self.job) + " " + str(self.pay)

class Manager(Person):
    def __init__(self, name='', pay=0, phone='', **kwargs):
        super().__init__(name, job="Manager", pay=pay, **kwargs)
        self.phone = phone
    def giveRaise(self):
        print("Giving Raise to Engineer")
    def __str__(self):
        return super().__str__() + " " + str(self.phone)

if __name__ == "__main__":
    e = Person("Bob", "Assistant", 10000)
    f = Person("Jack")
    g = Person("Greg", job="Developer", pay=30000)
    m = Manager("Smith",20000,123456789)
    print(e)
    print(f)
    print(g)
    print(m)
    print(m.phone)
    print()
    for person in Person.all_persons:
        print(person)


