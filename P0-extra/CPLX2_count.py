#Extra-exercise 2 of session 3

with open('CPLX2.txt', 'r') as f:
    for row in f:
        A = 0
        C = 0
        G = 0
        T = 0
        i = 0
        length_row = len(row.replace('\n', ''))
        while i < length_row:
            base = row[i]
            if base == '>':
                i += (row[i:].find('\n'))
            elif base == 'A':
                A += 1
                i += 1
            elif base == 'C':
                C += 1
                i += 1
            elif base == 'G':
                G += 1
                i += 1
            elif base == 'T':
                T += 1
                i += 1
        print('Total length: ',length_row)
        print('A:',A)
        print('C:',C)
        print('G:',G)
        print('T:',T)
