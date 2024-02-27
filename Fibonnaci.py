def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
#hello
# Example: Generate the first 10 Fibonacci numbers
n =int(input("Enter the no:"))
result = fibonacci(n)
print(f"The first {n} numbers in the Fibonacci series are: {result}")
'''
Hello
Enter the no:10
The first 10 numbers in the Fibonacci series are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
'''