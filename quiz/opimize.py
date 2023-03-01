# # problem
# print('Good morning!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good afternoon!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')
# print('Good evening!')
# print('How are you feeling?')
# feeling = input()
# print('I am happy to hear that you are feeling ' + feeling + '.')

import random

def greet(time, feeling):
    print('Good ' + time + '!')
    print('How are you feeling?')
    print('I am happy to hear that you are feeling ' + feeling + '.')

# use loop
for time in ['morning', 'afternoon', 'evening']:
    greet(time, random.choice(['great', 'good', 'okay']))

    

