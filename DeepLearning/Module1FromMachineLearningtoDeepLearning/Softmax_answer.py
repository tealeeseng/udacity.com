"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np
scores = np.array(scores)

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    # pass  # TODO: Compute and return softmax(x)
    return np.exp(x)/np.sum(np.exp(x), axis=0)

print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt

x = np.arange(-2.0, 6.0, 0.1)
score_raw = [x, np.ones_like(x), 0.2 * np.ones_like(x)]
scores = np.vstack(score_raw)
scores_softmax = softmax(scores)

plt.plot(x, scores_softmax.T, linewidth=2)
plt.show()
#
# scores = np.array([[1, 2, 3, 6],
#                    [2, 4, 5, 6],
#                    [3, 8, 7, 6]])
# print softmax(scores)
