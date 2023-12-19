#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Dec. 12, 2023
# This program generates 10 random numbers then finds the min number and uses a for...each loop.

import constants
import random


def find_min_value(list):
    # declare variable
    smallest_num = 100

    # Look for smallest number
    for value in list:
        if value < smallest_num:
            smallest_num = value

    # return value
    return smallest_num


def main():
    # introduce program to user
    print("Hello, this program generates 10 random numbers then finds the min.")

    # declare list
    num_list = []

    # populate list with loop
    for counter in range(0, constants.SIZE):
        # generate random numbers 0-100
        random_number = random.randint(constants.MIN, constants.MAX)

        # populate list
        num_list.append(random_number)

    # call function
    min = find_min_value(num_list)

    # loop to display all numbers in list
    for counter_two in range(0, constants.SIZE):
        print("Added: {} ".format(num_list[counter_two]))

    # display max number
    print("The min is {}.".format(min))


if __name__ == "__main__":
    main()
