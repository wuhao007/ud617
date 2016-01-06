#!/usr/bin/python

import sys

def reducer():
    count = 0
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisValue = data_mapped

        if oldKey and oldKey != thisKey:
            if oldKey == "fantastic":
                print oldKey, "\t", count
            count = 0

        oldKey = thisKey
        count += 1

    if oldKey == "fantastic":
        print oldKey, "\t", count

def main():
    sys.stdin = sys.__stdin__
    reducer()

main()    
