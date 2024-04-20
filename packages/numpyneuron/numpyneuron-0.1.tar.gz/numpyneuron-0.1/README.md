---
title: Numpy-Neuron
emoji: 🔙
colorFrom: yellow
colorTo: blue
sdk: gradio
sdk_version: 4.26.0
app_file: gradio_app.py
pinned: false
license: mit
---


# Numpy-Neuron

A small, simple neural network framework built using only [numpy](https://numpy.org) and python (duh). Check it out on [PyPI](https://pypi.org/project/numpy-neuron/)

## Install

`pip install numpy-neuron`


## Example

```py
from sklearn import datasets
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
import numpy as np
from nn import (
    NN,
    Relu,
    Sigmoid,
    CrossEntropyWithLogits,
)


RANDOM_SEED = 2


def _preprocess_digits(
    seed: int,
) -> tuple[np.ndarray, ...]:
    digits = datasets.load_digits(as_frame=False)
    n_samples = len(digits.images)
    data = digits.images.reshape((n_samples, -1))
    y = OneHotEncoder().fit_transform(digits.target.reshape(-1, 1)).toarray()
    X_train, X_test, y_train, y_test = train_test_split(
        data,
        y,
        test_size=0.2,
        random_state=seed,
    )
    return X_train, X_test, y_train, y_test


def train_nn_classifier() -> None:
    X_train, X_test, y_train, y_test = _preprocess_digits(seed=RANDOM_SEED)

    nn_classifier = NN(
        epochs=2_000,
        hidden_size=16,
        batch_size=1,
        learning_rate=0.01,
        loss_fn=CrossEntropyWithLogits(),
        hidden_activation_fn=Relu(),
        output_activation_fn=Sigmoid(),
        input_size=64,  # 8x8 pixel grid images
        output_size=10,  # digits 0-9
        seed=2,
    )

    nn_classifier.train(
        X_train=X_train,
        y_train=y_train,
    )

    pred = nn_classifier.predict(X_test=X_test)

    pred = np.argmax(pred, axis=1)
    y_test = np.argmax(y_test, axis=1)

    accuracy = accuracy_score(y_true=y_test, y_pred=pred)

    print(f"accuracy on validation set: {accuracy:.4f}")


if __name__ == "__main__":
    train_nn_classifier()
```


## Roadmap

**Optimizers**
I would love to add the ability to modify the learning rate over each epoch to ensure
that the gradient descent algorithm does not get stuck in local minima as easily.


## Gradio app demo development notes

The remote added to this repo so that it runs on hugging face spaces
`git remote add space git@hf.co:spaces/Jensen-holm/Numpy-Neuron` 

The command to force push to that space
`git push --force space main`
