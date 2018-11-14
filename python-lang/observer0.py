class Inventory:
    def __init__(self):
        self.observers = []
        self._product = None
        self._quantity = 0

    def attach(self, observer):
        self.observers.append(observer)

    @property
    def product(self):
        return self._product
    @product.setter
    def product(self, value):
        self._product = value
        self._update_observers()
        
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, value):
        self._quantity = value
        self._update_observers()

    def _update_observers(self):
        for observer in self.observers:
            observer()

def observer1():
    print("observer1 is called")
def observer2():
    print("observer2 is called")
if __name__ == '__main__':
    i = Inventory()
    i.attach(observer1)
    i.product = "computers"
    i.quantity = 10
    j = Inventory()
    j.attach(observer2)
    j.product = "routers"
    j.quantity = 34
    print(i.product)
    print(i.quantity)
    print(j.product)
    print(j.quantity)
    
    
