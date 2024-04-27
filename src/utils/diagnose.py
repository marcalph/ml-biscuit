#!/usr/bin/env python3
# coding: utf-8
##########################################
# authors                                #
# marcalph - https://github.com/marcalph #
##########################################
""" training  diagnostics
"""
from typing import Any, Callable, Union

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import pandas as pd
import seaborn as sns
import sklearn
from matplotlib.axes import Axes
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import BaseCrossValidator, learning_curve

from src.utils.log import logger, logthis

extra_args = {"funcname_override": "print"}

default_train_sizes = np.linspace(0.1, 1.0, 5)


@logthis
def plot_learning_curves(
    clf: sklearn.base.BaseEstimator,
    scoring: Callable[..., float],
    X: npt.NDArray[Any],
    y: npt.NDArray[Any],
    filename: str,
    cv: BaseCrossValidator,
    axes: Union[list[Axes], None] = None,
    n_jobs: Union[int, None] = None,
    train_sizes: npt.NDArray[Any] = default_train_sizes,
) -> None:
    """generate learning curves and scalability for a sklearn model"""
    if axes is None:
        _, axes = plt.subplots(1, 2, figsize=(10, 5))

    train_sizes, train_scores, test_scores, fit_times, _ = learning_curve(
        clf,
        X,
        y,
        cv=cv,
        n_jobs=n_jobs,
        train_sizes=train_sizes,
        scoring=scoring,
        return_times=True,
    )

    # learning curves
    sns.set_theme()
    sizes = np.tile(train_sizes, cv.n_splits)
    sizes.sort()
    df = pd.concat(
        [
            pd.DataFrame(
                {
                    "Sample size": sizes,
                    "Score": train_scores.reshape(-1),
                    "Set": "train",
                }
            ),
            pd.DataFrame(
                {"Sample size": sizes, "Score": test_scores.reshape(-1), "Set": "CV"}
            ),
        ]
    )
    sns.lineplot(
        data=df,
        x="Sample size",
        y="Score",
        hue="Set",
        errorbar=("ci", 95),
        marker="o",
        ax=axes[0],
    ).set_title("LC")

    # n_samples x fit_times
    sns.lineplot(
        data=pd.DataFrame(
            {"Sample size": sizes, "Fitting time": fit_times.reshape(-1)}
        ),
        x="Sample size",
        y="Fitting time",
        errorbar=("ci", 95),
        marker="o",
        ax=axes[1],
    ).set_title("Scalability")
    plt.savefig(filename)


@logthis
def cv_confusion_matrix(
    clf: sklearn.base.BaseEstimator,
    X: npt.NDArray[Any],
    y: npt.NDArray[Any],
    shuffle_split_strategy: BaseCrossValidator,
    filename: str,
    normalize: bool = False,
) -> None:
    """compute a cross validated confusion matrix for a bin target"""
    fig, ax = plt.subplots()
    cms = []
    labels = ["0", "1"]
    for train_idx, test_idx in shuffle_split_strategy.split(X, y):
        X_train, X_test = X[train_idx], X[test_idx]
        y_train, y_test = y[train_idx], y[test_idx]
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)
        cm = confusion_matrix(y_test, y_pred, labels=labels).T
        cms.append(cm)
    cmap = sns.diverging_palette(250, 30, as_cmap=True)
    agg_cm = np.mean(cms, axis=0)
    if normalize:
        cm_df = pd.DataFrame(
            agg_cm / agg_cm.sum(axis=1)[:, np.newaxis], index=labels, columns=labels
        )
        hm = sns.heatmap(
            cm_df,
            cmap=cmap,
            linewidth=0.5,
            annot=True,
            fmt=".1%",
            annot_kws={"size": 10},
            cbar=False,
        )
        hm.set_title("Confusion Matrix - normalised for Precision")
    else:
        cm_df = pd.DataFrame(agg_cm, index=labels, columns=labels)
        hm = sns.heatmap(
            cm_df.values,
            cmap=cmap,
            linewidth=0.5,
            annot=True,
            fmt=".0f",
            annot_kws={"size": 10},
            cbar=False,
        )
        hm.set_title("Confusion Matrix")

    hm.set_xlabel("True")
    hm.set_ylabel("Pred")
    plt.savefig(filename)


@logthis
def cv_classification_report() -> None:
    """generate a cross validated classification report"""
    pass
