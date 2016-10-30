# ! /usr/bin/env python3

import product

class Player:
    def __init__(self):
        self.position = None
        self.money = 0
        self.inventory = product.ProductList()
