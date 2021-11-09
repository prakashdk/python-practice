from find import is_match_file

def test_is_match_file():
    assert is_match_file("",{})==True
    assert is_match_file("numbers.txt",{'name':'*.txt'})==True
    assert is_match_file("numbers.txt",{'name':'*.py'})==False
    assert is_match_file("numbers.txt",{'type':'d'})==False
    assert is_match_file("find.py",{'type':'f'})==True
    assert is_match_file("find.py",{'size':'+1K'})==True
    assert is_match_file("find.py",{'size':'1K'})==False
    assert is_match_file("find.py",{'size':'-1K'})==False
    assert is_match_file("find.py",{'uid':0})==True
    assert is_match_file("find.py",{'uid':1})==False
    assert is_match_file("find.py",{'mtime':"-1"})==True
    assert is_match_file("find.py",{'mtime':"+1"})==False
    assert is_match_file("find.py",{'mtime':"1"})==False
    assert is_match_file("find.py",{'ctime':"-1"})==False
    assert is_match_file("find.py",{'ctime':"+1"})==True
    assert is_match_file("find.py",{'ctime':"1"})==False


