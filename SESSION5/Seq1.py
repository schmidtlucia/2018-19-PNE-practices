class Seq:
    """A class for representing sequences"""
    def __init__(self, str_bases):
        print('New sequence created!')

        self.str_bases = str_bases

    def len(self):
        return len(self.str_bases)

class Gene(Seq):
    """This class is derived from the Seq
        All the objects of class Gene
        inheritage the methods from seq Class."""
    pass



s1 = Gene('AAATTGACTAGTCATGCTGGATCGACTACTA')
s2 = Seq('ACTAGCTACGATAGCTCATGTAGCTGATGCTATGTGGTGATAG')

str1 = s1.str_bases
str2 = s2.str_bases

l1 = s1.len()
l2 = s2.len()

print('Sequence 1: {}'.format(str1))
print('Sequence 2: {}'.format(str2))
print(' length: {}'.format(l1))
print(' length: {}'.format(l2))

print('the end')
