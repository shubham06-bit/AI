from collections import defaultdict, Counter
import math

class NaiveBayesClassifier:
    def __init__(self):
        self.class_probs = {}
        self.feature_probs = {}
        self.classes = set()

    def fit(self, X, y):
        self.classes = set(y)
        total_samples = len(y)

        # Prior probabilities
        class_counts = Counter(y)
        self.class_probs = {c: count / total_samples for c, count in class_counts.items()}

        # Likelihoods
        feature_counts = {c: defaultdict(Counter) for c in self.classes}

        for features, label in zip(X, y):
            for i, value in enumerate(features):
                feature_counts[label][i][value] += 1

        self.feature_probs = {
            c: {
                i: {
                    val: (count + 1) / (sum(counter.values()) + len(counter))
                    for val, count in counter.items()
                }
                for i, counter in feature_counts[c].items()
            }
            for c in self.classes
        }

    def predict(self, X):
        predictions = []
        for features in X:
            class_scores = {}
            for c in self.classes:
                log_prob = math.log(self.class_probs[c])
                for i, val in enumerate(features):
                    prob = self.feature_probs[c].get(i, {}).get(val, 1e-6)  # small prob for unseen
                    log_prob += math.log(prob)
                class_scores[c] = log_prob
            predicted_class = max(class_scores, key=class_scores.get)
            predictions.append(predicted_class)
        return predictions


# Example dataset: [Outlook, Temperature, Humidity, Wind], PlayTennis
X = [
    ['Sunny', 'Hot', 'High', 'Weak'],
    ['Sunny', 'Hot', 'High', 'Strong'],
    ['Overcast', 'Hot', 'High', 'Weak'],
    ['Rain', 'Mild', 'High', 'Weak'],
    ['Rain', 'Cool', 'Normal', 'Weak'],
    ['Rain', 'Cool', 'Normal', 'Strong'],
    ['Overcast', 'Cool', 'Normal', 'Strong'],
    ['Sunny', 'Mild', 'High', 'Weak'],
    ['Sunny', 'Cool', 'Normal', 'Weak'],
    ['Rain', 'Mild', 'Normal', 'Weak'],
    ['Sunny', 'Mild', 'Normal', 'Strong'],
    ['Overcast', 'Mild', 'High', 'Strong'],
    ['Overcast', 'Hot', 'Normal', 'Weak'],
    ['Rain', 'Mild', 'High', 'Strong']
]

y = ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
     'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']

# Train classifier
clf = NaiveBayesClassifier()
clf.fit(X, y)

# Predict
test_samples = [
    ['Sunny', 'Cool', 'High', 'Strong'],
    ['Overcast', 'Mild', 'Normal', 'Strong']
]
predictions = clf.predict(test_samples)

# Output
for sample, pred in zip(test_samples, predictions):
    print(f"Input: {sample} => Predicted: {pred}")
