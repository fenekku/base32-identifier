# -*- coding: utf-8 -*-
#
# This file is part of base32-identifier
# Copyright (C) 2019 CERN.
# Copyright (C) 2019 Northwestern University,
#                    Galter Health Sciences Library & Learning Center.

# base32-identifier is free software; you can redistribute it and/or modify it
# under the terms of the MIT License; see LICENSE file for more details.

"""Small library to generate, encode and decode random base32 identifiers."""

from .base32 import decode, encode, generate

__all__ = ['decode', 'encode', 'generate']
