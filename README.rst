===========================
Recommender System Practice
===========================

Code repo for recommonder system offered by Udemy

Development Tools
-----------------

Install pip tools to compile the requirements for developments::

    pip install -U pip-tools

Compile requirements::

    pip-compile requirements-dev.in > requirements-dev.txt

Install requirements::

    pip install -r requirements-dev.txt

Install pre-commit git hooks::

    pre-commit install -f --install-hooks

Install Tox_ for running tests::

    pip install -U tox

References
----------
.. _Tox: https://tox.readthedocs.io/en/latest/