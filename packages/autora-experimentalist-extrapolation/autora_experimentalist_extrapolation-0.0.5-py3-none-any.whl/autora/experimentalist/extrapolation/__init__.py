"""
Example Experimentalist
"""
import copy
import random as _random
from typing import Literal, Union

import numpy as np
import pandas as pd
from sklearn.metrics import DistanceMetric

from autora.variable import VariableCollection

AllowedMetrics = Literal[
    "euclidean",
    "manhattan",
    "chebyshev",
    "minkowski",
    "wminkowski",
    "seuclidean",
    "mahalanobis",
    "haversine",
    "hamming",
    "canberra",
    "braycurtis",
    "matching",
    "jaccard",
    "dice",
    "kulsinski",
    "rogerstanimoto",
    "russellrao",
    "sokalmichener",
    "sokalsneath",
    "yule",
]

AllowedEstimationMethods = Literal[
    "mean",
    "median",
]


def sample(
    conditions: pd.DataFrame,
    experiment_data: pd.DataFrame,
    variables: VariableCollection,
    models,
    num_samples=1,
    threshold_y=0.001,
    threshold_x=0.001,
    metric: AllowedMetrics = "euclidean",
    estimation_method: Union[AllowedEstimationMethods, None] = "mean",
    check_influence=True,
    seed=None,
):
    """

    Args:
        conditions: The pool to sample from.
            Attention: `conditions` is a field of the standard state
        experiment_data: The data that has already been collected
            Attention: `conditions` is a field of the standard state
        variables: The variable definitions used in the experiment
            Attention: `conditions` is a field of the standard state
        models: The models used to predict data on novel conditions
            Attention: `conditions` is a field of the standard state
        num_samples: Number of experimental conditions to select
        threshold_y: A threshold bellow that distances are considered equal for y values
        threshold_x: A threshold bellow that distances are considered equal for x values
        metric: distance measure. Options: 'euclidean', 'manhattan', 'chebyshev',
            'minkowski', 'wminkowski', 'seuclidean', 'mahalanobis', 'haversine',
            'hamming', 'canberra', 'braycurtis', 'matching', 'jaccard', 'dice',
            'kulsinski', 'rogerstanimoto', 'russellrao', 'sokalmichener',
            'sokalsneath', 'yule'.
        estimation_method: The method to estimate the value if conditions occure
            multiple times in the experiment_data
        check_influence: Test if features of conditions are infleuncial in the prediction, if
            not randomize them
        seed: A random seed that makes results reproducible

    Returns:
        Sampled pool of experimental conditions

    Examples:
        First, we describe an experiment with one independent and one dependent variable:
        >>> from autora.variable import Variable
        >>> x = Variable(name='x', value_range=(0, 1),allowed_values=np.linspace(0, 1, 100))
        >>> y = Variable(name='y', value_range=(0, 1),allowed_values=np.linspace(0, 1, 100))
        >>> v = VariableCollection(independent_variables=[x],dependent_variables=[y])

        Then, we descibe a model. It is an object that needs a predict method to predict the
        dependent variable on independent variables. First, we use a model that predicts a
        constant value of .5
        >>> class ConstantModel:
        ...     def predict(self, x):
        ...         return np.array([.5] * len(x))
        >>> constantModel = ConstantModel()

        We can test the model:
        >>> constantModel.predict([.1, .2, .5])
        array([0.5, 0.5, 0.5])

        Now, let's assume we already observed data for x=.5 and x=.2
        >>> e_d = pd.DataFrame({'x':[.5, .2], 'y': [0, .5]})
        >>> e_d
             x    y
        0  0.5  0.0
        1  0.2  0.5

        And we want to choose which conditions it more interesting to observe next: x=.1 or x =.6 ?
        >>> c = pd.DataFrame({'x':[.1, .6]})
        >>> c
             x
        0  0.1
        1  0.6

        >>> sample(conditions=c, experiment_data=e_d, variables=v, models=[constantModel])
             x
        0  0.6

        x=.6 is the more intersting condition since the model makes the prediction of .5 on it. But
        right next to x=.6, we already observed the y-value for y(.5) = 0. This means the model
        assumes a large difference between the conditions .5 and .6 that we want to test. On the
        other hand the condition .1 is not as interesting to observe, since right next to it, we
        already observed a y-value for y(.2) = .5 that is very near to the predicted value for .1
        which is also .5.

        As a next test, we want to see which condition is more interesting to probe next:
        x=.6 or x=.7
        >>> c = pd.DataFrame({'x':[.6, .7]})
        >>> sample(conditions=c, experiment_data=e_d, variables=v, models=[constantModel])
             x
        0  0.6

        Again, the condition .6 is more interesting, since it is nearer to the already observed
        value for y(.5). The model predicts a large jump from .5 to .6 while this jump is a bit
        lower for .5 to .7. Allthough the difference in y is the same, the distance in x is higher.
        In other words: The predicted slope between .5 and .6 is higher than between .5 and .7.

        Now, let's see if .1 or 0. is more interesting:
        >>> c = pd.DataFrame({'x':[.1, 0.]})
        >>> sample(conditions=c, experiment_data=e_d, variables=v, models=[constantModel])
             x
        0  0.0

        In this situation, the more far conditon from .2 is more interesting since both the model
        predicts the same value for both but the .0 is farer away.

    """
    _random.seed(seed)
    ivs = [iv.name for iv in variables.independent_variables]
    dvs = [dv.name for dv in variables.dependent_variables]

    # estimate value if conditions where sampled multiple times
    if not estimation_method:
        _e_data = experiment_data.copy()
    elif estimation_method == "mean":
        _e_data = experiment_data.groupby(ivs, as_index=False).mean()
    elif estimation_method == "median":
        _e_data = experiment_data.groupby(ivs, as_index=False).median()

    _c = np.array(conditions)
    _r = np.array(_e_data[ivs])

    dist = DistanceMetric.get_metric(metric)
    distances = dist.pairwise(_c, _r)

    # distances = _distances(_c, _r)
    closest_b_for_each_a = np.argmin(distances, axis=1)

    _y_c = models[-1].predict(_c)

    # Populate the dictionary with vectors from 'a' based on their closest vector in 'b'
    _a = []
    for idx, a_vector in enumerate(_c):
        b_index = closest_b_for_each_a[idx]
        x_r = _r[b_index]
        y_r = np.array(_e_data[dvs])[b_index]

        x_c = a_vector
        y_c = _y_c[idx]

        if (
            np.isnan(y_r).any()
            or np.isnan(y_c).any()
            or np.isinf(y_r).any()
            or np.isinf(y_c).any()
        ):
            d_y = 0
        else:
            d_y = dist.pairwise([y_r], [[y_c]])[0]
            if d_y < threshold_y:
                d_y = 0
        d_x = dist.pairwise([x_r], [x_c])[0]
        if d_x < threshold_x:
            d_x = 0

        score_1 = 0
        if d_y != 0 and d_x != 0:
            score_1 = d_y / d_x

        score_2 = 0
        if d_y == 0:
            score_2 = d_x
        if d_x == 0:
            score_2 = d_y

        _a.append([a_vector, score_1, score_2, _random.random()])

    _sorted_a = sorted(_a, key=lambda x: (x[1], x[2], x[3]), reverse=True)

    a_np = np.array([x[0] for x in _sorted_a])

    n_features = _c.shape[1]

    # Initialize a list to store the influence of each feature
    feature_influence = []

    for i in range(n_features):
        # Create a copy of the original data
        modified_c = copy.deepcopy(_c)
        # Set the i-th feature to zero
        modified_c[:, i] = 0
        # Predict with the modified data
        modified_predictions = models[-1].predict(modified_c)
        # Check if predictions change
        if np.array_equal(_y_c, modified_predictions):
            feature_influence.append(False)
        else:
            feature_influence.append(True)

    if any(feature_influence) and not all(feature_influence) and check_influence:
        a_np = _replace_with_conditional_matching(_c, a_np, np.array(feature_influence))

    new_conditions = pd.DataFrame(a_np, columns=conditions.columns)

    return new_conditions[:num_samples]


def _replace_with_conditional_matching(pool, target, mask):
    # For each entry in the target array
    for idx, entry in enumerate(target):
        # Start with a full pool and filter down based on mask
        filtered_pool = pool
        for i, should_match in enumerate(mask):
            if should_match:  # Apply filter only where mask is True
                filtered_pool = filtered_pool[filtered_pool[:, i] == entry[i]]

        # If there are matching entries, replace the target entry with a random one from the matches
        if len(filtered_pool) > 0:
            target[idx] = filtered_pool[np.random.randint(len(filtered_pool))]

    return target
