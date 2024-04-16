#!/usr/bin/env python
# coding: utf-8

import numpy as np
from ._probabilistic_model import ProbabilisticModel


class UniGauss(ProbabilisticModel):

    """
    This class implements the univariate Gaussians. With this implementation we are updating N univariate Gaussians
    in each iteration. When a dataset is given, each column is updated independently. The implementation involves a
    matrix with two rows, in which the first row are the means and the second one, are the standard deviations.
    """

    def __init__(self, variables: list, lower_bound: float):
        super().__init__(variables)

        self.pm = np.zeros((2, self.len_variables))
        self.lower_bound = lower_bound

        self.id = 1

    def sample(self, size: int) -> np.array:
        """
        Samples new solutions from the probabilistic model. In each solution, each variable is sampled
        from its respective normal distribution.

        :param size: number of samplings of the probabilistic model.
        :return: array with the dataset sampled
        :rtype: np.array
        """
        return np.random.normal(
            self.pm[0, :], self.pm[1, :], (size, self.len_variables)
        )

    def learn(self, dataset: np.array, *args, **kwargs):
        """
        Estimates the independent Gaussian for each variable.

        :param dataset: dataset from which learn the probabilistic model.
        """
        for i in range(len(self.variables)):
            self.pm[0, i] = np.mean(dataset[:, i])
            self.pm[1, i] = np.std(dataset[:, i])

            if self.pm[1, i] < self.lower_bound:
                self.pm[1, i] = self.lower_bound

    def print_structure(self) -> list:
        """
        Prints the arcs between the nodes that represent the variables in the dataset. This function
        must be used after the learning process. Univariate approaches generate no-edged graphs.

        :return: list of arcs between variables
        :rtype: list
        """
        return list()
