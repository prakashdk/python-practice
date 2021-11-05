import os
from fnmatch import fnmatch
from size import Size
from timeoption import Time


class Option:
    """Validates and process all the options of 'find' command"""

    def __init__(self, file):
        self.file = file
        self.match = True

    def set_match(self, b):
        """sets the bool 'match' variable which is the result for all verified options """
        self.match = self.match and b

    def match_by_name(self, pattern):
        """Function for '-name' option. Matches the files by name """
        self.set_match(
            fnmatch(self.file, pattern) or pattern in self.file)

    def match_by_type(self, type):
        """Function for '-type' option. Matches the files by type [d(directory) f(file) l(symbolic link)] """
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

    def match_by_user(self, user):
        """Function for '-user' option. Matches the files by user """
        # To be fixed.
        # Problem : Can't find user in windows

        
        ###self.set_match(pwd.getpwuid(os.stat("sample.txt").st_uid).pw_name)==user) 
        #According to google, above line works on linux by importing 'pwd' module

    def match_by_uid(self, uid):
        """Function for '-uid' option. Matches the files by uid """
        self.set_match(os.stat(self.file).st_uid == uid)

    def match_by_size(self, size):
        """Function for '-size' option. Matches the files by size using 'Size' class """
        self.set_match(Size(size).match_size(os.stat(self.file).st_size))

    def match_by_mtime(self, mtime):
        """Function for '-mtime(modified time)' option. Matches the files by mtime(modified time) using 'Time' class"""
        self.set_match(Time(mtime).compare_time(os.stat(self.file).st_mtime))

    def match_by_ctime(self, ctime):
        """Function for '-ctime(created time)' option. Matches the files by ctime(created time) using 'Time' class """
        self.set_match(Time(ctime).compare_time(os.stat(self.file).st_ctime))

    def is_match(self):
        return self.match
