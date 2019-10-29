# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015-2019 CERN.
# Copyright (C) 2019 Northwestern University.
#
# Invenio is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Provider tests."""

import pytest

from base32_identifier import base32


def test_basic_encode():
    assert base32.encode(32) == "10"
    assert base32.encode(1234) == "16j"


def test_basic_decode():
    assert base32.decode("16j") == 1234


def test_decode_normalizes_symbols():
    assert (
        base32.decode("abcdefghijklmnopqrstvwxyz") ==
        base32.decode("ABCDEFGHIJKLMNOPQRSTVWXYZ")
    )
    assert base32.decode('IL1O0ilo') == base32.decode('11100110')
    assert base32.decode('1-6-j') == base32.decode('16j')


def test_decode_raises_for_invalid_string():
    with pytest.raises(ValueError):
        base32.decode("Ü'+?")

    with pytest.raises(ValueError):
        base32.decode("IOU20D011ARS")


def test_decode_0_padded_equivalent_to_non_0_padded():
    assert base32.decode('016j') == base32.decode('16j')


def test_encode_hyphenates():
    assert base32.encode(1234, split_every=1) == "1-6-j"

    with pytest.raises(ValueError):
        assert base32.encode(1234, split_every=-1)


def test_encode_min_length():
    assert base32.encode(1234, min_length=4) == "016j"
    assert base32.encode(1234, min_length=2) == "16j"
    assert base32.encode(1234, min_length=0) == "16j"
    assert base32.encode(1234, min_length=-1) == "16j"


def test_encode_checksum():
    assert base32.encode(1234, checksum=True) == "16j82"


def test_decode_checksum():
    assert base32.decode("16j82", checksum=True) == 1234


def test_decode_invalid_checksum():
    with pytest.raises(ValueError):
        assert base32.decode("16j44", checksum=True)
