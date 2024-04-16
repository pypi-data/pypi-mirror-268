import pytest
import numpy as np
import pandas as pd
from quantile_glasses import LinearQuantileGlasses
from quantile_glasses.exceptions import SolverError


@pytest.fixture
def data():
    x = pd.Series(np.sin(np.linspace(0, 4 * np.pi, 1100)))
    y = 5 * x + np.random.randn(len(x))

    quantiles = np.linspace(0.05, 0.95, 5)
    y_quant = pd.DataFrame(
        {
            q: y.groupby(pd.cut(x, 10), observed=True).transform(
                lambda x: x.quantile(q)
            )
            for q in quantiles
        }
    )
    x_train, y_train = y_quant.iloc[:1000].copy(), y.iloc[:1000].copy()
    x_pred = y_quant.iloc[-100:].copy()
    quant_switch = x_pred.sample(10).index
    for i in quant_switch:
        x_pred.loc[i] = x_pred.loc[i].sort_values(ascending=False).values

    return x_train, y_train, x_pred


@pytest.mark.parametrize(
    "fit_intercept,fit_slope", [(True, True), (True, False), (False, True)]
)
def test_linear_quantile_glasses(fit_intercept, fit_slope, data):
    x_train, y_train, x_pred = data

    qlg = LinearQuantileGlasses(fit_intercept=fit_intercept, fit_slope=fit_slope)
    try:
        y_quant_corr = qlg.fit_predict(x_train, y_train, x_pred, solver="CLARABEL")
        assert (y_quant_corr.diff(axis=1).iloc[:, 1:].round(4) >= 0).mean().all()
    except SolverError as e:
        # if we failed because of infeasibility this needs to be the message
        assert e.args[0] == "Problem status is infeasible"
