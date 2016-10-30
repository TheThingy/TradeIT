#! /usr/bin/env python3

import json
import sys

from product import Product, ProductList
from city import City, CityList
from player import Player


class Game:
    def __init__(self):
        self.product_list = ProductList()
        self.city_list = CityList()
        
        # Load JSON files
        for prod in json.loads(open("data/products.json", 'r', encoding="utf8").read()):
            temp = Product(prod)
            self.product_list.add_product(temp)
        
        for cty in json.loads(open("data/cities.json", 'r', encoding="utf8").read()):
            temp = City(cty)
            self.city_list.add_city(temp)
       
        self.player = Player("Per", self.city_list.get_list()[0])
        
    
    
    def get_input(self):
        promt = str(self.player.name)
        promt += "@"
        promt += str(self.player.location.city_name)
        promt += "$ "
        return input(promt)
    
    def decode_command(self, command):
        command_list = command.split()
        
        if command_list[0] == "info":
            print("Name: %s" %(self.player.name))
            print("Money: %i" %(self.player.money))
            print("Location: %s" %(self.player.location.city_name))
        elif command_list[0] == "exit":
            print("Quitting")
            sys.exit()
        if command_list[0] == "help":
            if len(command_list) == 1:
                print("Available commands:")
                print("info")
                print("exit")
            elif len(command_list) > 1:
                if command_list[1] == "info":
                    print("Shows information about your character")
                if command_list[1] == "exit":
                    print("Exits the game")

    def mainloop(self):
        while True:
            self.decode_command(self.get_input())




if __name__ == '__main__':
    game = Game()
    game.mainloop()
