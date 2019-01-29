#Exercise 4 of session 2

def len_dna():
    sequence = input('Please enter a valid DNA sequence to analyze: ')
    sequence = sequence.upper()
    num = len(sequence)
    A = sequence.count('A')
    C = sequence.count('C')
    G = sequence.count('G')
    T = sequence.count('T')

    return num, A, C, G, T

data = len_dna()

def print_len_dna(n):
    print('Total length: ', n[0])
    print('A: ', n[1])
    print('C: ', n[2])
    print('G: ', n[3])
    print('T: ', n[4])
    return

print(print_len_dna(data))
