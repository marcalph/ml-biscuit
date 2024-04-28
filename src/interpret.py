#!/usr/bin/env python3
# coding: utf-8
##########################################
# authors                                #
# marcalph - https://github.com/marcalph #
##########################################
""" interpretabilty utils
"""
from typing import Any, Iterable

import lime.lime_tabular  # type: ignore
import numpy.typing as npt

from src.utils.predictor import BasePredictor


def interpret_sample_lime(
    clf: BasePredictor,
    X: npt.NDArray[Any],
    y: npt.NDArray[Any],
    sample: npt.NDArray[Any],
    names: Iterable[str],
) -> Any:
    """linearly explain tabular prediction"""
    explainer = lime.lime_tabular.LimeTabularExplainer(
        X.astype(float).astype(int),
        mode="classification",
        training_labels=y,
        feature_names=names,
        class_names=[0, 1],
    )
    limexpl = explainer.explain_instance(
        sample.astype(float).astype(int).flatten(),
        clf.predict,
        num_features=10,
        num_samples=500,
    )
    return limexpl.as_html()
