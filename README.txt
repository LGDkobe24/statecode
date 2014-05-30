Statecode
=========

Convert US state names to state abbreviations using regular expressions.

Installation
------------

    git clone https://github.com/vincentarelbundock/statecode
    cd statecode
    python setup.py install

Example
-------

::
    In [1]: from statecode import statecode

    In [2]: statecode(['Arizona', 'Utah'])
    Out[2]: ['AZ', 'UT']

    In [3]: statecode(['AZ', 'UT'], origin='abbreviation', target='state')
    Out[3]: ['Arkansas', 'Utah']
