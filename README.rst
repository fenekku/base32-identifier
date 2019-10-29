..
   This file is part of base32-identifier
   Copyright (C) 2019 CERN.
   Copyright (C) 2019 Northwestern University,
                      Galter Health Sciences Library & Learning Center.

   base32-identifier is free software; you can redistribute it and/or modify it
   under the terms of the MIT License; see LICENSE file for more details.


=================
base32-identifier
=================

.. image:: https://img.shields.io/travis/inveniosoftware/base32-identifier.svg
        :target: https://travis-ci.org/inveniosoftware/base32-identifier

.. image:: https://img.shields.io/coveralls/inveniosoftware/base32-identifier.svg
        :target: https://coveralls.io/r/inveniosoftware/base32-identifier

.. image:: https://img.shields.io/github/tag/inveniosoftware/base32-identifier.svg
        :target: https://github.com/inveniosoftware/base32-identifier/releases

.. image:: https://img.shields.io/pypi/dm/base32-identifier.svg
        :target: https://pypi.python.org/pypi/base32-identifier

.. image:: https://img.shields.io/github/license/inveniosoftware/base32-identifier.svg
        :target: https://github.com/inveniosoftware/base32-identifier/blob/master/LICENSE


Small library to generate, encode and decode random base32 identifiers with nice properties.

Usage
=====

.. code-block:: python

    import base32_identifier as base32

    # Generate
    ## Generate a random identifier
    base32.generate()
    # -> abcd1234

    # Generate a random identifier with bells and whistle
    base32.generate(length=10, split_every=5, checksum=True)
    # ->

    # Encode a pre-existing number
    base32.encode(1234, split_every=3, checksum=True) == "16j-82"

    # Decode an identifier
    base32.decode("16j-82", checksum=True) == 1234

    base32.decode("16i-82", checksum=True)
    # raises ValidationError

Features
========

- Generation, encoding and decoding of identifiers
- Decoding of any-case identifiers
- Configurable length identifiers
- Randomness through cryptographically secure random number generator
- Douglas Crockford base32 encoding
- URL-safe identifiers with no problematic special characters
- Optional ISO-7064 checksum
- Optional hyphenation


Installation
============

The base32-identifier package is on PyPI so all you need is:

.. code-block:: console

    pip install base32-identifier


Development
===========

.. code-block:: console

    pipenv run pip install -e .[docs,tests]

Tests
-----

.. code-block:: console

    pipenv run ./run-tests.sh
