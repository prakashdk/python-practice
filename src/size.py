class Size:

    """Processes the size option"""

    def __init__(self, size):
        self.size = size

    def is_valid_size(self):
        """Checks the user provided option valid or not"""
        return len(self.size) >= 2 and self.size[-1] in ["B", "K", "M", "G"] and self.isint()

    def isint(self):
        """Sub function for size validation which is used for integer validation"""
        num = self.size[:-1]
        if "-" in num or "+" in num:
            return len(num) >= 2 and num[1:].isdigit()
        return num.isdigit()

    def match_size(self, filesize):
        """matches the files with 'process_size'"""
        if self.is_valid_size():
            return self.process_size(filesize)
        else:
            print("Invalid size")
            exit(1)

    def process_size(self, filesize):
        """processes the user provided size to compare file sizes"""
        units = {
            "B": 0,
            "K": 1,
            "M": 2,
            "G": 4,
        }
        unit = self.size[-1]
        opt_size = self.size[:-1]
        calc_size = int(opt_size)*(1024**units[unit])
        if "-" in opt_size:
            return filesize <= abs(calc_size)
        elif "+" in opt_size:
            return filesize >= calc_size
        return filesize == calc_size
