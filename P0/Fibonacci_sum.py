#Exercise 6 of session 1

def fibonacci2(n):
    from math import sqrt
    sol = (((1 + sqrt(5))**(n-1)) - (1 - sqrt(5))**(n-1)) / ((2**(n-1))*sqrt(5))
    return (int(sol))

def fibonacci_sum():
    n = int(input('Enter the number n for the summation from the first number of the Fibonacci serie until the n-th one: '))
    num = 0
    for b in range(n):
        sol = fibonacci2(n-n+(b+1))
        num += sol
    print(num)


fibonacci_sum()

