#!/usr/bin/python

import sys
import csv
import heapq

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

currTag = None
leaderboard = []
cnt = 0
for line in reader:
    if len(line) == 1:
        tag = line[0]
        if tag != currTag:
            heapq.heappush(leaderboard, (cnt, currTag))
            if len(leaderboard) > 10:
                heapq.heappop(leaderboard)
            cnt = 0
 
        currTag = tag
        cnt += 1

if currTag:
    heapq.heappush(leaderboard, (cnt, currTag))
    if len(leaderboard) > 10:
        heapq.heappop(leaderboard)
for cnt, currTag in heapq.nlargest(10, leaderboard, key=lambda x: x[0]):
    writer.writerow([currTag, cnt])

