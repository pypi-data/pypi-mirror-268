from warnings import warn
from quantile_glasses.exceptions import SolverError

import cvxpy as cp
import numpy as np
import pandas as pd


class LinearQuantileGlasses:
    """
    Class for applying linear optimization to correct quantile crossing.
    Fits a linear (degree 1) model to guarantee absence of quantile crossing in the
    prediction while minimizing pinball loss on the training data.
    """

    def __init__(self, fit_intercept: bool = True, fit_slope: bool = True):
        """Initializes class

        :param fit_intercept: whether to fit an intercept to the data, defaults to True
        :param fit_slope: whether to fit a slope to the data, defaults to True
        """
        self.fit_intercept = fit_intercept
        self.fit_slope = fit_slope

    def _get_vars(self, quantiles: list) -> tuple[cp.Variable]:
        """Creates cvxpy variables

        :param quantiles: list of quantiles from the prediction
        :return: slope and intercept variables
        """
        slope = cp.Variable(shape=(1, len(quantiles)), name="slope")
        intercept = cp.Variable(shape=(1, len(quantiles)), name="intercept")
        return slope, intercept

    def _get_constraints(
        self,
        y_pred: cp.Expression,
        X_pred: pd.DataFrame | np.ndarray,
        enforce_bounds: bool,
    ) -> list[cp.Constraint]:
        """Creates cvxpy constraints

        :param y_pred: cvxpy expression for the corrected forecast
        :param X_pred: raw prediction before the correction
        :param enforce_bounds: whether to constrain the corrected prediction to have the same
            max and min values as the raw one
        :return: _description_
        """
        no_quantile_crossing = y_pred[:, 1:] >= y_pred[:, :-1]
        constraints = [no_quantile_crossing]
        if enforce_bounds:
            same_upper_bound = y_pred.max(axis=0) <= X_pred.max()
            same_lower_bound = y_pred.min(axis=0) >= X_pred.min()
            constraints += [same_upper_bound, same_lower_bound]
        return constraints

    def _get_obj_fun(
        self,
        y_train: pd.Series | pd.DataFrame | np.ndarray,
        y_pred_train: cp.Expression,
        slope: cp.Variable,
        intercept: cp.Variable,
        weights: np.ndarray,
        lambda_l1: float,
    ) -> cp.Expression:
        """Builds objective function (pinball loss)

        :param y_train: training data for target
        :param y_pred_train: raw prediction data for the training set
        :param slope: variable for slope
        :param intercept: variable for intercept
        :param weights: vector with weights to assign to training set
        :param lambda_l1: regularization factor
        :return: cvxpy objective function
        """
        r = y_train.values.reshape(-1, 1) - y_pred_train
        if weights is not None:
            # ensure weights sum to 1
            weights = weights / weights.sum()
            r = cp.multiply(r, weights.reshape(-1, 1))

        q_loss = 0.5 * cp.abs(r) + cp.multiply(np.array([self.quantiles]) - 0.5, r)
        abs_weight = (cp.abs(slope) + cp.abs(intercept)).sum()

        obj = q_loss.sum()
        if lambda_l1 != 0:
            obj += lambda_l1 * abs_weight
        return obj

    def fit_predict(
        self,
        X_train: pd.DataFrame | np.ndarray,
        y_train: pd.Series | pd.DataFrame | np.ndarray,
        X_pred: pd.DataFrame | np.ndarray,
        weights: np.ndarray = None,
        enforce_bounds: bool = True,
        lambda_l1: float = 0,
        **solve_kwargs,
    ) -> np.ndarray | pd.DataFrame:
        """Fits model and corrects prediction to avoid quantile crossing

        :param X_train: raw prediction before correction for training set
        :param y_train: training data for target
        :param X_pred: raw prediction before correction
        :param weights: vector of weights to apply to training samples,
            e.g. to give more weight to recent samples, defaults to None
        :param enforce_bounds: whether to constrain the corrected prediction to have the same
            max and min values as the raw one
        :param lambda_l1: regularization factor for l1 regularization.
            If 0, no regularization is applied. If non-zero, the sum of the absolute value
            of slope and intercept is added to the objective function
        :return: corrected prediction
        """

        if isinstance(X_train, pd.DataFrame):
            as_df = True
            self.quantiles = X_train.columns.values
        else:
            as_df = False
            self.quantiles = np.linspace(0, 1, X_train.shape[1])

        if self.quantiles.max() > 1:
            warn(
                UserWarning(
                    "Looks like quantiles are (0,100) instead of (0,1). Will divide by 100"
                )
            )
            self.quantiles /= 100

        # define cvxpy problem
        self.slope, self.intercept = self._get_vars(self.quantiles)

        # corrected quantile forecasts
        y_pred_train = (
            cp.multiply(X_train.values, self.slope if self.fit_slope else 1)
        ) + (self.intercept if self.fit_intercept else 0)
        y_pred = cp.multiply(X_pred.values, self.slope if self.fit_slope else 1) + (
            self.intercept if self.fit_intercept else 0
        )

        # objective function
        obj = self._get_obj_fun(
            y_train, y_pred_train, self.slope, self.intercept, weights, lambda_l1
        )
        # constraints
        constraints = self._get_constraints(y_pred, X_pred, enforce_bounds)
        # make and solve problem
        prob = cp.Problem(cp.Minimize(obj), constraints)
        prob.solve(**solve_kwargs)
        if prob.status != "optimal":
            raise SolverError(f"Problem status is {prob.status}")

        if as_df:
            y_pred = pd.DataFrame(
                y_pred.value, index=X_pred.index, columns=X_pred.columns
            )
        else:
            y_pred = y_pred.value

        return y_pred

    def pinball_loss(self, y_pred: pd.DataFrame, y_true: pd.Series) -> float:
        """Computes pinball loss

        :param y_pred: probabilistic prediction (columns are quantiles)
        :param y_true: target values
        :return: loss value
        """
        quantiles = y_pred.columns
        r = y_pred.sub(y_true, axis=0)
        loss = 0.5 * r.abs() + r.mul(quantiles - 0.5, axis=1)
        return loss.mean()
