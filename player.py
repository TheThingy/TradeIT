# ! /usr/bin/env python3

import product
import economy


class Player:
    """A player class containing relevant attributes and methods"""
    def __init__(self, name, city, money=0):
        self.name = name
        self.location = city
        self.money = money
        self.inventory = product.ProductList()
        self.loan = economy.Loan(0, 0.05)

    def get_location(self):
        return self.location

    def set_location(self, location):
        self.location = location

    def get_inventory(self):
        return self.inventory

    def get_money(self):
        return self.money

    def set_money(self, amount):
        self.money = amount
    
    def add_money(self, amount):
        self.money += amount

    def add_product(self, prod, amount):
        self.inventory.add_product(prod, amount)

    def remove_product(self, prod, amount):
        amount = self.inventory.get_product_amount(prod.name) - amount
        self.inventory.set_product_amount(prod.name, amount)

