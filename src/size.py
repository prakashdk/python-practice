class Size:
    def __init__(self, size):
        self.size = size

    def is_valid_size(self):
        return len(self.size) >= 2 and self.size[-1] in ["B", "K", "M", "G"] and self.isint()

    def isint(self):
        num = self.size[:-1]
        if "-" in num or "+" in num:
            return len(num) >= 2 and num[1:].isdigit()
        return num.isdigit()

    def match_size(self, filesize):
        if self.is_valid_size():
            return self.process_size(filesize)
        else:
            print("Invalid size")
            exit(1)

    def process_size(self, filesize):
        units = {
            "B": 0,
            "K": 1,
            "M": 2,
            "K": 3,
            "G": 4,
        }
        unit = self.size[-1]
        exp_size = self.size[:-1]
        calc_size= int(exp_size)*(1024**units[unit])
        if "-" in exp_size:
            return filesize <= abs(calc_size)
        elif "+" in exp_size:
            return filesize >= calc_size
        return filesize == calc_size