.. image:: https://badge.fury.io/py/degenerate-dna.svg
    :target: https://pypi.python.org/pypi/degenerate-dna
    :alt: Latest PyPI version

.. image:: https://travis-ci.org/carlosp420/degenerate-dna.png
   :target: https://travis-ci.org/carlosp420/degenerate-dna
   :alt: Latest Travis CI build status

.. image:: https://coveralls.io/repos/carlosp420/degenerate-dna/badge.svg?branch=master&service=github
   :target: https://coveralls.io/github/carlosp420/degenerate-dna?branch=master
   :alt: Coveralls

.. image:: https://www.quantifiedcode.com/api/v1/project/fdd4eceac24d47adb5b9e73f475de560/badge.svg
   :target: https://www.quantifiedcode.com/app/project/fdd4eceac24d47adb5b9e73f475de560
   :alt: Code issues

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
