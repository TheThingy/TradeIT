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
        self.plist.append(product)

    def remove_product(self, product):
        if product in self.plist:
            self.plist.remove(product)

    def get_list(self):
        return self.plist

