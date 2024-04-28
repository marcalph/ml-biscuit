#!/usr/bin/env python3
# coding: utf-8
##########################################
# authors                                #
# marcalph - https://github.com/marcalph #
##########################################
""" basic predictor classe
"""

from abc import ABC, abstractmethod

import numpy as np
import numpy.typing as npt


class BasePredictor(ABC):
    @abstractmethod
    def fit(self, X: npt.NDArray[np.float32], y: npt.NDArray[np.float32]) -> None:
        """Fits the classifier to the training data.
        args
        ----
            X `array-like`: The training input samples.
            y `array-like`: The target values.
        returns
        -------
            self: The fitted classifier.
        """
        pass

    @abstractmethod
    def predict(self, X: npt.NDArray[np.float32]) -> None:
        """Runs inference
        args
        ----
            X : `array-like, sparse matrix` of shape (n_samples, n_features)
        returns
        -------
            y_pred : ndarray of shape (n_samples,)
        """
        pass

    @abstractmethod
    def quantize(self) -> None:
        """Apply post training quantization"""
        pass
