# from abc import ABC, abstractmethod

# class ProductBase(ABC):
#     @abstractmethod




class Product():

    def __init__(self, name, price) -> None:
        self._name = name
        self._price = price
    
    # def get_price(self):
    #     return self._price
    
    # def set_price(self, price):
    #     self._price = price


    def special_offer():
        return f'You have been awarded a 10% discount'


    @property  #getter method  #>>gets a value for a variable
    def price(self):
        return self._price
    
    @price.setter #>>sets a value for a variable
    def price(self, price):
        self._price = price

bread = Product('Bread',65)
bread.price = 100
print(bread.price)

class Foodstuff(Product):

    def special_offer(self):
        return f'You have been awarded a 15% discount'
    
    def product_offer(self):
        super().special_offer()

milk = Foodstuff('Milk', 60)

print(milk.special_offer())
print(milk.product_offer())


# print(bread.get_price())
# print(bread.set_price(120))
# print(bread.get_price())


# Obstruction


