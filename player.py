# ! /usr/bin/env python3

import product

class Player:
    def __init__(self, name, city):
        self.name = name
        self.location = city
        self.money = 0
        self.inventory = product.ProductList()
        self.loan = 0

    def get_position(self):
        return self.location

    def set_position(self, location):
        self.location = location

    def get_inventory(self):
        return self.inventory

    def set_inventory(self, inventory):
        self.inventory = inventory

    def get_loan(self):
        return self.loan

    def set_loan(self, loan):
        self.loan = loan
