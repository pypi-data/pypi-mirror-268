:eyeglasses: :eyeglasses: :eyeglasses:
# quantile-glasses
A simple python package to correct the issue of quantile crossing in probabilistic forecasting. Kind of like wearing glasses if you can't see well!

The `LinearQuantileGlasses` class allows you to correct your probabilistic forecast and remove quantile crossing.
It works by applying linear optimization, imposing a constraint that quantile crossing does not happen while minimizing [pinball loss](https://www.lokad.com/pinball-loss-function-definition/) on the training set. 

### Installation
Just run 
```bash
pip install quantile-glasses
```
You might encounter a few difficulties installing dependencies for `cvxpy`. If that happens to be the case, install `cvxpy` without dependencies first by running:
```bash
pip install cvxpy --no-deps
```
You can then selectively install the dependencies for that package one at a time. Note that `cvxpy` can work without most dependencies as long as you select a solver that you have installed. See the getting started guide below for an example.

### Getting started
```python
import pandas as pd
import numpy as np
from quantile_glasses import LinearQuantileGlasses

# simulate an independent and dependent variable for a regression problem
x = pd.Series(np.sin(np.linspace(0, 4 * np.pi, 1100)))
y = 5 * x + np.random.randn(len(x))

# define quantiles
quantiles = np.linspace(0.05, 0.95, 5)

# create a simple quantile forecast by binning the data
y_quant = pd.DataFrame(
    {
        q: y.groupby(pd.cut(x, 10), observed=True).transform(lambda x: x.quantile(q))
        for q in quantiles
    }
)

# split data
x_train, x_test = y_quant.iloc[:1000].copy(), y_quant.iloc[-100:].copy()
y_train, y_test = y.iloc[:1000].copy(), y.iloc[-100:].copy()

# artificially switch around the order of some quantiles
quant_switch = x_test.sample(10).index
for i in quant_switch:
    x_test.loc[i] = x_test.loc[i].sort_values(ascending=False).values

# apply correction to prediction
qlg = LinearQuantileGlasses()
y_quant_corr = qlg.fit_predict(x_train, y_train, x_test, solver="CLARABEL")

print("Pinball loss with quantile crossing", qlg.pinball_loss(x_test, y_test).mean())
print(
    "Pinball loss without quantile crossing",
    qlg.pinball_loss(y_quant_corr, y_test).mean(),
)
```
