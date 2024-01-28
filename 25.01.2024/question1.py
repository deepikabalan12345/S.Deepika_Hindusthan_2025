"""

Consider two points,  and . We consider the inversion or point reflection, , of point  across point  to be a  rotation of point  around .

Given  sets of points  and , find  for each pair of points and print two space-separated integers denoting the respective values of  and  on a new line.

Function Description

Complete the findPoint function in the editor below.

findPoint has the following parameters:

int px, py, qx, qy: x and y coordinates for points  and 
Returns

int[2]: x and y coordinates of the reflected point 
Input Format

The first line contains an integer, , denoting the number of sets of points.
Each of the  subsequent lines contains four space-separated integers that describe the respective values of , , , and  defining points  and .

Constraints

Sample Input

2
0 0 1 1
1 1 2 2
Sample Output

2 2
3 3

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'findPoint' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER px
#  2. INTEGER py
#  3. INTEGER qx
#  4. INTEGER qy
#

def findPoint(px, py, qx, qy):
    # Calculate the coordinates of the reflected point
    rx = 2 * qx - px
    ry = 2 * qy - py

    return [rx, ry]

# Read the number of sets of points
n = int(input().strip())

# Iterate through each set of points
for _ in range(n):
    # Read the coordinates of points px, py, qx, qy
    px, py, qx, qy = map(int, input().split())

    # Find the reflected point and print the result
    result = findPoint(px, py, qx, qy)
    print(*result)












