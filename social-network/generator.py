import os
import random
import requests


def read_name(filepath):
    with open(filepath, "r") as file:
        return [line.strip() for line in file]


dp = "lists/"

first_name_filepath = os.path.join(dp, "boy-names.txt")
last_name_filepath = os.path.join(dp, "surname-list.txt")

first_names = read_name(first_name_filepath)
last_names = read_name(last_name_filepath)

num = 0
while num < 19:
    print(random.choice(first_names), random.choice(last_names))
    num = num + 1
