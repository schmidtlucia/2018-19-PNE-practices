import termcolor
from Seq import Seq
import requests
import sys


server = "http://rest.ensembl.org"
# the following variable uses the given identifier to return its latest version
ext = "/sequence/id/ENSG00000165879?"  # ENSG00000165879 este es el código para el FRAT1 gene

r = requests.get(server + ext, headers={"Content-Type": "application/json"})

if not r.ok:
    r.raise_for_status()
    sys.exit()

decoded = r.json()

# we have to extract out of the 'decoded' dictionary the value for the key that corresponds to the DNA serquence of our gene
# in this case the key is 'seq'

sequence = decoded['seq']
sequence = Seq(sequence)

num = sequence.count('A') + sequence.count('C') + sequence.count('G') + sequence.count('T')
base_t = sequence.count('T')
percentage = {'A': sequence.perc('A'), 'C': sequence.perc('C'), 'G': sequence.perc('G'), 'T': sequence.perc('T')}

maximum = max(sequence.perc('A'), sequence.perc('C'), sequence.perc('G'), sequence.perc('T'))

for base in percentage:
    if percentage[base] == maximum:
        popularity = base
        percen_pop = percentage[base]
1
print()
termcolor.cprint('The asked information about the {} gene is:\n'.format(ext[13:-1]), 'red')
termcolor.cprint('  The FRAT1 gene contains {} bases in total.'.format(num), 'yellow')

termcolor.cprint('  It contains {} T bases.'.format(base_t), 'yellow')
termcolor.cprint('  The most popular base in the sequence is the {} base with a percentage of {} %'.format(popularity, percen_pop), 'yellow')

for base in percentage:
    termcolor.cprint('  The percentage of the {} base is {} %'.format(base, percentage[base]), 'green')
