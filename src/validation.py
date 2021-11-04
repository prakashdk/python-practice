
class Validation:

    def is_valid_size(self, size):
        return len(size) >= 2 and size[-1] in ["B", "K", "M", "G"] and self.isint(size[:-1])

    def isint(self, num):
        if "-" in num or "+" in num:
            return len(num) >= 2 and num[1:].isdigit()
        return num.isdigit()
