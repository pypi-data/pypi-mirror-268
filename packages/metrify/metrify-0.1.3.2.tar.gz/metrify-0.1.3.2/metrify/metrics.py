from typing import Tuple

import numpy as np
from sklearn.metrics import precision_recall_curve


def confusion_matrix(t: np.array, p: np.array) -> tuple:
    """The confusion_matrix function computes the confusion matrix for a binary classification problem.
       It takes two input arrays t and p, which represent the true labels and predicted labels respectively.
       The function calculates the number of true positives (TP), true negatives (TN), false positives (FP),
       and false negatives (FN) by comparing the elements of t and p.
       It then returns these values as a tuple.

    Returns:
        tuple: tuple ordered as (TP, TN, FP, FN)
    """

    # Check content
    # Raise error if not 1D numpy arrays
    if t.ndim != 1 or p.ndim != 1:
        raise ValueError("Input arrays must be 1D numpy arrays.")
    # Raise error if different length
    if len(t) != len(p):
        raise ValueError("Input arrays must have the same length.")

    # Compute the confusion matrix
    TP = np.sum((p == 1) & (t == 1))
    TN = np.sum((p == 0) & (t == 0))
    FP = np.sum((p == 1) & (t == 0))
    FN = np.sum((p == 0) & (t == 1))

    return TP, TN, FP, FN


def informedness(t: np.array, p: np.array) -> float:
    """Compute the informedness metric for a binary classification problem."""

    # Compute the confusion matrix
    TP, TN, FP, FN = confusion_matrix(t, p)

    return TP / (TP + FN) - FP / (TN + FP)


def markedness(t: np.array, p: np.array) -> float:
    """Compute the markedness metric for a binary classification problem."""

    # Compute the confusion matrix
    TP, TN, FP, FN = confusion_matrix(t, p)

    return TP / (TP + FP) - FN / (TN + FN)


def phi_beta(t: np.array, p: np.array, beta: float) -> float:
    """Compute the phi_beta metric for a binary classification problem."""

    i = informedness(t, p)
    m = markedness(t, p)

    return (1 + beta**2) * i * m / (beta**2 * m + i)


def phi(t: np.array, p: np.array) -> float:
    """Compute the phi metric as special case of beta=1
    of phi_bea metric for a binary classification problem."""

    return phi_beta(t, p, 1)


def find_best_fbeta(t: np.array, p: np.array, beta: float) -> Tuple[float, float]:
    """
    Given a binary ground truth t and a set of predictions p (these are probabilities)
    and a value for beta, return the best fbeta score and the corresponding threshold
    """

    # Get precisions, recalls and thresholds (shape for each of these (N, ))
    precisions, recalls, thresholds = precision_recall_curve(t, p)

    # Compute all the fbeta scores
    fbetas = (1 + beta**2) * (precisions * recalls) / (beta**2 * precisions + recalls)

    # Find the highest beta score and its position *exlcuding nans*
    max_fbeta = np.nanmax(fbetas)
    position = np.nanargmax(fbetas)

    # Return the best fbeta score and the corresponding threshold
    return max_fbeta, thresholds[position]
