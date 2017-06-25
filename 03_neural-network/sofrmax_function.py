import numpy as np

# Simple way
# def softmax(a):
#     exp_a = np.exp(a)
#     sum_exp_a = np.sum(exp_a)
#     y = exp_a / sum_exp_a
#
#     return y

# Prevent Overflow
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

A = np.array([0.3, 2.9, 4.0])
print(softmax(A))

print("SUM of softmax(A) =")
print(np.sum(softmax(A)))

# Output
# [ 0.01821127  0.24519181  0.73659691]
# SUM of softmax(A) =
# 1.0
