class Cart():

    ITEMS = []
    def __init__(self, name) -> None:
        self.name = name

    def add_to_cart(self,item):
        if not isinstance(item, Product):
            raise TypeError('Item must be a product')
        Cart.ITEMS.append(item)    


    def find_specific_product(self,name):
        product = [item for item in Cart.ITEMS if item.name == name]

        if product:
            return f'You have purchased{product.quantity} {product.name} at {product.price}'
        else:
            raise Exception('The product does not exist in the cart')


    def total_price(self):
        return reduce(lambda sum,pd:sum+pd.price, Cart.ITEMS)

class Product():
    def __init__(self, name, price, quantity) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity


    def __repr__(self) -> str:
        return f'<Product: {self.name}:{self.price}'

bread_lovers_cart = Cart('Bread Lover')

bread = Product('Bread',65,3)
milk = Product('Milk',60,7)

bread_lovers_cart.add_to_cart(bread)
bread_lovers_cart.add_to_cart(milk)
print(bread_lovers_cart.find_specific_product('Bread'))
print(bread_lovers_cart.find_specific_product('milk'))

print(Cart.ITEMS)

