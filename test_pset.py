#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pset_1` package."""

import os
from pathlib import Path
from unittest import TestCase

# Import module
import submit
import numpy as np
import scipy.stats
from sklearn.linear_model import LinearRegression


class FakeFileFailure(IOError):
    pass


class psetTest(TestCase):
    def test_manual_linear_regression(self):
        expected_slope, expected_intercept = 1.4, -15.54
        x = np.array([24, 63, -15])
        y = np.array([33, 65, -44])
        actual_slope, actual_intercept = submit.manual_linear_regression(x, y)
        self.assertEqual(expected_slope, actual_slope)
        self.assertEqual(expected_intercept, actual_intercept)

    def test_scipy_linear_regression(self):
        x = np.array([1, 2, 3])
        y = np.array([12, 24, 36])
        expected_value = scipy.stats.linregress(x, y)
        actual_value = submit.scipy_linear_regression(x, y)
        self.assertEqual(expected_value, actual_value)

    def test_prediction(self):
        expected_value = 2
        actual_value = submit.prediction(1, 1, 1)
        self.assertEqual(expected_value, actual_value)

    def test_example(self):
        expected_slope, expected_intercept, expected_rvalue = 10, 0, 1
        actual_slope, actual_intercept, actual_rvalue = submit.example()
        self.assertEqual(expected_slope, actual_slope)
        self.assertEqual(expected_intercept, actual_intercept)
        self.assertEqual(expected_rvalue, actual_rvalue)

    def test_my_regression(self):
        x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
        y = np.array([5, 20, 14, 32, 22, 38])
        model = LinearRegression().fit(x, y)
        expected_slope, expected_intercept = model.coef_, model.intercept_
        actual_slope, actual_intercept = submit.my_regression(x, y)
        self.assertEqual(expected_slope, actual_slope)
        self.assertEqual(expected_intercept, actual_intercept)