#!/usr/bin/python

import sys
import csv
import string

def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    specials = '.,!?:;"()<>[]#$=-/'
    trans = string.maketrans(specials, ' ' * len(specials))
   
    for line in reader:
        if len(line) == 19:
            node_id, words = line[0], line[4].translate(trans).strip().split()
            for word in words:
                print "{0}\t{1}".format(word.lower(), node_id)

def main():
    sys.stdin = sys.__stdin__
    mapper()

main()
