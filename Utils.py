MACHINE = {
    "014c" : "Intel 80386",
    "014d" : "Intel 80486",
    "014e"  : "Intel Pentium"
}
class bcolors:
    colors = {
        "OK"     :      "\033[92m" ,
        "WARNING" :     "\033[93m",
        "FAIL"    :     "\033[91m",
        "RESET"   :     "\033[0m"
    }

class Utils:

    """
    A class for all Utility classes and functions for building the other classes
    """

    def __init__(self) -> None:
        self.bcolors = bcolors.colors

    def getMachine(self,code):
        print(code)
        try:
            return MACHINE[code]
        except (KeyError):
            return "Machine Unknown"

    def color(self,string="",condition="OK"):
        RESET = "RESET"
        return f"{bcolors.colors[condition]}[*] {string} {bcolors.colors[RESET]}"

    def removeZeros(self,listObj):
        for i in range(len(listObj)):
            if(listObj[i] != '00'):
                break
            listObj[i] = ''

    def reverseBytes(self,string=b""):
        Bytes = string.hex(':').split(':')
        self.removeZeros(Bytes)
        Bytes.reverse()
        return "".join(Bytes)

    def line(self,char="*",length=10):
        linearr = [char for i in range(length)]
        linestr = "".join(linearr)
        return self.color(f"{linestr} [*]")


if __name__ == "__main__":
    Utils()