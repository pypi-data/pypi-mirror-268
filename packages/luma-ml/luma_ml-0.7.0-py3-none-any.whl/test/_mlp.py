import __local__
from luma.preprocessing.scaler import StandardScaler
from luma.model_selection.split import TrainTestSplit
from luma.neural.network import MLPClassifier
from luma.neural.optimizer import *
from luma.visual.evaluation import ConfusionMatrix

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)

X, y = load_digits(return_X_y=True)

sc = StandardScaler()
X_std = sc.fit_transform(X)

X_train, X_test, y_train, y_test = TrainTestSplit(
    X_std, y, test_size=0.3, shuffle=True, stratify=True
).get

X_train, X_val, y_train, y_val = TrainTestSplit(
    X_train, y_train, test_size=0.2, shuffle=True, stratify=True
).get

X_all = np.vstack((X_train, X_val, X_test))
y_all = np.hstack((y_train, y_val, y_test))

optimizers = [
    SGDOptimizer,
    MomentumOptimizer,
    RMSPropOptimizer,
    AdamOptimizer,
    AdaGradOptimizer,
    AdaDeltaOptimizer,
    AdaMaxOptimizer,
    AdamWOptimizer,
    NAdamOptimizer,
]

param_dict = {
    "input_size": X.shape[1],
    "hidden_sizes": 100,
    "output_size": len(np.unique(y)),
    "max_epoch": 300,
    "batch_size": 100,
    "learning_rate": 0.001,
    "activation": "relu",
}

mlps = [MLPClassifier(**param_dict, optimizer=opt()) for opt in optimizers]

best_mlp = None
best_score = -np.inf

fig = plt.figure(figsize=(12, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

for mlp in mlps:
    mlp.fit(X_train, y_train)
    val_score = mlp.score(X_val, y_val)
    print(f"Done fitting for {type(mlp.optimizer).__name__}")

    if val_score > best_score:
        best_score = val_score
        best_mlp = mlp

    ax1.plot(
        mlp.batch_losses_, lw=0.5, label=f"{type(mlp.optimizer).__name__}", alpha=0.7
    )

print(f"Best optimizer: {type(best_mlp.optimizer).__name__}")

ax1.set_xlabel("Batches")
ax1.set_ylabel("Loss")
ax1.set_title(f"MLP for Various Optimizers [Best Acc: {best_score:.4f}]")
ax1.legend()
ax1.grid(alpha=0.2)

conf = ConfusionMatrix(y_all, best_mlp.predict(X_all))
conf.plot(ax=ax2, show=True)
