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

# {1: [2, 3], 2: [1], 3: [1]} from users.json

# Write a Python program that reads in a JSON file containing data on a set of users,

# and outputs a dictionary containing the number of friends that each user has.


with open('users.json') as f:
    data = json.load(f)
    friends = {}
    for user in data:
        friends[user['id']] = len(user['friends'])
    print(friends)

    # Write a Python program that takes a JSON file containing data on a set of users, and creates a dictionary where each key is a user ID and each value is a list of the user's followers.


with open('users.json') as f:
    data = json.load(f)
    followers = {}
    for user in data:
        followers[user['id']] = user['followers']
    print(followers)
