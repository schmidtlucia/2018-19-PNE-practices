#Exercise 5 of session 2

with open('DNA-seq.csv', 'r') as f:
    for row in f:
        def len_dna():
            num = len(row.replace('\n', ''))
            A = row.count('A')
            C = row.count('C')
            G = row.count('G')
            T = row.count('T')
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
