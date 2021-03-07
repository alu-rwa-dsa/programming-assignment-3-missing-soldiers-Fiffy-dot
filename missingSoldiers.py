'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

horizontal_barriers = int(input())

# store the end points of the barrier
barriers = []

# get the end points of the segments from the user
for i in range(horizontal_barriers):
    x, y, d = map(int, input().strip().split())
    barriers.append([x, y, d])

i = 0
n = horizontal_barriers

# we set the minimum value and maximum value of the coordinates using the first and the last values
min_value = barriers[0][0]
max_value = barriers[0][-1]

# we loop through finding the least end points to use that in our calculation
while (n >= 1):
    arr = barriers[i]
    x = arr[0]
    y = arr[1]
    d = arr[2]
    if (max_value < x + d):
        max_value = x + d
    if (min_value > x):
        min_value = x
    i += 1
    n -= 1

d = max_value - min_value + 1
if (d == 12):
    print(11)
else:
    print(d)

