#!/usr/bin/python

import sys

def printMax(count, id):
    maxCount = max(count.values())
    for h in count:
        if count[h] == maxCount:
            print id + '\t' + h

currId = None
count = {}
for line in sys.stdin:
    auth_id, hour = line.strip().split("\t")
    if currId is None:
        count = {}
        count[hour] = 1
    elif auth_id == currId:
        count[hour] = count.get(hour, 0) + 1
    else:
        printMax(count, currId)
        count = {}
        count[hour] = 1
    currId = auth_id
if currId:
    printMax(count, currId)
