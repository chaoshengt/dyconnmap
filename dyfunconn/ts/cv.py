""" Coefficient of Variation


"""
# Author: Avraam Marimpis <avraam.marimpis@gmail.com>

import typing
import numpy as np


def cv(X: np.ndarray) -> float:
    """


    Parameters
    ----------
    X :


    Returns
    -------
    cv : float
        The computed coefficient of variation.
    """
    return np.std(X) / np.mean(X)
