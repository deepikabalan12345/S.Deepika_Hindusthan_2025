"""
Given a time in -hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example


Return '12:01:00'.


Return '00:01:00'.

Function Description

Complete the timeConversion function in the editor below. It should return a new string representing the input time in 24 hour format.

timeConversion has the following parameter(s):

string s: a time in  hour format
Returns

string: the time in  hour format
Input Format

A single string  that represents a time in -hour clock format (i.e.:  or ).

Constraints

All input times are valid
Sample Input 0

07:05:45PM
Sample Output 0

19:05:45

"""
def timeConversion(s):
    # Extract hours, minutes, and seconds
    hh, mm, ss = map(int, s[:-2].split(':'))
    # Check if it's PM and not 12:00:00PM
    if 'PM' in s and hh != 12:
        hh += 12
    # Check if it's AM and 12:00:00AM
    elif 'AM' in s and hh == 12:
        hh = 0
    # Format the result as a 24-hour time string
    result = "{:02d}:{:02d}:{:02d}".format(hh, mm, ss)
    return result

# Sample Input
input_time = "07:05:45PM"
# Sample Output
output_time = timeConversion(input_time)
print(output_time)


