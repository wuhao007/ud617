#!/usr/bin/python

import sys

def reducer():
    index = []
    oldKey = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 2:
            # Something has gone wrong. Skip this line.
            continue

        thisKey, thisValue = data_mapped

        if oldKey and oldKey != thisKey and oldKey == "fantastically":
            break
        if thisKey == "fantastically":
            index += [int(thisValue)]
    index.sort()
    print ','.join(map(lambda x: str(x), index))

def main():
    sys.stdin = sys.__stdin__
    reducer()

main()    
