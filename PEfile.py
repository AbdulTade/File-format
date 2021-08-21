import os
import sys

import Utils
import Headers

IMAGE_NT_HEADER = Headers.IMAGE_NT_HEADER
IMAGE_OPTIONAL_HEADER = Headers.IMAGE_OPTIONAL_HEADER
DOS_MZ_HEADER = Headers.DOS_MZ_HEADER

utils = Utils.Utils()
color = utils.color
line = utils.line
getMachine = utils.getMachine
reverseBytes = utils.reverseBytes
paths = []

DWORD = 4
WORD  = 2







def Populate_NT_HEADER(offset,filecontents):
    image_nt_header = IMAGE_NT_HEADER.copy()
    end = offset+DWORD
    image_nt_header["SIGNATURE"] = filecontents[offset:end]
    image_nt_header["FileHeader"] = IMAGE_OPTIONAL_HEADER.copy()
    end = end+1
    image_nt_header["FileHeader"]["Machine"] = getMachine(reverseBytes(filecontents[end:end+WORD+1]))
    print(color(image_nt_header))


def PopulateHeaders(path=""):
    try:
        f = open(path,"rb")
        contents = f.read()
        signature = contents[:2]
        dos_mz_header = DOS_MZ_HEADER.copy()
        if(signature == b'MZ'):
            dos_mz_header["SIGNATURE"] = signature
            PE_OFFSET = int(reverseBytes(contents[59:64]),base=16)
            dos_mz_header["Offset to New Header"] = PE_OFFSET
            Populate_NT_HEADER(PE_OFFSET,contents)
            print(color(dos_mz_header))
        else:
            print(color(f"{path} not a Portable Executable","FAIL"))
            sys.exit(-1)
    except (FileNotFoundError):
        print(color(f"File {path} does not exist",condition="FAIL"))

if(len(sys.argv) >= 2):
        paths = sys.argv[1:]
else:
    print(color("Usage: python PEfile.py [PATHS]",condition="FAIL"))


if __name__ == "__main__":
    for path in paths:
        print(line(length=100))
        PopulateHeaders(path=path)
