=====
Usage
=====
This package ``degenerate-dna`` is a Python implementation of Zwick's et al method
to degenerate DNA sequences.

API
---
How to use it:

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AAC'
    >>> res = Degenera(dna=dna, table=1, type='normal')
    >>> res.degenerate()
    >>> res.degenerated
    'AAY'

