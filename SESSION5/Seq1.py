# Program for creating class Seq and Gene and an attribute (strbases) and a method (len)

class Seq:
    """A class for representing sequences"""
    def __init__(self, strbases):
        print('New sequence created!')

        # Initialize the sequence with the value
        # passed as argument when creating the object
        self.strbases = strbases


    def len(self):
        # Return the length of the strings of bases
        return len(self.strbases)

class Gene(Seq):
    """This class is derived from the Seq
        All the objects of class Gene
        inheritage the methods from seq Class."""
    pass

# Notice that even though we have not defined any method in the Class Gene,
# we can create a Gene in the same way we create a Sequence. This is due to
# the inheritance. The Gene objects inheritate the methods and attributes
# from the sequence class (that is called their base class).


# Main program
# Create objects of class Gene and Seq
s1 = Gene('AAATTGACTAGTCATGCTGGATCGACTACTA')
s2 = Seq('ACTAGCTACGATAGCTCATGTAGCTGATGCTATGTGGTGATAG')

# Access the attribute strbases for printing the sequences
str1 = s1.strbases
str2 = s2.strbases

# Invoking the len methods for calculating the sequence length
# Notice the parenthesis: methods always have parenthesis
# but not the attributes!!

l1 = s1.len()
l2 = s2.len()

print('Sequence 1: {}'.format(str1))
print(' length: {}'.format(l1))
print('Sequence 2: {}'.format(str2))
print(' length: {}'.format(l2))
