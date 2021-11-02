# UNIX `find` command using Python

### Usage 
>  The `find` command is used to find files matching given conditions at the specified path.

### Synopsis

> find [-t] [-n] [-u] [expression]

### Options

>-t type
>    True if the file is of the specified type.  Possible file types are as follows: 
>    d       directory
>    f       regular file
>    l       symbolic link
>
>-n name pattern
>     True if the last component of the pathname being examined matches pattern.  Special shell pattern >matching characters (``['', ``]'', ``*'', and ``?'') may be used as part of pattern.  
>     These characters may be matched explicitly by escaping them with a backslash (``\'').     
>-u user uname
>     True if the file belongs to the user uname.  If uname is numeric and there is no such user name, 
>     then uname is treated as a user ID.
>--uid uname
>     The same thing as -user uname for compatibility with GNU find.  GNU find imposes a restriction that uname >is numeric, while find(1) does not.
>
>--size n[ckMGTP]
>     True if the file's size, rounded up, in 512-byte blocks is n.  If n is followed by a c, then the primary >is true if
>     the file's size is n bytes (characters).  Similarly if n is followed by a scale indicator then the file's >size is compared to n scaled as:
>     k       kilobytes (1024 bytes)
>     M       megabytes (1024 kilobytes)
>     G       gigabytes (1024 megabytes)
>     T       terabytes (1024 gigabytes)
>     P       petabytes (1024 terabytes)
>
>--mtime n[smhdw]
>     If no units are specified, this primary evaluates to true if the difference between the file last >modification time and the time find was started, rounded up to the next full 24-hour period, is n 24-hour >periods.
>     If units are specified, this primary evaluates to true if the difference between the file last >modification time and the time find was started is exactly n units.  Please refer to the -atime primary >description for information on supported time units.   
>
>--ctime n[smhdw]
>     If no units are specified, this primary evaluates to true if the difference between the time of last >change of file status information and the time find was started, rounded up to the next full 24-hour >period, is n 24-hour periods.
>     If units are specified, this primary evaluates to true if the difference between the time of last change >of file status information and the time find was started is exactly n units.  Please refer to the -atime >primary description for information on supported time units.

