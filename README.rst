degenerate-dna
==============

.. list-table::
    :stub-columns: 1

    * - tests
      - | |travis| |requires| |coveralls|
        | |quantified-code|
    * - package
      - |version| |wheel| |supported-versions| |supported-implementations|

.. |travis| image:: https://travis-ci.org/carlosp420/degenerate-dna.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/carlosp420/degenerate-dna

.. |requires| image:: https://requires.io/github/carlosp420/degenerate-dna/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/carlosp420/degenerate-dna/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/carlosp420/degenerate-dna/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/carlosp420/degenerate-dna

.. |version| image:: https://img.shields.io/pypi/v/degenerate-dna.svg?style=flat
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/degenerate-dna

.. |wheel| image:: https://img.shields.io/pypi/wheel/degenerate-dna.svg?style=flat
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/degenerate-dna

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/degenerate-dna.svg?style=flat
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/degenerate-dna

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/degenerate-dna.svg?style=flat
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/degenerate-dna

.. |quantified-code| image:: https://www.quantifiedcode.com/api/v1/project/fdd4eceac24d47adb5b9e73f475de560/badge.svg
   :target: https://www.quantifiedcode.com/app/project/fdd4eceac24d47adb5b9e73f475de560
   :alt: Code issues


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
python 2.6, 2.7, 3.3, 3.4, 3.5

Licence
-------
BSD

Authors
-------
`Carlos Peña <mycalesis@gmail.com>`_.
