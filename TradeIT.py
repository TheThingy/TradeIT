#! /usr/bin/env python3

import json
import sys

from product import Product, ProductList
from city import City, CityList
from player import Player
from shop import Shop
import screen_objects as so
from render import View
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
        
        self.view = View()
        self.init_screen_objects()
        
    def init_screen_objects(self):
        """Create screen objects"""
        self.money_field = so.Text(0.1, 0.1, self.player.money)
        self.view.add(self.money_field)

        self.output1 = so.Text(0, 3, "", abs_pos=False, rel_corner="bottom-left")
        self.view.add(self.output1)

        self.output2 = so.Text(0, 2, "", abs_pos=False, rel_corner="bottom-left")
        self.view.add(self.output1)

        self.output3 = so.Text(0, 1, "", abs_pos=False, rel_corner="bottom-left")
        self.view.add(self.output1)
        
        self.input = so.Input(0, 0, cmd.get_prompt(self))
        self.view.add(self.input)


    
    def do_step(self):
        """Execute step operations"""
        self.step += 1
        
        # Pay for loan interest
        self.player.add_money(-self.player.loan.get_interest())
        
    def mainloop(self):
        """Start main loop"""
        while True:
            command = self.view.render()
            result = cmd.decode_command(self, command)
            self.output1.text =





if __name__ == '__main__':
    game = Game()
    game.mainloop()
