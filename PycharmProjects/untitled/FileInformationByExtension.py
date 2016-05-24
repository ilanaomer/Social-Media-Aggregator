from collections import defaultdict
import sys
from pathlib import Path
import os

try:
    path = sys.argv[1]
except IndexError:
    path = "xxx"

if os.path.isdir(path): # os.path.exists(sys.argv[1])
    def create_files_information():
        return {
            'amount': 0,
            'sizeTotal': 0,
        }

    filesInformation = defaultdict(create_files_information)

    folder = Path(path)
    for p in folder.iterdir():
        if p.is_file():
            suffixName = p.suffix[1:]
            if suffixName == "":
                suffixName = "."
            if filesInformation[suffixName]['amount'] == 0:
                filesInformation[suffixName]['amount'] = 1
            else:
                filesInformation[suffixName]['amount'] += 1
            filesInformation[suffixName]['sizeTotal'] += p.stat().st_size

    for name, info in sorted(filesInformation.items()):
        print("{} {amount} {sizeTotal}".format(name, **info))
else:
    print("usage: ext_info.py path\ndisplays number of files and total size of files per extension in the specified path.")
