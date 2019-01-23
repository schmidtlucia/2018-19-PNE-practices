#Exercise 4 of session 1

def sum(n):
    total = 0
    for i in range (n + 1):
        total = total + i
    return total

#---- Main program ----

num = int(input('Please enter an integer to calculate: '))
total_s = sum(num)
print(total_s)
