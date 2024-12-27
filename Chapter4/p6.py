#!/usr/bin/env python3

import numpy as np

layer_outputs = [4.8, 1.21, 2.385]

exp_values = np.exp(layer_outputs)
norm_values = exp_values / np.sum(exp_values)

print(f"Exp. values: {exp_values}")
print(f"Normalized values: {norm_values}")
print(f"Sum of normalized values: {np.sum(norm_values)}")
