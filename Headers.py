DOS_MZ_HEADER = {
    "SIGNATURE" : 0,
    "Last Page Size" : 0,
    "Total Pages in File" : 0,
    "Relocation Items" : 0,
    "Paragraphs in Header" : 0,
    "Minimum Extra Paragraphs" : 0,
    "Maximum Extra Paragraphs" : 0,
    "Initial Stack Segment" : 0,
    "Initial Stack Pointer" : 0,
    "Complemented Checksum" : 0,
    "Initial Instruction Pointer" : 0,
    "Initial Code Segment" : 0,
    "Relocation Table Offset" : 0,
    "Overlay Number" : 0,
    "Reserved" : [0,0,0,0],
    "Offset to New Header" : 0
}

IMAGE_OPTIONAL_HEADER = {
    "Magic" : 0,
    "Linker Version" : 0,
    "Size Of Code" : 0
}

IMAGE_FILE_HEADER = {
    "Machine" : 0,
    "NumberOfSections" : 0,
    "TimeDataStamp" : 0,
    "PointerToSymbolTable" : 0,
    "SizeOfOptionalHeader" : 0,
    "SizeOfOptionalHeader" : 0
}

IMAGE_NT_HEADER = {
    "SIGNATURE" : 0,
    "FileHeader" : IMAGE_FILE_HEADER.copy(),
    "OptionalHeader" : IMAGE_OPTIONAL_HEADER.copy()
}

class Headers:

    def __init__(self):
        self.DOS_MZ_HEADER = DOS_MZ_HEADER.copy()
        self.IMAGE_OPTIONAL_HEADER = IMAGE_OPTIONAL_HEADER.copy()
        self.IMAGE_FILE_HEADER = IMAGE_FILE_HEADER.copy()
        self.IMAGE_NT_HEADER =  IMAGE_NT_HEADER.copy()


if __name__ == "__main__":
    Headers()
