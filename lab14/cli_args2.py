import argparse


print('Hello')

argparser = argparse.ArgumentParser()
argparser.add_argument("symbol", type=str)
argparser.add_argument("multiplier", type=int)
args = argparser.parse_args()

print(args.symbol * int(args.multiplier))


# Tema, adauga inca un argument Sep(separator denumire), si sa arate de forma symbol separator symbol sep
# adaugam un argument -v (verbose) = afiseaza mesajele hello si bye daca este setat la true.


print('Bye')
