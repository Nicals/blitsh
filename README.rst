Blitch
======

A python 3+ webshell.

This project is inspired from `Weevely <https://github.com/epinna/weevely3>`_.
You should check it out, it really worths it as it have far much functionality than this.


Development
-----------

Run the test suite with ``tox`` if you have it installed.
This is the prefered usage since it will check the project for every
supported python interpreter.
It will also unit test the distribution and the documentation.

.. code:: shell-session

    $ python tox

If you prefer to only run package test suite with only your current python
interpreter:

.. code:: shell-session

    $ pip install .[tests]
    $ py.test
