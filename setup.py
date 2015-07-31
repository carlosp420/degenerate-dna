import setuptools

setuptools.setup(
    name="degenerate-dna",
    version="0.0.5",
    url="https://github.com/carlosp420/degenerate-dna",

    author="Carlos Pena",
    author_email="mycalesis@gmail.com",

    description="Python implementation of the Degen Perl package by Zwick et al.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    license='BSD',

    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
)
