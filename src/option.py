import os
from fnmatch import fnmatch
from size import Size


class Option:
    def __init__(self, file):
        self.file = file
        self.match = True

    def set_match(self, b):
        self.match = self.match and b

    def match_by_name(self, pattern):
        self.set_match(
            fnmatch(self.file, pattern) or pattern in self.file)

    def match_by_type(self, type):
        filetypes = {
            "d": os.path.isdir,
            "f": os.path.isfile,
            "l": os.path.islink,
        }
        if not type in filetypes.keys():
            print(f"Invalid type of file '{type}'")
            self.set_match(False)
            exit(1)
        self.set_match(filetypes[type](self.file))
    
    def match_by_user(self,user):
        pass

    def match_by_uid(self,uid):
        self.set_match(os.stat(self.file).st_uid==uid)

    def match_by_size(self, size):
        self.set_match(Size(size).match_size(os.stat(self.file).st_size))
    
    def match_by_mtime(self,mtime):
        pass
    def match_by_ctime(self,ctime):
        pass

    def is_match(self):
        return self.match

    def compare(self,a,b):
        if "-" in b:
            return a <= abs(int(b))
        elif "+" in b:
            return a >= int(b)
        return a == int(b)
