import numpy as np
from abc import abstractmethod, ABC


class Activation(ABC):
    @abstractmethod
    def forward(self, X: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def backward(self, X: np.ndarray) -> np.ndarray:
        pass


class Relu(Activation):
    def forward(self, X: np.ndarray) -> np.ndarray:
        return np.maximum(0, X)

    def backward(self, X: np.ndarray) -> np.ndarray:
        return np.where(X > 0, 1, 0)


class TanH(Activation):
    def forward(self, X: np.ndarray) -> np.ndarray:
        return np.tanh(X)

    def backward(self, X: np.ndarray) -> np.ndarray:
        return 1 - self.forward(X) ** 2


class Sigmoid(Activation):
    def forward(self, X: np.ndarray) -> np.ndarray:
        return 1.0 / (1.0 + np.exp(-X))

    def backward(self, X: np.ndarray) -> np.ndarray:
        s = self.forward(X)
        return s - (1 - s)


class SoftMax(Activation):
    def forward(self, X: np.ndarray) -> np.ndarray:
        exps = np.exp(
            X - np.max(X, axis=1, keepdims=True)
        )  # Avoid numerical instability
        return exps / np.sum(exps, axis=1, keepdims=True)

    def backward(self, X: np.ndarray) -> np.ndarray:
        return X


ACTIVATIONS: dict[str, Activation] = {
    "Relu": Relu(),
    "Sigmoid": Sigmoid(),
    "TanH": TanH(),
    "SoftMax": SoftMax(),
}
