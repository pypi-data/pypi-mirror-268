from dataclasses import dataclass, field
from typing import Callable, Optional
import gradio as gr
import numpy as np
from tqdm import tqdm

from nn.activation import Activation
from nn.loss import Loss, LogitsLoss


DTYPE = np.float32


@dataclass
class NN:
    epochs: int
    learning_rate: float
    hidden_size: int
    input_size: int
    batch_size: float
    output_size: int
    hidden_activation_fn: Activation
    output_activation_fn: Activation
    loss_fn: Loss | LogitsLoss
    seed: int

    _gradio_app: bool = False
    _p_bar: Optional[tqdm | gr.Progress] = field(
        default_factory=lambda: None, init=False
    )
    _forward_fn: Optional[Callable] = field(default_factory=lambda: None, init=False)
    _loss_history: list = field(default_factory=lambda: [], init=False)
    _wo: np.ndarray = field(default_factory=lambda: np.ndarray([]), init=False)
    _wh: np.ndarray = field(default_factory=lambda: np.ndarray([]), init=False)
    _bo: np.ndarray = field(default_factory=lambda: np.ndarray([]), init=False)
    _bh: np.ndarray = field(default_factory=lambda: np.ndarray([]), init=False)

    def __post_init__(self) -> None:
        self._init_weights_and_biases()
        self._forward_fn, self._p_bar = self._pre_train()

        assert 0 < self.batch_size <= 1
        assert self._forward_fn is not None
        assert self._p_bar is not None

    def _pre_train(self) -> tuple[Callable, tqdm | gr.Progress]:
        def _get_forward_fn() -> Callable:
            if isinstance(self.loss_fn, LogitsLoss):
                return self._forward_logits
            return self._forward

        def _get_p_bar() -> tqdm | gr.Progress:
            if self._gradio_app:
                return gr.Progress().tqdm(range(self.epochs))
            return tqdm(range(self.epochs), unit="epoch", ascii=" >=")

        return (
            _get_forward_fn(),
            _get_p_bar(),
        )

    @classmethod
    def from_dict(cls, args: dict) -> "NN":
        return cls(**args)

    def _init_weights_and_biases(self) -> None:
        """
        NN._init_weights_and_biases(): Should only be ran once, right before training loop
            in order to initialize the weights and biases randomly.

        params:
            NN object with hidden layer size, output size, and input size
            defined.

        returns:
            self, modifies _bh, _bo, _wo, _wh NN attributes in place.
        """
        np.random.seed(self.seed)
        self._bh = np.zeros((1, self.hidden_size), dtype=DTYPE)
        self._bo = np.zeros((1, self.output_size), dtype=DTYPE)
        self._wh = np.asarray(
            np.random.randn(self.input_size, self.hidden_size)
            * np.sqrt(2 / self.input_size),
            dtype=DTYPE,
        )
        self._wo = np.asarray(
            np.random.randn(self.hidden_size, self.output_size)
            * np.sqrt(2 / self.hidden_size),
            dtype=DTYPE,
        )

    def _forward(self, X_train: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        hidden_layer_output = self.hidden_activation_fn.forward(
            np.dot(X_train, self._wh) + self._bh
        )

        # Compute the output layer (prediction layer) using the specified activation function
        y_hat = self.output_activation_fn.forward(
            np.dot(hidden_layer_output, self._wo) + self._bo
        )

        return y_hat, hidden_layer_output

    def _forward_logits(self, X_train: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        hidden_layer_output = self.hidden_activation_fn.forward(
            np.dot(X_train, self._wh) + self._bh,
        )
        # output layer does not apply softmax like other forward function, just return logits
        logits = np.dot(hidden_layer_output, self._wo) + self._bo
        return logits, hidden_layer_output

    def _backward(
        self,
        X_train: np.ndarray,
        y_hat: np.ndarray,
        y_train: np.ndarray,
        hidden_output: np.ndarray,
    ) -> None:
        assert self._wo is not None

        # Calculate the error at the output
        # This should be the derivative of the loss function with respect to the output of the network
        error_output = self.loss_fn.backward(y_hat, y_train)

        # Calculate gradients for output layer weights and biases
        wo_prime = np.dot(hidden_output.T, error_output) * self.learning_rate
        bo_prime = np.sum(error_output, axis=0, keepdims=True) * self.learning_rate

        # Propagate the error back to the hidden layer
        error_hidden = np.dot(
            error_output, self._wo.T
        ) * self.output_activation_fn.backward(hidden_output)

        # Calculate gradients for hidden layer weights and biases
        wh_prime = np.dot(X_train.T, error_hidden) * self.learning_rate
        bh_prime = np.sum(error_hidden, axis=0, keepdims=True) * self.learning_rate

        # Gradient clipping to prevent overflow
        max_norm = 1.0  # this is an adjustable threshold
        wo_prime = np.clip(wo_prime, -max_norm, max_norm)
        bo_prime = np.clip(bo_prime, -max_norm, max_norm)
        wh_prime = np.clip(wh_prime, -max_norm, max_norm)
        bh_prime = np.clip(bh_prime, -max_norm, max_norm)

        # Update weights and biases
        self._wo -= wo_prime
        self._wh -= wh_prime
        self._bo -= bo_prime
        self._bh -= bh_prime

    def train(self, X_train: np.ndarray, y_train: np.ndarray) -> "NN":
        assert self._p_bar is not None
        assert self._forward_fn is not None

        for _ in self._p_bar:
            n_samples = int(self.batch_size * X_train.shape[0])
            batch_indeces = np.random.choice(
                X_train.shape[0], size=n_samples, replace=False
            )

            X_train_batch = X_train[batch_indeces]
            y_train_batch = y_train[batch_indeces]

            y_hat, hidden_output = self._forward_fn(X_train=X_train_batch)
            loss = self.loss_fn.forward(y_hat=y_hat, y_true=y_train_batch)
            self._loss_history.append(loss)
            self._backward(
                X_train=X_train_batch,
                y_hat=y_hat,
                y_train=y_train_batch,
                hidden_output=hidden_output,
            )

        return self

    def predict(self, X_test: np.ndarray) -> np.ndarray:
        assert self._forward_fn is not None
        pred, _ = self._forward_fn(X_test)
        return self.output_activation_fn.forward(pred)
