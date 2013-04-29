#!/usr/bin/env python
#coding: utf-8

import math

def is_prime(number):
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i += 1

    return True

prime_10000 = 104729

i = prime_10000 + 1

while not is_prime(i):
    i += 1

print i