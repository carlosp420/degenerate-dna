import setuptools

setuptools.setup(
    name="degenerate-dna",
    version="0.0.9",
    url="https://github.com/carlosp420/degenerate-dna",

    author="Carlos Pena",
    author_email="mycalesis@gmail.com",

    description="Python implementation of the Degen Perl package by Zwick et al.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=[],

    license='BSD',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    test_suite='tests',
)
