# pre-defined code start

#!/bin/python3
import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
# pre-defined code end

# TASK:
# Given an integer, n, perform the following conditional actions:
# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

# first we check if the number n is even or odd
if n % 2 == 1:
  print("Weird")
# then we proceed to check the conditions
elif 2<= n <=5:
  print("Not Weird")
elif 6<= n <=20:
  print("Weird")
else:
  print("Not Weird")

# ALTERNATE WORKAROUND for cleaner thinking.

n = int(input())
if (n % 2 == 1) or (6 <= n <= 20):
    print("Weird")
else:
    print("Not Weird")
