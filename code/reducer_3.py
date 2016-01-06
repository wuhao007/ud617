#!/usr/bin/python

import sys

def reducer():
    userinfo = []
    currentuserid = None

    for line in sys.stdin:
        data_mapped = line.strip().split("\t")
        if len(data_mapped) != 6 and len(data_mapped) != 10:
            continue
        if data_mapped[1] == "A" and currentuserid != data_mapped[0]:
            userinfo = data_mapped
            currentuserid = data_mapped[0]
        elif data_mapped[1] == "B" and currentuserid == data_mapped[0]:
            author_id, clasif, id, title, tagnames, node_type, parent_id, abs_parent_id, added_at, score = data_mapped
            print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(id, title, tagnames, author_id, node_type, parent_id, abs_parent_id, added_at, score, userinfo[2], userinfo[3], userinfo[4], userinfo[5])

def main():
    sys.stdin = sys.__stdin__
    reducer()

main()    
