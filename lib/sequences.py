#!/usr/bin/env python3

def print_fibonacci(length):
    a, b = 0, 1
    count = 0

    while count < length:
        print(a, end=" ")
        a, b = b, a + b
        count += 1


# Call the function with the desired length
length = 10  # Set the desired length here
print_fibonacci(length)
