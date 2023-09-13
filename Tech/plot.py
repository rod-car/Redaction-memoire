import matplotlib.pyplot as plt

# True positives, false positives, and false negatives based on different thresholds
thresholds = [0.2, 0.4, 0.6, 0.8, 1.0]
true_positives = [7, 7, 7, 7, 7]
false_positives = [3, 2, 1, 0, 0]
false_negatives = [3, 3, 3, 3, 3]

# Calculate precision and recall for each threshold
precision = [tp / (tp + fp) for tp, fp in zip(true_positives, false_positives)]
recall = [tp / (tp + fn) for tp, fn in zip(true_positives, false_negatives)]

# Plot the precision-recall curve
plt.plot(recall, precision, marker='o', linestyle='-')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.title('Precision-Recall Curve')
plt.grid(True)
plt.show()