import sys

def has_argument():
    if len(sys.argv>1):
        return sys.argv[1:]
    raise Exception("N arguments provided")
