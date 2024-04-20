import __local__
from luma.preprocessing.scaler import StandardScaler
from luma.preprocessing.encoder import OneHotEncoder
from luma.model_selection.split import TrainTestSplit, BatchGenerator
from luma.metric.classification import Accuracy

from luma.neural.layer import Sequential
from luma.neural.layer import Convolution, Pooling, Flatten, Dense
from luma.neural.loss import CategoricalCrossEntropy
from luma.neural.optimizer import AdamOptimizer

from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
import numpy as np


np.random.seed(42)

X, y = load_digits(return_X_y=True)

sc = StandardScaler()
X_sc = sc.fit_transform(X)

X_train, X_test, y_train, y_test = TrainTestSplit(
    X_sc, y, test_size=0.3, shuffle=True, stratify=True
).get

en = OneHotEncoder()
y_train = en.fit_transform(y_train.reshape(-1, 1))
y_test = en.fit_transform(y_test.reshape(-1, 1))

X_train = X_train.reshape(-1, 1, 8, 8)
X_test = X_test.reshape(-1, 1, 8, 8)

epochs = 100
batch_size = 100

model = Sequential(
    Convolution(6, 3, activation="relu"),
    Pooling(2, 2, mode="avg"),
    Flatten(),
    Dense(96, 10, activation="softmax"),
)
model.set_optimizer(AdamOptimizer(), learning_rate=0.001)
model.set_loss(CategoricalCrossEntropy())

losses = []
for i in range(1, epochs + 1):
    epoch_loss = []
    for j, (X_batch, y_batch) in enumerate(
        BatchGenerator(X_train, y_train, batch_size=batch_size), start=1
    ):
        loss = model(X_batch, y_batch, is_train=True)
        losses.append(loss)
        epoch_loss.append(loss)

    print(f"Epoch {i}/{epochs} - Avg. Loss: {np.average(epoch_loss)}")

print("\n" + repr(model))

score = Accuracy.score(
    y_true=y_test.argmax(axis=1), y_pred=model.forward(X_test).argmax(axis=1)
)

plt.plot(losses, lw=1, label=type(model.optimizer).__name__)
plt.xlabel("Total Batches")
plt.ylabel("Loss")
plt.title(f"CNN for load_digits dataset [Acc: {score:.4f}]")
plt.grid(alpha=0.2)

plt.legend(loc="upper right")
plt.tight_layout()
plt.show()
