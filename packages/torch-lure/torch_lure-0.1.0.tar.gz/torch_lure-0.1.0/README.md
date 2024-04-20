# Torch Lure


<a href="https://www.youtube.com/watch?v=wCzCOYCfY9g" target="_blank">
  <img src="http://img.youtube.com/vi/wCzCOYCfY9g/maxresdefault.jpg" alt="Chandelure" style="width: 100%;">
</a>


```sh
pip install torch-lure
```


# Usage
```py
import torch_lure as lure


# Optimizers
lure.SophiaG(lr=1e-3, weight_decay=0.2)

# Functions
lure.tanh_exp(x)
lure.TanhExp()

lure.quantile_loss(y_pred, y_target, quantile=0.5)
lure.QuantileLoss(quantile=0.5)
```