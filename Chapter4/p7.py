#!/usr/bin/env python3

import numpy as np

layer_outputs = np.array([
    [4.8, 1.21, 2.385],
    [8.9, -1.81, 0.2],
    [1.41, 1.051, 0.026]
])

print(f"Sum without axis: {np.sum(layer_outputs)}")
print(f"Identical: {np.sum(layer_outputs, axis=None)}")
print(f"Axis = 0: {np.sum(layer_outputs, axis=0)}")
print(f"Axis = 1: {np.sum(layer_outputs, axis=1)}")
print(f"Axis = 1, keepdims=True: {np.sum(layer_outputs, axis=1, keepdims=True)}")
