#! /usr/bin/env python3

import json

from product import Product, ProductList
from city import City, CityList
from player import Player




def main():
    product_list = ProductList()
    city_list = CityList()
    player = Player()
    
    # Load JSON files
    for prod in json.loads(open("products.json", 'r', encoding="utf8").read()):
        temp = Product(prod)
        product_list.add_product(temp)
    
    for cty in json.loads(open("cities.json", 'r', encoding="utf8").read()):
        temp = City(cty)
        city_list.add_city(temp)
    
    



if __name__ == '__main__':
    main()
