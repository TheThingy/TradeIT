# ! /usr/bin/env python3

import product

class Player:
    def __init__(self, name, city):
        self.name = name
        self.location = city
        self.money = 0
        self.inventory = product.ProductList()
        self.loan = 0
