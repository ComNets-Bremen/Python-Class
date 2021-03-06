Python example files
====================

About this directory
--------------------

The idea of this course is to be programming-driven. We offer a set of example
programs using the basic functions of Python. Interested people should go through
them and try to understand by themself. The links to the corresponding
documentation is given in the header of each individual example file. The main
Python documentation is online available under
[docs.python.org](https://docs.python.org/3).

For the example which require data, the corresponding
[example data files](files) are given in the [files](files) directory.

The order you should go through the examples is given below. After that
tutorial, you should be able to reuse these examples to create your own
applications.

How to start?
-------------

Go through the example files given in the next section and try to understand
them. If you have problems with one file: The link to the documentation is
usually given in the header. The complexity is increasing with each step. After
going through all of these files, you should be able to write a Python script
for plotting data with the following capabilities:

- A command line interface where the input filename and some other options
  like the title, axis description etc. can be defined
- The Data is read and parsed from the given file. Maybe some further analysis
  is done (min, mean, max values)
- The results should be exported to a pdf or text file so they can be used for
  further documentation (i.e., in a report)

Things to implement
-------------------

Some ideas what you could implement for further understanding of the language:

* Hello world example
* Print a square / triangle
* Enter name and gender to formulate a greeting
* Print prime numbers
* Try out the random number generators
* Calculate some statistics from user-given numbers
* Create a simple phone book
* Plot a sine / cosine using matplotlib
* Read data from the files directory and plot statistics
* ...


Commented example files
-----------------------

The examples are sorted in an increasing order, i.e., they are getting more
complex. The files are written in Python 3 **not** in Python 2. Please check
weather you have installed the correction version. If you are new to Python, you
should start at the beginning and go through all examples step by step. If you
are a more experienced programmer, you can use these examples to lookup how to
use certain functions.

1. [01_helloworldExample.py](01_helloworldExample.py)
1. [02_numberExample.py](02_numberExample.py)
1. [03_conditionsExample.py](03_conditionsExample.py)
1. [04_stringExample.py](04_stringExample.py)
1. [05_textInputExample.py](05_textInputExample.py)
1. [06_datastructuresExample.py](06_datastructuresExample.py)
1. [07_loopsExample.py](07_loopsExample.py)
1. [08_castingExample.py](08_castingExample.py)
1. [09_enumerateExample.py](09_enumerateExample.py)
1. [10_functionExample.py](10_functionExample.py)
1. [11_datetimeExample.py](11_datetimeExample.py)
1. [12_randomExample.py](12_randomExample.py)
1. [13_numpyExample.py](13_numpyExample.py)
1. [14_classExample.py](14_classExample.py), [myClassExample.py](myClassExample.py)
1. [15_csvExample.py](15_csvExample.py)
1. [16_argumentParserExample.py](16_argumentParserExample.py)
1. [17_matplotlibExample.py](17_matplotlibExample.py)
1. [18_pickleExample.py](18_pickleExample.py)
1. [19_jsonExample.py](19_jsonExample.py)
1. [20_regularExpressionExample.py](20_regularExpressionExample.py)
1. [21_exceptionsExample.py](21_exceptionsExample.py)


Libraries and the corresponding references
==========================================

This section briefly introduces commonly used libraries for Python. Some
libraries offer similar functionality. The choice depends on the project
requirements and often on the personal preferences.

SciPy
-----

SciPy is a library for scientific calculations and offers for example
algorithms for Fourier Transforms, Interpolation, Statistics etc.

* [Webpage](https://www.scipy.org/)
* [Reference documentation](https://docs.scipy.org/doc/scipy/reference/)

numpy
-----

Numpy is a library for efficient numeric calculations. It is a base library of
SciPy.

* [Webpage](http://www.numpy.org/)
* [Reference documentation](https://docs.scipy.org/doc/numpy/reference/)

Pandas
------

Pandas is a library for high-performance data analysis.

* [Webpage](https://pandas.pydata.org)
* [Reference documentation](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

matplotlib
----------

matplotlib is a graphing library for Python. It can create nice graphs
comparable to the ones creates using Matlab. It is commonly used together mit
Scipy and numpy.

* [Webpage](https://matplotlib.org/)
* [Examples](https://matplotlib.org/gallery/index.html)
* [Tutorials](https://matplotlib.org/tutorials/index.html)
* [Reference documentation](https://matplotlib.org/api/index.html)

Seaborn
-------

Seaborn is based on matplotlib and specialized on statistical data
visualization.

* [Webpage](https://seaborn.pydata.org/)
* [Reference documentation](https://seaborn.pydata.org/api.html)

pyserial
--------

Library for serial communication in Python.

* [Reference and webpage](https://pythonhosted.org/pyserial/)

tkinter
-------

tkinter is a library for platform-independent GUI-design using Python.

* [Webpage](https://wiki.python.org/moin/TkInter)
* [Referecne documentation](https://docs.python.org/3/library/tk.html)

kivy
----

kivy is Python library for the development of touch GUI applications on
Windows, Linux, OS X, Android, iOS and RaspberryPi.

* [Webpage](https://kivy.org)
* [Examples](https://kivy.org/#gallery)
* [Reference documentation](https://kivy.org/doc/stable/api-kivy.html)


SQLAlchemy
----------

SQLAlchemy is an ORM (object-relational mapper), i.e. it represents
database interactions like for example with SQLite as objects in Python. Using
SQLAlchemy, one can write data to a database without knowing SQL.

* [Webpage](https://www.sqlalchemy.org/)
* [Tutorial](https://www.sqlalchemy.org/library.html#tutorials)
* [API](https://docs.sqlalchemy.org/en/latest/)


Virtual environment
===================

Sometimes a project requires the installation of libraries which are either not
available as packages for the current used system or the user can not install
them (limited system access, beta version etc.).

For this case, Python3 comes with a module called `virtualenv` (virtual
environment). It creates a separate directory with an isolated Python path.
`virtualenv` is used on the command line and is handled as follows:

* Create a new virtual environment in the current directory: `python3 -m
  virtualenv .` This directory only has access to the core libraries of the
  system.
* Create a new virtual environment in the current directory **which has access
  to the system wide installed libraries**: `python3 -m virtualenv .
  --system-site-packages`
* Activate the virtual environment: `. ./bin/activate`. The name of the
  environment will be indicated with its name on the command line
* Deactivate the currently used virtual environment: `deactivate`
* Install packages in the environment: `pip3 install <packagename>`

Additional information can be found in the official [Python3 documentation of
the package](https://docs.python.org/3/library/venv.html)

FAQ
===

This section contains the frequently asked questions

Package cannot be found
-----------------------

Depending on your Python installation, you might get an error message
complaining that a package is missing like for example the numpy package. You
can install most packages using the pip tool.

* On Unix / Linux / MacOS, you can usually use `pip3 install <package name>` to
  install packages
* On Windows, you will find the corresponding command in the
  `C:\Python2x\Scripts` directory. Open a shell, change into that directory and
  execute the command as mentioned above

For this tutorial, the following packages are required:

* `pip3 install numpy`
* `pip3 install python-dateutil`
* `pip3 install matplotlib`

For Linux based systems, you can also install the packages using the system
package manager. On a Debian / Ubuntu system, the following commands will
install the corresponding packages. You should prefer this way over the pip
command:

* `sudo apt install python-numpy`
* `sudo apt install python-dateutil`
* `sudo apt install python-matplotlib`

I got an *IndentationError*
---------------------------

Maybe you are mixing space an tabs. According to the documentation
(https://www.python.org/dev/peps/pep-0008/#tabs-or-spaces), you should stick to
spaces. It is also a good idea to setup you text editor to highlight tabs and
replace tabs by spaces (preferable 4 spaces).

Timestamp vs. Datetime
----------------------

Dates and times can be represented in different formats. The human-readable
format (2017-04-08 01:00PM or 8.4.17 13:00) and Unix timestamp are the most
common ones. The timestamp gives the number of seconds since 1970-01-01 and has
several advantages in performing calculations and storing the values. In
most cases, it is easier to convert dates and times to timestamps and only
convert them back if they are shown to the user.

https://en.wikipedia.org/wiki/Unix_time

Naming your programs
--------------------

When naming your program, you should ensure that you are not using a reserved
name (i.e. a module name) as Python will try to import your app instead of the
system module. So do not use filenames like `matplotlib.py`, `numpy.py`,
`int.py` etc.


Tuples vs. Lists
----------------

Tuples and lists look quite similar but are showing crucial differences.
Tuples are fixed (immutable) and cannot be changed after the assignment but are
faster compared to lists. Lists are dynamically assigned (mutable) and thus
are more flexible  but are slower in processing.

So use tuples if
* You need a write-protected structure
* A faster structure

For everything else you should prefer lists
