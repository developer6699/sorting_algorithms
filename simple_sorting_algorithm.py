# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed(1)

arr = []

# User input for number of elements
n = int(input("Enter number of elements: "))

# Inputting values in array through user
'''
# For user input
while n!=0:
    arr.append(int(input("Enter elements: ")))
    n-=1
'''

# For random input
for _ in range(n):
    arr.append(randint(0, n))

# Unsorted Array
print("Unsorted Array: ", arr)

# Sorting Array in Ascending Order
for i in range(0, n):
    j = i+1
    for j in range(0, n):
        if arr[j] > arr[i]:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

print("Sorted Array: ", arr)