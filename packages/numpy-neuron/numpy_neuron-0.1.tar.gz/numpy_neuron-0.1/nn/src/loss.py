from abc import ABC, abstractmethod
from nn.activation import SoftMax
import numpy as np


class Loss(ABC):
    @abstractmethod
    def forward(self, y_hat: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def backward(self, y_hat: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        pass


class LogitsLoss(Loss):
    pass


class MSE(Loss):
    def forward(self, y_hat: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        return np.sum(np.square(y_hat - y_true)) / y_true.shape[0]

    def backward(self, y_hat: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        return (y_hat - y_true) * (2 / y_true.shape[0])


class CrossEntropy(Loss):
    def forward(self, y_hat: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        y_hat = np.asarray(y_hat)
        y_true = np.asarray(y_true)
        m = y_true.shape[0]
        p = self._softmax(y_hat)
        eps = 1e-15  # to prevent log(0)
        log_likelihood = -np.log(
            np.clip(p[range(m), y_true.argmax(axis=1)], a_min=eps, a_max=None)
        )
        loss = np.sum(log_likelihood) / m
        return loss

    def backward(self, y_hat: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        y_hat = np.asarray(y_hat)
        y_true = np.asarray(y_true)
        grad = y_hat - y_true
        return grad / y_true.shape[0]

    @staticmethod
    def _softmax(X: np.ndarray) -> np.ndarray:
        return SoftMax().forward(X)


class CrossEntropyWithLogits(LogitsLoss):
    def forward(self, y_hat: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        # Apply the log-sum-exp trick for numerical stability
        max_logits = np.max(y_hat, axis=1, keepdims=True)
        log_sum_exp = np.log(np.sum(np.exp(y_hat - max_logits), axis=1, keepdims=True))
        log_probs = y_hat - max_logits - log_sum_exp
        # Select the log probability of the true class
        loss = -np.sum(log_probs * y_true) / y_true.shape[0]
        return loss

    def backward(self, y_hat: np.ndarray, y_true: np.ndarray) -> np.ndarray:
        # Compute softmax probabilities
        exps = np.exp(y_hat - np.max(y_hat, axis=1, keepdims=True))
        probs = exps / np.sum(exps, axis=1, keepdims=True)
        # Subtract the one-hot encoded labels from the probabilities
        grad = (probs - y_true) / y_true.shape[0]
        return grad


LOSSES: dict[str, Loss] = {
    "MSE": MSE(),
    "CrossEntropy": CrossEntropy(),
    "CrossEntropyWithLogitsLoss": CrossEntropyWithLogits(),
}
