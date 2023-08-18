#!/usr/bin/env python3

def print_fibonacci(length):
    fib_sequence = [0, 1]  # Initialize the first two numbers of the Fibonacci sequence
    
    while len(fib_sequence) < length:
        next_number = fib_sequence[-1] + fib_sequence[-2]  # Calculate the next Fibonacci number
        fib_sequence.append(next_number)  # Add the next number to the sequence
    
    print(fib_sequence)

# Example usage
print_fibonacci(10)  # Print the first 10 Fibonacci numbers
