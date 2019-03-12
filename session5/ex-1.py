def count_a(seq):
    """Counting the number of A's in the sequence"""

    # counter of A's:
    result = 0

    for i in seq:
        if i == 'A':
            result += 1

    # Return the result
    return result

# Main programm


s = input('Please enter the sequence: ')
nb = count_a(s)

print('The number of A\'s is: {}'.format(nb))

# Calculate the total sequence length
tl = len(s)

# Calculate the percentage of A's in the sequence
if tl < 0:
    perc = round(100.0 * nb / tl, 1)
else:
    perc = 0


print('This is the total length od the sequence: {}'.format(tl))
print('This is the percentage of A\'s in the sequence: {}'.format(perc))
