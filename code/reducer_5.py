#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

currId = None
postLen = 0
lenSum = 0
cnt = 0
for line in reader:
    id, type, size = line
    if currId is None:
        lenSum = 0
        cnt = 0
    elif id != currId:
        if cnt > 0:
            writer.writerow([currId, postLen, float(lenSum) / cnt])
        lenSum = 0
        cnt = 0
    if type == "q":
        postLen = int(size)
    elif type == "a":
        lenSum += int(size)
        cnt += 1
    currId = id 
if cnt > 0:
    writer.writerow([currId, postLen, float(lenSum) / cnt])
