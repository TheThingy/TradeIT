# ! /usr/bin/env python3


class Product:
    """ Product class """

    def __init__(self, name):
        self.name = name


class ProductList:
    """ A class for managing a list of products """

    def __init__(self):
        self.plist = {}

    def add_product(self, product):
        if self.contains(product.name):
            return False
        
        self.plist[product.name] = product
        return True

    def remove_product(self, product):
        if self.contains(product.name):
            del self.plist[product.name]
            return True
        
        return False

    def get_list(self):
        return self.plist
    
    def get_product(self, name):
        return self.plist[name]
    
    def contains(self, name):
        return name in self.plist # Return True if (name in self.plist), False otherwise

