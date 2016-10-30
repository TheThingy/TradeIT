#! /usr/bin/env python3

import json

import product
import city





def main():
    product_list = product.ProductList()
    city_list = city.CityList()
    
    # Load JSON files
    for prod in json.loads(open("products.json", 'r', encoding="utf8").read()):
        temp = product.Product(prod)
        product_list.add_product(temp)
    
    for cty in json.loads(open("cities.json", 'r', encoding="utf8").read()):
        temp = city.City(cty)
        city_list.add_city(temp)
    



if __name__ == '__main__':
    main()
