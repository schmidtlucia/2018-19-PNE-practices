#Exercise 5 of session 1

def fibonacci():
    n = int(input('Enter the n-th fibonacci number to calculate: '))
    a, b = 0, 1
    num = 2
    condition = True
    if n == 0:
        print('0')
        condition = False
    elif n == 1:
        print('1')
        condition = False
    while condition:
        a, b = b, a + b
        num += 1
        if num == n:
            print(b)

fibonacci()
