import io
import sys
import math
import scipy.stats
import numpy as np
from sklearn.linear_model import LinearRegression

from git import Repo


def manual_linear_regression(X, Y):
    """
        Calculates best fit given vectors X and Y
        using numpy (manually)
    """
    sumX = X.sum()
    sumXsquare = (X ** 2).sum()
    sumY = Y.sum()
    sumXY = (X * Y).sum()
    n = X.size

    # Matrices for linear equation AX = B
    A = np.array([[sumXsquare, sumX],
                  [sumX, n]])
    B = np.array([sumXY, sumY])

    # Solving lineal equation (roots)
    coefficients = np.linalg.solve(A, B)

    slope = round(coefficients[0], 2)
    intercept = round(coefficients[1], 2)

    return slope, intercept


def scipy_linear_regression(X, Y):
    """
        linear regression using scipy utils
    """
    return scipy.stats.linregress(X, Y)


def prediction(m, b, x):
    """
    makes a prediction using a linear model
    given slope (m) and intercept(b)
    """
    return round(m * x + b, 2)


def example():
    X = np.array([1, 2, 3, 4, 5, 6])
    Y = np.array([10, 20, 30, 40, 50, 60])

    # solving Manually using NumPy
    slope, intercept = manual_linear_regression(X, Y)
    print(f'slope {slope}, intercept {intercept}')
    x = 0
    print(f'f({x})={x * slope + intercept}')
    x = 120
    print(f'f({x})={x * slope + intercept}')
    x = -50
    print(f'f({x})={x * slope + intercept}')

    # solving using SciPy linear Regression
    BestLine = scipy_linear_regression(X, Y)

    print(f'\nslope {BestLine.slope} ,intercept {BestLine.intercept}, R value {BestLine.rvalue}')
    x = 0
    print(f'f({x})={prediction(BestLine.slope, BestLine.intercept, x)}')
    x = 120
    print(f'f({x})={prediction(BestLine.slope, BestLine.intercept, x)}')
    x = -50
    print(f'f({x})={prediction(BestLine.slope, BestLine.intercept, x)}')
    return BestLine.slope, BestLine.intercept, BestLine.rvalue


def my_regression(X, Y):
    model = LinearRegression().fit(X, Y)
    return model.coef_, model.intercept_


if __name__ == "__main__":
    repo = Repo(".")

    # just a little info on repository
    print(f'my repo working dir: {repo.working_dir}')

    # dummy example 
    example()

    # input data for making your own linear model
    X = np.array(
        [65.2, 21.9, -14.1, 29.6, 2.1, 64.5, 5.5, 36.7, 43.0, 6.2, 21.6, -1.7, -12.1, 22.8, 41.7, 68.3, 64.2, 53.0,
         62.8, -14.5])
    Y = np.array(
        [-48.2, 53.9, 86.1, 15.1, 68.3, -41.7, 80.8, 2.6, 1.8, 73.0, 53.0, 49.3, 77.7, 27.7, 9.5, -37.5, -30.5, -37.1,
         -28.8, 67.2])

    my_regression([X], [Y])

    # Add code and print the results to the console

    # Predict the values for
    # x=-25.3
    # x=310

    # What is the error for x=64.4?
    # Error =  (actual value - predicted value)/actual value
