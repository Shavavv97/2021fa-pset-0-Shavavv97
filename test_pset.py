#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pset_1` package."""

import os
from pathlib import Path
from unittest import TestCase

# Import module
import submit

class FakeFileFailure(IOError):
    pass

class psetTest(TestCase):
    def test_prediction(self):

        expected_value = 2
        actual_value = submit.prediction(1,1,1)
        self.assertEqual(expected_value, actual_value)