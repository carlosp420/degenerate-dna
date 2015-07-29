=====
Usage
=====
This package BOLD can be used to interact with the BOLDSYSTEMS API. We can use
methods to interact with the several end-points.

ID Engine API
-------------
The ID Engine API is found at this URL:
http://www.boldsystems.org/index.php/resources/api?type=idengine

How to use it:

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AAC'
    >>> res = Degenera(dna=dna, table=1, type='normal')
    >>> res.degenerate()
    >>> res.degenerated
    'AAY'

