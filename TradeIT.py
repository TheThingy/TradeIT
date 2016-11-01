#! /usr/bin/env python3

import json
import sys

from product import Product, ProductList
from city import City, CityList
from player import Player
from shop import Shop
import cmd


class Game:
    def __init__(self):
        self.product_list = ProductList()
        self.city_list = CityList()
        self.step = 0
        
        # Load JSON files
        for prod in json.loads(open("data/products.json", 'r', encoding="utf8").read()):
            temp = Product(prod)
            self.product_list.add_product(temp)

        for cty in json.loads(open("data/cities.json", 'r', encoding="utf8").read()):
            temp = City(cty)
            self.city_list.add_city(temp)
        
        ## TODO: add shops

        self.player = Player("Per", self.city_list.get_city("Tromsø"))
        self.player.set_money(20000)
        self.player.loan.set_loan(80000)
        
    
    def do_step(self):
        self.step += 1
        
        # Pay for loan interest
        self.player.add_money(-self.player.loan.get_interest())
        
        

    def mainloop(self):
        while True:
            cmd.decode_command(self, cmd.get_input(self))
            




if __name__ == '__main__':
    game = Game()
    game.mainloop()
