"""

Two words are anagrams of one another if their letters can be rearranged to form the other word.

Given a string, split it into two contiguous substrings of equal length. Determine the minimum number of characters to change to make the two substrings into anagrams of one another.

Example

Break  into two parts: 'abc' and 'cde'. Note that all letters have been used, the substrings are contiguous and their lengths are equal. Now you can change 'a' and 'b' in the first substring to 'd' and 'e' to have 'dec' and 'cde' which are anagrams. Two changes were necessary.

Function Description

Complete the anagram function in the editor below.

anagram has the following parameter(s):

string s: a string
Returns

int: the minimum number of characters to change or -1.
Input Format

The first line will contain an integer, , the number of test cases.
Each test case will contain a string .

Constraints


 consists only of characters in the range ascii[a-z].
Sample Input

6
aaabbb
ab
abc
mnop
xyyx
xaxbbbxx
Sample Output

3
1
-1
2
0
1
Explanation

Test Case #01: We split  into two strings ='aaa' and ='bbb'. We have to replace all three characters from the first string with 'b' to make the strings anagrams.

Test Case #02: You have to replace 'a' with 'b', which will generate "bb".

Test Case #03: It is not possible for two strings of unequal length to be anagrams of one another.

Test Case #04: We have to replace both the characters of first string ("mn") to make it an anagram of the other one.

Test Case #05:  and  are already anagrams of one another.

Test Case #06: Here S1 = "xaxb" and S2 = "bbxx". You must replace 'a' from S1 with 'b' so that S1 = "xbxb".

"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def anagram(s):
    length = len(s)

    # If the length of the string is odd, it's not possible to split it into two equal substrings
    if length % 2 != 0:
        return -1

    # Split the string into two equal parts
    mid = length // 2
    s1 = s[:mid]
    s2 = s[mid:]

    # Count the occurrences of each character in both substrings
    count_s1 = [0] * 26
    count_s2 = [0] * 26

    for char in s1:
        count_s1[ord(char) - ord('a')] += 1

    for char in s2:
        count_s2[ord(char) - ord('a')] += 1

    # Calculate the minimum number of changes needed to make the two substrings anagrams
    changes_needed = 0
    for i in range(26):
        changes_needed += abs(count_s1[i] - count_s2[i])

    # Return the result
    return changes_needed // 2  # Divide by 2 because each change affects two characters

# Test cases
test_cases = int(input())
for _ in range(test_cases):
    s = input()
    result = anagram(s)
    print(result)

