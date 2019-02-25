# This program will count the number of bases in the sequence, as well as the number of A, C, G and T bases and it percentage

def count_A(seq):
    result = 0
    for i in seq:
        if i == 'A':
            result += 1
    return result

def count_C(seq):
    result = 0
    for i in seq:
        if i == 'C':
            result += 1
    return result

def count_G(seq):
    result = 0
    for i in seq:
        if i == 'G':
            result += 1
    return result

def count_T(seq):
    result = 0
    for i in seq:
        if i == 'T':
            result += 1
    return result

def count_bases(seq):
    nb_a = count_A(seq)
    nb_c = count_C(seq)
    nb_g = count_G(seq)
    nb_t = count_T(seq)

    tl = len(seq)
    print('This is the total length of the sequence: {}'.format(tl))

    if tl > 0:
        perc_a = round(100.0 * nb_a / tl, 1)
        perc_c = round(100.0 * nb_c / tl, 1)
        perc_g = round(100.0 * nb_g / tl, 1)
        perc_t = round(100.0 * nb_t / tl, 1)

    return {'A': [nb_a, perc_a], 'C': [nb_c, perc_c], 'G': [nb_g, perc_g], 'T': [nb_t, perc_t]}


def bonito(dict):
    for key, elements in dict.items():
        print('Base {}'.format(key), '\n   Counter: {}'.format(elements[0]), '\n   Percentage. {}'.format(elements[1]))

# Main program

s1 = input('Please enter Sequence 1: ')
s1 = s1.upper()
s2 = input('Please enter Sequence 2: ')
s2 = s2.upper()

if s1.strip('ACGT') == '':
    seq = s1
    print('-------------------------------------------------')
    print('Sequence 1:')
    dict = count_bases(seq)
    print(bonito(dict))
    print('-------------------------------------------------')
    if s2.strip('ACGT') == '':
        seq = s2
        print('Sequence 2:')
        dict = count_bases(seq)
        print(bonito(dict))
    else:
        print('Sorry, something must be wrong with Sequence 2')
else:
    print('Sorry, something must be wrong with Sequence 1')
