import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_deriv(x):
    return x * (1 - x)

# Neural Network class
class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.5):
        # Weights initialization
        self.learning_rate = learning_rate
        self.input_size = input_size

        self.W1 = np.random.uniform(-1, 1, (input_size, hidden_size))
        self.B1 = np.random.uniform(-1, 1, (1, hidden_size))
        self.W2 = np.random.uniform(-1, 1, (hidden_size, output_size))
        self.B2 = np.random.uniform(-1, 1, (1, output_size))

    def forward(self, X):
        self.Z1 = np.dot(X, self.W1) + self.B1
        self.A1 = sigmoid(self.Z1)

        self.Z2 = np.dot(self.A1, self.W2) + self.B2
        self.A2 = sigmoid(self.Z2)
        return self.A2

    def backward(self, X, y, output):
        error = y - output
        d_output = error * sigmoid_deriv(output)

        error_hidden = d_output.dot(self.W2.T)
        d_hidden = error_hidden * sigmoid_deriv(self.A1)

        # Update weights and biases
        self.W2 += self.A1.T.dot(d_output) * self.learning_rate
        self.B2 += np.sum(d_output, axis=0, keepdims=True) * self.learning_rate

        self.W1 += X.T.dot(d_hidden) * self.learning_rate
        self.B1 += np.sum(d_hidden, axis=0, keepdims=True) * self.learning_rate

    def train(self, X, y, epochs=10000):
        for epoch in range(epochs):
            output = self.forward(X)
            self.backward(X, y, output)
            if epoch % 1000 == 0:
                loss = np.mean(np.square(y - output))
                print(f"Epoch {epoch} Loss: {loss:.4f}")

    def predict(self, X):
        output = self.forward(X)
        return np.round(output)

# XOR dataset
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])

y = np.array([[0], [1], [1], [0]])

# Create Neural Network
nn = NeuralNetwork(input_size=2, hidden_size=2, output_size=1)

# Train Neural Network
nn.train(X, y, epochs=10000)

# Predictions
print("\nFinal Predictions:")
for i in range(len(X)):
    print(f"Input: {X[i]} => Output: {nn.predict(X[i].reshape(1, -1))[0][0]}")
