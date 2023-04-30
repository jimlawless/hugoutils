# Copyright (c) 2023 by Jim Lawless
# https://jiml.us
# MIT/X11 license
# See https://github.com/jimlawless/hugoutils

import datetime
import dbm
import hashlib
import os
import shutil

def sha256sum(filename):
    with open(filename, 'rb', buffering=0) as f:
        return hashlib.file_digest(f, 'sha256').hexdigest()
        
def copyFile(filename):
    dest=filename.replace("public\\","stage\\")
    print("Copying " + filename + " to " + dest)
    os.makedirs(os.path.dirname(dest),exist_ok=True)
    shutil.copy(filename,dest)
    

with dbm.open('snapshot','c') as db:
    paths=[]
    for root, dirs, files in os.walk("public"):
        currentDir=root
        for file in files:
            key = root + "\\" + file
            val = sha256sum(key)
            #print(key + " " + val )
            try:
                mykey=db[key].decode("ascii")
                if mykey != val:
                    copyFile(key)
            except KeyError:
                copyFile(key)
                
            