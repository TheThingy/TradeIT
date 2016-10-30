#! /usr/bin/env python3

import json

from product import Product, ProductList
from city import City, CityList
from player import Player


class Game:
    def __init__():
        self.product_list = ProductList()
        self.city_list = CityList()
        self.player = Player()
        
        # Load JSON files
        for prod in json.loads(open("products.json", 'r', encoding="utf8").read()):
            temp = Product(prod)
            product_list.add_product(temp)
        
        for cty in json.loads(open("cities.json", 'r', encoding="utf8").read()):
            temp = City(cty)
            city_list.add_city(temp)
        
    
    
    def get_input():
        return input(self.player.position + "$")
    
    def mainloop(self):
        pass




if __name__ == '__main__':
    game = Game()
    game.mainloop()
