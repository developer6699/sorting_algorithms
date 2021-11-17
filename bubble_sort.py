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


# Function for bubble sort
def bubble_sort(ar, num):
    for i in range(num - 1):
        for j in range(num - 1 - i):
            if ar[j] > ar[j + 1]:
                temp = ar[j]
                ar[j] = ar[j + 1]
                ar[j + 1] = temp


bubble_sort(arr, n)
print("Bubble Sort Array: ", arr)
