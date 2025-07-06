import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1, epochs=10):
        self.weights = np.zeros(input_size + 1)  # +1 for bias
        self.lr = learning_rate
        self.epochs = epochs

    def activation_fn(self, x):
        return 1 if x >= 0 else 0

    def predict(self, x):
        x = np.insert(x, 0, 1)  # Insert bias term
        z = np.dot(self.weights, x)
        return self.activation_fn(z)

    def train(self, X, y):
        for _ in range(self.epochs):
            for xi, target in zip(X, y):
                xi = np.insert(xi, 0, 1)  # Bias term
                z = np.dot(self.weights, xi)
                pred = self.activation_fn(z)
                error = target - pred
                self.weights += self.lr * error * xi

    def test(self, X):
        return [self.predict(x) for x in X]

# Training data for AND and OR gates
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y_and = np.array([0, 0, 0, 1])
y_or  = np.array([0, 1, 1, 1])

# Train for AND gate
print("Training Perceptron for AND gate")
perceptron_and = Perceptron(input_size=2)
perceptron_and.train(X, y_and)

print("Results for AND gate:")
for inp, pred in zip(X, perceptron_and.test(X)):
    print(f"Input: {inp}, Output: {pred}")

print("\n" + "-"*30 + "\n")

# Train for OR gate
print("Training Perceptron for OR gate")
perceptron_or = Perceptron(input_size=2)
perceptron_or.train(X, y_or)

print("Results for OR gate:")
for inp, pred in zip(X, perceptron_or.test(X)):
    print(f"Input: {inp}, Output: {pred}")
