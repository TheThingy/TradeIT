# ! /usr/bin/env python3


class Product:
    """ Product class """

    def __init__(self, name):
        self.name = name


class ProductList:
    """ A class for managing a list of products """

    def __init__(self):
        self.plist = []

    def add_product(self, product):
        if self.contains(product.name):
            return False
        
        self.plist.append(product)
        return True

    def remove_product(self, product):
        if product in self.plist:
            self.plist.remove(product)
            return True
        
        return False

    def get_list(self):
        return self.plist
    
    def get_product(self, name):
        return self.contains(name):
    
    def contains(self, name):
        for product in self.plist:
            if name == product.name:
                return product
        
        return False

