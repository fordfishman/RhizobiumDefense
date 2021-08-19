import argparse

# parse args
parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter) # help will show default values
parser.add_argument('-f','--file',  type=str, help="Path to input files (.sr files)")
parser.add_argument('-o','--output', default='output.fasta', type=str, help="Path for output fasta")
arguments = parser.parse_args()
filename = arguments.file
output = arguments.output

# read in file
with open(filename, 'r') as r:

    consensus_sr = r.readline().strip()

# make into fasta entry
parts = consensus_sr.split('\t')
header = parts[0]
seq = parts[1]

# append output fasta
with open(output, 'a+') as f: 
    f.write('>{}\n'.format(header))
    f.write('{}\n'.format(seq))


