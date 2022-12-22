#!/usr/bin/env python3

# Created By: Spencer Scarlett
# Date: Dec 21, 2022
# A program which uses lists to generate 10 numbers
# with a range of 1/100 and find the lowest value

import random


def find_min_value(random_list):

    find_min = random_list[0]

    # calculate the min value
    for i in random_list:
        if find_min > i:
            find_min = i
    # return cmd
    return find_min


def main():
    # intro message
    print(
        "This is a program that generates 10 random numbers"
        " and finds the lowest value out of them"
    )
    print("")

    # declaring variable
    rand_num_list = []

    for i in range(10):
        # generates 10 random numbers from 1, 100
        rand_num = random.randint(1, 100)
        # displays what number was created and where
        print(f"{rand_num} added to the list and in element {i}")
        # appends them to a list
        rand_num_list.append(rand_num)

    # calls the above function
    min_number = find_min_value(rand_num_list)
    print("")
    # displays output message
    print(f"The lowest value of {rand_num_list} is {min_number}")


if __name__ == "__main__":
    main()
