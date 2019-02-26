# Main program of Practice 1

from Seq import Seq

# Creation of four sequences

s1 = Seq('ACTGTTGCTAG')
s2 = Seq('TTGACGAT')
s3 = s1.complement()
s4 = s3.reverse()

seq_list = [s1, s2, s3, s4]
seq_id = 1

for seq in seq_list:
    print('---------------------------------------')
    print('Sequence {}:'.format(seq_id), seq.strbases)
    print('     Length:', seq.len())
    bases = ['A', 'C', 'G', 'T']
    seq_id += 1
    for i in bases:
        print('     Bases count: {}'.format(i, seq.count(i)))
        print('     Bases {} percentage: {}'.format(i, seq.perc(i)), '%')