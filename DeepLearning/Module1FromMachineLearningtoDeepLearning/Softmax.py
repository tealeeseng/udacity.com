"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np
scores = np.array(scores)

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # pass  # TODO: Compute and return softmax(x)
    total = 0.0
    for j in x:
        total = total + np.exp(j)

    cells =np.array([ np.exp(k)/total for k in x])
    return cells

print('normal',softmax(scores))

scores10x = scores*10
print('10x', softmax(scores10x))


scoresDividedBy10 = scores/10
print('/10', softmax(scoresDividedBy10))

# Plot softmax curves
import matplotlib.pyplot as plt

x = np.arange(-2.0, 6.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()
#
# scores = np.array([[1, 2, 3, 6],
#                    [2, 4, 5, 6],
#                    [3, 8, 7, 6]])
# print softmax(scores)
