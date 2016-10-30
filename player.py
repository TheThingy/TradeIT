# ! /usr/bin/env python3

import product

class Player:
    def __init__(self, name, city):
        self.name = name
        self.location = city
        self.money = 0
        self.inventory = product.ProductList()
        self.loan = 0

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_inventory(self):
        return self.inventory

    def get_loan(self):
        return self.loan

    def set_loan(self, loan):
        self.loan = loan

    def add_prod(self, amount, product):
        self.add_prod = self.add_product(product, amount)

    def remove_prod(self, amount):