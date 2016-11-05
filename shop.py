#! /usr/bin/env python3

from product import ProductList
from player import Player


class ShopList(ProductList):
    """A class used for containing a list of Shops"""
    def __init__(self):
        super().__init__() # not sure if ".__init__()" is needed
        
    def add_product(self, product, amount=1, price=0):   
        if self.contains(product.name):
            amount += self.plist[product.name][1]     
        self.plist[product.name] = [product, amount, price]  # Every product has a counter
        return True
    
    def get_product_price(self, name):
        if self.contains(name):
            return self.plist[name][2]
        return False

    def set_product_amount(self, name, price):
        if self.contains(name):
            self.plist["name"][2] = price
            return True
        return False

class Shop(Player): # class Shop extends class Player
    """A class used for a shop, extends Player."""
    def __init__(self, city):
        super().__init__("shop", city)
        
        self.inventory = ShopList()
        
