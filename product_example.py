#! /usr/bin/env python3

import product

product_list = product.ProductList()

for product_name in ["product1", "product2", "product3", "product4"]:
    temp_product = product.Product(product_name)
    
    product_list.add_product(temp_product)



for prd in product_list.get_list():
    print(prd.name)

