# generate random integer values
from random import seed
from random import randint
import random

# seed random number generator
seed(1)

arr = []

# User input for number of elements
n = int(input("Enter number of elements: "))

# For random input
for _ in range(n):
    arr.append(randint(0, n))

print("Unsorted Array", arr)


# Function for insertion sort
def insertion_sort(a, num):
    for i in range(1, n):
        temp = a[i]
        for j in reversed(range(0, i)):
            if temp < a[j]:
                a[j+1] = a[j]
                a[j] = temp
    print("Insertion Sort Array: ", a)


insertion_sort(arr, n)
