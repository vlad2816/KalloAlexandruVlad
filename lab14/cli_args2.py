import argparse


argparser = argparse.ArgumentParser()
argparser.add_argument("symbol", type=str)
argparser.add_argument("sep", type=str, help='Increase a string')
argparser.add_argument("multiplier", type=int)
argparser.add_argument('-v', action='store_true')
args = argparser.parse_args()
print('Hello')
print(args.symbol * int(args.multiplier))


# Tema, adauga inca un argument Sep(separator denumire), si sa arate de forma symbol separator symbol sep
# adaugam un argument -v (verbose) = afiseaza mesajele hello si bye daca este setat la true.

if args.v:
    print('Bye')
