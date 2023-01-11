Have you ever wondered how do relative imports work? 


Im pretty sure that you've done something like that at some point:


from . import bar
from .bar import foo



It's using a special magic attribute on the module called __package__.
Lets say you have the following structure:


foo/
    __init__.py
    bar/
        __init__.py
main.py



The value of __package__ for foo/__init__.py is set to "foo", and for foo/bar/__init__.py its "foo.bar".


Note that for main.py __package__ isn't set, that's because main.py is not in a package.


So when you're doing from .bar import buz within foo/__init__.py, 
it simply appends "bar" to foo/__init__.py's __package__ attribute, esentially it gets translated to from foo.bar import buz.


You can actually hack __package__, e.g:


>>> __package__ = "re"
>>> from . import compile
>>> compile
<function compile at 0x10e0ee550>