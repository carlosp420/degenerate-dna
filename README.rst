.. image:: https://badge.fury.io/py/degenerate-dna.svg
    :target: https://pypi.python.org/pypi/degenerate-dna
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/carlosp420/degenerate-dna.png
   :target: https://travis-ci.org/carlosp420/degenerate-dna
   :alt: Latest Travis CI build status

degenerate-dna
==============

Python implementation of the Degen Perl package by Zwick et al.

http://www.phylotools.com/ptdegenoverview.htm

Usage
-----
.. code:: python

    >>> from degenerate_dna import Degenera
    >>> dna = 'AGTTCT'
    >>> res = Degenera(dna=dna, table=1, method='S')
    >>> res.degenerate()
    >>> res.degenerated
    'AGYAGY'

Installation
------------
.. code:: shell

    pip install degenerate-dna

Requirements
^^^^^^^^^^^^
python +3

Licence
-------
BSD

Authors
-------
`Carlos Peña <mycalesis@gmail.com>`_.
