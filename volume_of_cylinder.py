#!/usr/bin/env python3

# Created by Marlon Poddalgoda
# Created on November 2020
# This program calculates the volume of a cylinder
#     with user inputted radius and height

import math


def main():
    # this function calculates the volume of the cylinder
    print("Hello! Today we will be calculating the volume for a cylinder.")
    print("")

    # input
    radius = int(input("Enter the radius of the cylinder (mm): "))
    height = int(input("Enter the height of the cylinder (mm): "))

    # process
    volume = (math.pi * (radius ** 2) * height)

    # output
    print("")
    print("The volume of this cylinder is {} mm²".format(volume))


if __name__ == "__main__":
    main()
