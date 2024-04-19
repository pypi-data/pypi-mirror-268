# metrify

## Installation

To install *metrify*, simply run `pip install metrify`. 

## Purpose

The purpose of *metrify* is to add a few simple functionalities to scikit-learn. In particular, the **informedness**, **markedness** and **$\phi_\beta$** scores are introduced. Furthermore, some other utilities related to more traditional metrics (e.g. $F_\beta$) are introduced, too. The reason for introducing them (and hence their utility) stems from the following observations.

The main issue with precision, recall and F-score is that none of them makes use of *True Negatives* (*TN*s) to assess the model performance. Whilst we are usually interested in the positive class, ensuring to get the negative class right is a sort of sanity check for our model. For example, if we had a highly imbalanced dataset (towards the negative class) we definitely want the negative class to be predicted with high confidence. Our job should be, in theory, to ensure that the model performs well on the minority, i.e. the positive, class.

In practice, suppose we have a model whose predictions yield, in terms of *False Positives*, *False Negatives* and *True Positives*
$$TP = 50, FP = 1000, FN = 10$$
Even though we can compute e.g. the F-score given this information, this metric totally neglects if we had, for example, $TN = 100000$ or $TN = 100$ which would indeed make a very big difference when assessing the model performance. This is a signal that we are not really capturing the information about the model. Whilst it is clear that the model is not satisfactory in either case, as we have an abundance of $FP$s, the latter situation is much more worrisome. In fact, although the negative class is the majority, we are basically getting it totally wrong by always predicting the positive one. This is likely indicating that our model has some inherent issue in its construction, e.g. setting a threshold too low or something similar. 

To make sure our metrics do take into consideration this case, we need an alternative to precision and recall. One option is to use **markedness** $M$ and **informedness** $I$. Formulas are the following:
$$M = \frac{TP}{TP +  FP} - \frac{FN}{TN+FN} \qquad I =  \frac{TP}{TP +  FN} - \frac{FP}{TN+FP}$$
Markedness plays the role of precision, and is informative about the role of $FP$s in our model. Conversely, Informedness plays the role of recall, and gauges the importance of $FN$s. However, in either case, the $TN$s **do enter** the game and help bring these metrics down. In fact, both of these are bounded between -1 and +1, with -1 corresponding to the worst scenario (no *TP*, and no *TN*). It is also possible to combine them into something reminiscent of F-score. I called it $\phi$-score. Similarly to the F-score, it can be weighted by a real parameter $\beta$, so as to give more or less importance to either $M$ or $I$. 
$$\phi_\beta = (1 + \beta^2) \frac{I \cdot M}{\beta^2 M + I}$$

## Usage

### Informedness, Markedness, $\phi$

Currently *metrify* only works for a binary classification problem. A sample usage is the following
```
from metrify import informedness, markedness, phi_beta

# Define a random numpy array of 100 true values
t = np.random.randint(0, 2, 100)

# Define a random numpy array of 100 predicted values
p = np.random.randint(0, 2, 100)

# Compute the metrics
i = informedness(t, p)
m = markedness(t, p)
phi_2 = phi_beta(t, p, beta=2)
```

### $F_\beta$

Given a set of binary ground truths and predictions as probabilities, find the best $F_\beta$ and corresponding threshold:
```
from metrify import find_best_fbeta

# Define a random numpy array of 100 true values
t = np.random.randint(0, 2, 100)

# Define a random numpy array of 100 predicted probabilities
p = np.random.rand(100)

# Get the best F0.5 and the corresponding threshold
f_beta, threshold = find_best_fbeta(t, p, beta=0.5)
```

## New Versions

To create and deploy a new version, the recipe is:

- Modify the code as suited;
- Update the version and possibly the dependencies in `pyproject.toml`;
- Build the package `python -m build`;
- Upload the package `python -m twine upload dist/metrify-<VERSION>*`