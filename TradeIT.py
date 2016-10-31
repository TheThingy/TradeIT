#! /usr/bin/env python3

import json
import sys

from product import Product, ProductList
from city import City, CityList
from player import Player
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

        self.player = Player("Per", self.city_list.get_city("Tromsø"))
        
    
    def do_step(self):
        self.step += 1

    def mainloop(self):
        while True:
            cmd.decode_command(self, cmd.get_input(self))
            




if __name__ == '__main__':
    game = Game()
    game.mainloop()
