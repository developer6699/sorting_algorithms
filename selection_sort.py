# generate random integer values
from random import seed
from random import randint

# seed random number generator
seed(1)

arr = []

# User input for number of elements
n = int(input("Enter number of elements: "))
'''
# Inputting values in array through user

# For user input
while n!=0:
    arr.append(int(input("Enter elements: ")))
    n-=1
'''

# For random input
for _ in range(n):
    arr.append(randint(0, n))

print(arr)


def selection_sort(a, num):
    for i in range(num-1):
        min_pos = i
        for j in range(i, n):
            if a[j] < a[min_pos]:
                min_pos = j
        if min_pos != i:
            temp = a[i]
            a[i] = a[min_pos]
            a[min_pos] = temp


selection_sort(arr, n)
print(arr)
