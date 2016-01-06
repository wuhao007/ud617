#!/usr/bin/python

import sys
import csv
import heapq

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

currPostId = None
output = []
for line in reader:
    if len(line) == 2:
        postId, userId = line
        if currPostId is None:
            output.append(postId)
        elif postId != currPostId:
            if len(output) > 0:
                writer.writerow(output)
            output = []
            output.append(postId) 
        currPostId = postId
        output.append(userId)

writer.writerow(output)
