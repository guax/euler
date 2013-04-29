#!/usr/bin/env python
#coding: utf-8

size = 100

sum_of_squares = sum([x*x for x in range(0, size+1)])
square_of_sum = sum(range(0, size+1)) ** 2

print abs(sum_of_squares - square_of_sum)
