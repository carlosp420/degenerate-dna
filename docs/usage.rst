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
    >>> res = Degenera(dna=dna, table=1, method='normal')
    >>> res.degenerate()
    >>> res.degenerated
    'AAY'

Degenerate using the Standard Genetic code and the method *S*.

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AGTTCT'
    >>> res = Degenera(dna=dna, table=1, method='S')
    >>> res.degenerate()
    >>> res.degenerated
    'AGYAGY'

Degenerate using the Standard Genetic code and the method *Z*.

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AGTTCT'
    >>> res = Degenera(dna=dna, table=1, method='Z')
    >>> res.degenerate()
    >>> res.degenerated
    'TCNTCN'

Degenerate using the Standard Genetic code and the method *SZ*.

.. doctest::

    >>> from degenerate_dna import Degenera
    >>> dna = 'AGTTCT'
    >>> res = Degenera(dna=dna, table=1, method='SZ')
    >>> res.degenerate()
    >>> res.degenerated
    'NNNNNN'
