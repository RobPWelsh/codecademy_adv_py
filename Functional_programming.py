from collections import namedtuple
from functools import reduce
import csv
import json


# # Immutable Data types
# country = namedtuple('country', ['name', 'capital', 'continent'])
#
# France = country('France', 'Paris', 'Europe')
# Japan = country('Japan', 'Tokyo', 'Asia')
# Senegal = country('Senegal', 'Dakar', 'Africa')
#
# countries = (France, Japan, Senegal)
#
# # ________________________________________________________
# # Review of Lambda Functions
# """
# def squared(x):
#   return x * x
#
# def cubed(x):
#   return x*x*x
# """
#
#
# def odd_or_even(n, even_function, odd_function):
#     if n % 2 == 0:
#         return even_function(n)
#     return odd_function(n)
#
#
# # Checkpoint 2 code goes here.
# square = lambda x: x ** 2
# cube = lambda x: x ** 3
#
# # Checkpoint 3 code goes here.
# test = odd_or_even(5, cube, square)
#
# print(test)  # 25
#
# # ________________________________________________________
# # Review of filter(), map(), and reduce()
# nums = (16, 2, 19, 22, 10, 23, 16, 2, 27, 29, 19, 26, 12, 20, 16, 29, 6, 2, 12, 20)
#
# # Checkpoint 1 code goes here.
# filtered_numbers = filter(lambda x: x % 2 == 0, nums)
# print(tuple(filtered_numbers))  # tuple of even nums
#
# # Checkpoint 2 code goes here.
# mapped_numbers = map(lambda x: x * 3, nums)
# print(tuple(mapped_numbers))  # tuple of nums multiplied by 3
#
# # Checkpoint 3 code goes here.
# sum = reduce(lambda x, y: x + y, nums)
# print(sum)  # 328
#
# # ________________________________________________________
# # Mapping a Filtered Collection
# nums = (2, 12, 5, 8, 9, 3, 16, 7, 13, 19, 21, 1, 15, 4, 22, 20, 11)
#
# # multiply values greater than 10 by 2
# greater_than_10_doubled = map(lambda x: x * 2, filter(lambda num: num > 10, nums))
# print(tuple(greater_than_10_doubled))  # (24, 32, 26, 38, 42, 30, 44, 40, 22)
#
# """
# Convert the following code from the imperative style to the declarative
# lst = []
# for i in nums:
#   if i % 3 == 0:
#     lst.append(i)
#
# for i in range(len(lst)):
#   lst[i] = lst[i] * 3
#
# tuple(lst)
#
# Here, nums represents the tuple provided in the workspace.
#
# Save your result in a variable called functional_way. Print your answer using the following line of code:
#
# print(tuple(functional_way))
# """
# functional_way = map(lambda x: x * 3, filter(lambda num: num % 3 == 0, nums))
# print(tuple(functional_way))  # (36, 27, 9, 63, 45)
#
# # ________________________________________________________
# # Reducing a Filtered Collection
# # Prices are in USD
# menu_item = namedtuple("menu_item", ["name", "dish_type", "price"])
#
# jsp = menu_item("Jumbo Shrimp Platter", "Appetizer", 29.95)
# lc = menu_item("Lobster Cake", "Appetizer", 30.95)
# scb = menu_item("Sizzling Canadian Bacon", "Appetizer", 9.95)
# ccc = menu_item("Codecademy Crab Cake", "Appetizer", 32.95)
# cs = menu_item("Caeser Salad", "Salad", 14.95)
# mgs = menu_item("Mixed Green Salad", "Salad", 10.95)
# cp = menu_item("Codecademy Potatoes", "Side", 34.95)
# mp = menu_item("Mashed Potatoes", "Side", 14.95)
# a = menu_item("Asparagus", "Side", 15.95)
# rs = menu_item("Ribeye Steak", "Entree", 75.95)
# phs = menu_item("Porter House Steak", "Entree", 131.95)
# grs = menu_item("Grilled Salmon", "Entree", 36.95)
#
# menu = (jsp, lc, scb, ccc, cs, mgs, cp, mp, a, rs, phs, grs)
# entree = 0
# least_expensive = 0
#
# # Code for Checkpoint 1 goes here.
# entree = reduce(lambda x, y: x if x.price > y.price else y, filter(lambda x: x.dish_type == 'Entree', menu))
# print(entree)  # menu_item(name='Porter House Steak', dish_type='Entree', price=131.95)
#
# # Code for Checkpoint 2 goes here.
# least_expensive = reduce(lambda x, y: x if x.price < y.price else y, filter(lambda x: x.dish_type == 'Side' or x.dish_type == 'Salad', menu))
#
# print(least_expensive)  # menu_item(name='Mixed Green Salad', dish_type='Salad', price=10.95)
#
# # ________________________________________________________
# # Reducing a Mapped Collection
# fruits = {"Grape":(4, 6, 2), "Lemon":(7, 3, 1), "Orange":(5, 8, 1), "Apple":(2, 8, 10), "Watermelon":(0, 9, 6)}
#
# total_fruits = reduce(lambda a, b: a + b, map(lambda c: fruits[c][0] + fruits[c][1] + fruits[c][2], fruits))
# print(total_fruits)  # 72
#
# # ________________________________________________________
# # Combining all Three Higher-Order Functions
# costs = {"shirt": (4, 13.00), "shoes":(2, 80.00), "pants":(3, 100.00), "socks":(5, 5.00), "ties":(3, 14.00), "watch":(1, 145.00)}
#
# nums = (24, 6, 7, 16, 8, 2, 3, 11, 21, 20, 22, 23, 19, 12, 1, 4, 17, 9, 25, 15)
#
# # Code for Checkpoint 1 goes here.
# total = reduce(lambda a, b: a + b, filter(lambda c: c > 150, map(lambda d: costs[d][0] * costs[d][1], costs)))
#
# print(total)  # 460
#
# product = -1
#
# # Code for Checkpoint 2 goes here.
# product = reduce(lambda a, b: a * b, map(lambda c: c + 5, filter(lambda d: d < 10, nums)))
#
# print(product)  # 72648576
#
# # ________________________________________________________
# # Importing Data From a CSV File
# # Code for Checkpoint 1 goes here.
#
# tree = namedtuple('tree', ['index', 'width', 'height', 'volume'])
#
# with open('trees.csv', newline='') as csvfile:
#     reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#     next(reader)  # Skip the first line in trees.csv that contains the data labels.
#
#     mapper = map(lambda x: tree(int(x[0]), float(x[1]), int(x[2]), float(x[3])), reader)
#
#     t = filter(lambda y: y[2] > 75, mapper)
#
#     trees = tuple(t)
#     print(trees)  # tuple of trees with height greater than 75
#
#     widest = reduce(lambda x, y: x if x.width > y.width else y, trees)
#     print(widest)  # tree(index=31, width=20.6, height=87, volume=77.0)
#
# # _____________________________________________________________________
# # Processing Data From a JSON File
# city = namedtuple("city", ["name", "country", "coordinates", "continent"])
#
# with open('cities.json') as json_file:
#   data = json.load(json_file)
#
# cities = map(lambda x: city(x["name"], x["country"], x["coordinates"], x["continent"]), data["city"])
#
# # Code for Checkpoint 1 goes here.
# asia = tuple(filter(lambda x: x[3] == 'Asia', cities))
# print(asia)  # tuple of cities on the continent of Asia
#
# west = None
#
# # Code for Checkpoint 2 goes here.
# west = reduce(lambda x, y: x if x.coordinates[1] < y.coordinates[1] else y, asia)
# print(west)  # city(name='Beirut', country='Lebanon', coordinates=[33.8938, 35.5018], continent='Asia')

# ____________________________________________________________________________________
# Project - Create your own Higher Order Functions

def count(predicate, itr):
    count_filter = filter(predicate, itr)
    count_reduce = reduce(lambda x, y: x + 1, count_filter, 0)
    return count_reduce


def average(itr):
    # If itr is not iterable, this will generate an iterator.
    iterable = iter(itr)
    return avg_helper(0, iterable, 0)


def avg_helper(curr_count, itr, curr_sum):
    next_num = next(itr, 'null')
    if next_num == 'null':
        return curr_sum / curr_count
    curr_count += 1
    curr_sum += next_num
    return avg_helper(curr_count, itr, curr_sum)


with open('1kSalesRec.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    fields = next(reader)
    count_belgiums = count(lambda x: x[1] == 'Belgium', reader)
    print(count_belgiums)
    csvfile.seek(0)
    avg_portugal = average(map(lambda y: float(y[13]), filter(lambda x: x[1] == 'Portugal', reader)))
    print(avg_portugal)

