# Copyright (c) 2023 by Jim Lawless
# https://jiml.us
# MIT/X11 license
# See https://github.com/jimlawless/hugoutils

# Scan the public\* folder hierarchy, storing SHA-256 hashes for
# each file in the DBM database "snapshot.*"

import datetime
import dbm
import hashlib
import os

def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()

with dbm.open('snapshot','c') as db:
    paths=[]
    for root, dirs, files in os.walk("public"):
        currentDir=root
        for file in files:
            key = str(root + "\\" + file)
            val = str(sha256sum(key))
            print(key + " " + str(val) )
            db[key]=val
            