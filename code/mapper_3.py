#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
    if len(line) == 19:
        id, title, tagnames, author_id, body, node_type, parent_id, abs_parent_id, added_at, score, state_string, last_edited_id, last_activity_by_id, last_activity_at, active_revision_id, extra, extra_ref_id, extra_count, marked = line
        if author_id is not None and author_id != "author_id":
            d = datetime.strptime(added_at, "%Y-%m-%d %H:%M:%S.%f+00")
            print author_id + '\t' + str(int(d.strftime("%H")))
