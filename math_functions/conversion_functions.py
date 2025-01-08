import numpy as np


def sigmoid(real_value: float, k=1.0):
    # Simple logistic transform, no bias
    return 1.0 / (1.0 + np.exp(-k * real_value))