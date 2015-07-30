degenerate-dna
==============

.. image:: https://pypip.in/v/degenerate-dna/badge.png
    :target: https://pypi.python.org/pypi/degenerate-dna
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/carlosp420/degenerate-dna.png
   :target: https://travis-ci.org/carlosp420/degenerate-dna
   :alt: Latest Travis CI build status

Python implementation of the Degen Perl package by Zwick et al.

http://www.phylotools.com/ptdegenoverview.htm

Usage
-----

    >>> from degenerate_dna import Degenera
    >>> dna = 'AGTTCT'
    >>> res = Degenera(dna=dna, table=1, type='S')
    >>> res.degenerate()
    >>> res.degenerated
    'AGYAGY'

Installation
------------

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
