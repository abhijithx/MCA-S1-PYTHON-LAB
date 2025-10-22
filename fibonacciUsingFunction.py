def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Example usage
num = int(input("Enter the number of Fibonacci terms: "))
print("Fibonacci series:", fibonacci(num))
