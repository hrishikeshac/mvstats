=======
mvstats
=======


.. image:: https://img.shields.io/pypi/v/mvstats.svg
        :target: https://pypi.python.org/pypi/mvstats

.. image:: https://img.shields.io/travis/hrishikeshac/mvstats.svg
        :target: https://travis-ci.org/hrishikeshac/mvstats

.. image:: https://readthedocs.org/projects/mvstats/badge/?version=latest
        :target: https://mvstats.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/hrishikeshac/mvstats/shield.svg
     :target: https://pyup.io/repos/github/hrishikeshac/mvstats/
     :alt: Updates


Vectorized multivariate statistical functions for analyzing multi-dimensional earth system data


* Free software: MIT license
* Documentation: https://mvstats.readthedocs.io.


Features
--------

* Vectorized multivariate statistical functions such as covariance, correlation, and regression between two multidimensional datasets
* Can compute lagged relationships
* Can provide confidence levels on relationships
* A handy vectorized 'detrend' function that removes temporal trend in a data
* Built from xarray: returned objects can utilize all of xarray.DataArray() capabilities

Credits
---------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
