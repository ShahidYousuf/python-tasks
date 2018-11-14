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

class Observer1:
    def __init__(self, inventory):
        self.inventory = inventory
    # this is important, you need to define the __call__ method
    def __call__(self):
        print("Observer1")
        print("Product ", self.inventory.product, "Quantity ", self.inventory.quantity)
class Observer2:
    def __init__(self, inventory):
        self.inventory = inventory

    def __call__(self):
        print("Observer2")
        print("Product ", self.inventory.product, "Quantity ", self.inventory.quantity)

if __name__ == '__main__':
    
    #i = Inventory()
    #i.attach(observer1)
    #i.product = "computers"
    #i.quantity = 10
    
    k = Inventory()
    o1 = Observer1(k)
    o2 = Observer2(k)
    k.attach(o1)
    k.attach(o2)
    k.product = "classic computers"
    k.quantity = 23

    print("#"*40)
    print("Currently registered observers")
    print("#"*40)
    for item in k.observers:
        print(item.__class__.__name__ , end=' ')

    
    
