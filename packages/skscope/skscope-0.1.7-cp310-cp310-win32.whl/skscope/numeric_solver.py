#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Zezhi Wang
# Copyright (C) 2023 abess-team
# Licensed under the MIT License.

import numpy as np
import math
import nlopt
from scipy.optimize import minimize


def convex_solver_nlopt(
    objective_func,
    value_and_grad,
    init_params,
    optim_variable_set,
    data,
):
    """
    A wrapper of ``nlopt`` solver for convex optimization.

    Parameters
    ----------
    objective_func: callable
        The objective function.
        ``objective_func(params, data) -> loss``, where ``params`` is a 1-D array with shape (dimensionality,).
    value_and_grad: callable
        The function to compute the loss and gradient.
        ``value_and_grad(params, data) -> (loss, grad)``, where ``params`` is a 1-D array with shape (dimensionality,).
    init_params: array of shape (dimensionality,)
        The initial value of the parameters to be optimized.
    optim_variable_set: array of int
        The index of variables to be optimized, others are fixed to the initial value.
    data:
        The data passed to objective_func and value_and_grad.

    Returns
    -------
    loss: float
        The loss of the optimized parameters, i.e., `objective_func(params, data)`.
    optimized_params: array of shape (dimensionality,)
        The optimized parameters.
    """
    best_loss = math.inf
    best_params = None

    def cache_opt_fn(x, grad):
        nonlocal best_loss, best_params
        # update the nonlocal variable: params
        init_params[optim_variable_set] = x
        if grad.size > 0:
            loss, full_grad = value_and_grad(init_params, data)
            grad[:] = full_grad[optim_variable_set]
        else:
            loss = objective_func(init_params, data)
        if loss < best_loss:
            best_loss = loss
            best_params = np.copy(x)
        return loss

    nlopt_solver = nlopt.opt(nlopt.LD_LBFGS, optim_variable_set.size)
    nlopt_solver.set_min_objective(cache_opt_fn)

    try:
        init_params[optim_variable_set] = nlopt_solver.optimize(
            init_params[optim_variable_set]
        )
        return nlopt_solver.last_optimum_value(), init_params
    except RuntimeError:
        init_params[optim_variable_set] = best_params
        return best_loss, init_params


def convex_solver_BFGS(
    objective_func,
    value_and_grad,
    init_params,
    optim_variable_set,
    data,
):
    def fun(x):
        init_params[optim_variable_set] = x
        return objective_func(init_params, data)

    def jac(x):
        init_params[optim_variable_set] = x
        _, grad = value_and_grad(init_params, data)
        return grad[optim_variable_set]

    res = minimize(fun, init_params[optim_variable_set], method="BFGS", jac=jac)
    init_params[optim_variable_set] = res.x
    return res.fun, init_params
