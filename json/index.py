# Write a Python program that reads in a JSON file containing data on a set of customers, 
# and outputs a list of all the unique countries that the customers are from.

import json

with open('customers.json') as f:
    data = json.load(f)
    countries = []
    for customer in data:
        countries.append(customer['country'])
    print(set(countries))

# Write a Python program that takes a JSON file containing data on a set of products,
#  and outputs the name and price of the most expensive product.


with open('products.json') as f:
    data = json.load(f)
    max_price = 0
    for product in data:
        if product['price'] > max_price:
            max_price = product['price']
            max_product = product
    print(max_product['name'], max_product['price'])