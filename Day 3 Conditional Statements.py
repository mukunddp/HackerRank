#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if (N % 2) == 1 :
        print("Weird")
    if ((N%2)==0 and (1<N<5)):
        print("Not Weird")
    if ((N%2)==0 and (5<N<21)):
        print("Weird")
    if ((N%2)==0 and (20<N)):
        print("Not Weird")
