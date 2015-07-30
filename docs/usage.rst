=====
Usage
=====
This package ``degenerate-dna`` is a Python implementation of Zwick's et al method
to degenerate DNA sequences.

API
---
Degenerate using the Standard Genetic code.

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AAC'
    >>> res = Degenera(dna=dna, table=1, type='normal')
    >>> res.degenerate()
    >>> res.degenerated
    'AAY'

Degenerate using the Standard Genetic code and the method *S*.

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AGTTCT'
    >>> res = Degenera(dna=dna, table=1, type='S')
    >>> res.degenerate()
    >>> res.degenerated
    '---'

Degenerate using the Standard Genetic code and the method *Z*.

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AGTTCT'
    >>> res = Degenera(dna=dna, table=1, type='Z')
    >>> res.degenerate()
    >>> res.degenerated
    '---'

Degenerate using the Standard Genetic code and the method *SZ*.

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AGTTCT'
    >>> res = Degenera(dna=dna, table=1, type='SZ')
    >>> res.degenerate()
    >>> res.degenerated
    '---'
