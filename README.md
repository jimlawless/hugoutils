# hugoutils
Hugo blog utilities

This is just a little collection of scripts that I find useful when updating my Hugo-generated blog at https://jiml.us

Please note that the source code uses Windows slashes as directory separators.

**hugoscan.py** is a script that will create a DBM key/value "database" called **snapshot**.  Run it from your Hugo blog directory.  It will scan the public folder, adding entries to snapshot for each file using the relative path and filename as the key and the SHA-256 hash of that file (converted to a hex string) as the value.  Run this after you've updated your blog or just before you plan to create a new update.

**hugodiff.py** scans the public folder, comparing newly-computed SHA-256 hashes for each file against the ones stored in the snapshot DBM database.  If the hash values differ or if the entry isn't in snapshot, the file is copied to the **stage** folder with the relative directory hierarchy.  When the script finishes, the files in stage are the only ones you should have to publish to your Hugo blog.

Note that you should erase **stage** before running hugodiff.py.
