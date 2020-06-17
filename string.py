#!/bin/python3

import math
import os
import random
import re
import sys


class Car :
    def __init__(self, max_speed, speed_notation) :
        self.max_speed = max_speed
        self.speed_notation = speed_notation


class Boat :
    def __init__(self, max_speed) :
        self.max_speed = max_speed


car = Car(151, 'km/h')
print("Car with the maximum speed of " + str(car.max_speed) + ' ' + car.speed_notation)
boat = Boat(77)
print("Boat with the maximum speed of " + str(boat.max_speed) + " knots")

