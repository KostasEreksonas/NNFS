#!/usr/bin/env python3

import math

# An example output from the output layer of the neural network
softmax_output = [0.7, 0.1, 0.2]

# Ground truth
target_output = [1, 0, 0]

loss = -(
    math.log(softmax_output[0])*target_output[0] +
    math.log(softmax_output[1])*target_output[1] +
    math.log(softmax_output[2])*target_output[2]
)

loss2 = -math.log(softmax_output[0])

print(f"Loss: {loss}")
print(f"Loss: {loss2}")
