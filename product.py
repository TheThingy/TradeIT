# ! /usr/bin/env python3


class Product:
    """ Product class """

    def __init__(self, name):
        self.name = name


class ProductList:
    """ A class for managing a list of products """

    def __init__(self):
        self.plist = {}

    def add_product(self, product, amount=1):   
        if self.contains(product.name):
            amount += self.plist[product.name][1]     
        self.plist[product.name] = [product, amount]  # Every product has a counter
        return True

    def remove_product(self, product):
        if self.contains(product.name):
            del self.plist[product.name]
            return True
        
        return False

    def get_list(self):
        return self.plist
    
    def get_product(self, name):
        if self.contains(name):
            return self.plist[name][0]
        
        return False
    
    def get_product_amount(self, name):
        if self.contains(name):
            return self.plist[name][1]
        
        return False
    
    def set_product_amount(self, name, amount):
        if self.contains(name):
            self.plist["name"][1] = amount
            return True
        
        return False
    
    def contains(self, name):
        return name in self.plist  # Return True if (name in self.plist), False otherwise

