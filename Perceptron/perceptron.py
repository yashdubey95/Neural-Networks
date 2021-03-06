# Dubey, Yash
# 1001-670-330
# 2019-09-23
# Assignment-01-01

import numpy as np
import itertools


class Perceptron(object):
    def __init__(self, input_dimensions=2, number_of_classes=4, seed=None):
        """
        Initialize Perceptron model
        :param input_dimensions: The number of features of the input data, for example (height, weight) would be two features.
        :param number_of_classes: The number of classes.
        :param seed: Random number generator seed.
        """
        if seed != None:
            np.random.seed(seed)
        self.input_dimensions = input_dimensions
        self.number_of_classes= number_of_classes
        self._initialize_weights()
    
    def _initialize_weights(self):
        """
        Initialize the weights, initalize using random numbers.
        Note that number of neurons in the model is equal to the number of classes
        """
        classes = self.number_of_classes
        in_dim = self.input_dimensions
        self.weights = np.random.randn(classes, in_dim + 1)

    def initialize_all_weights_to_zeros(self):
        """
        Initialize the weights to zero.
        """
        cls_zero = self.number_of_classes
        dim_zero = self.input_dimensions
        self.weights = np.zeros((cls_zero, dim_zero + 1))

    def predict(self, X):
        """
        Make a prediction on an array of inputs
        :param X: Array of input [input_dimensions,n_samples]. Note that the input X does not include a row of ones
        as the first row.
        :return: Array of model outputs [number_of_classes ,n_samples]
        """
        X = np.insert(X, 0, 1, axis = 0)
        net = np.dot(self.weights,X)
        y_pred = np.where(net>=0.0,1.0,0.0)
        return y_pred


    def print_weights(self):
        """
        This function prints the weight matrix (Bias is included in the weight matrix).
        """
        print(self.weights)

    def train(self, X, Y, num_epochs=10, alpha=0.001):
        """
        Given a batch of data, and the necessary hyperparameters,
        this function adjusts the self.weights using Perceptron learning rule.
        Training should be repeted num_epochs time.
        :param X: Array of input [input_dimensions,n_samples]
        :param y: Array of desired (target) outputs [number_of_classes ,n_samples]
        :param num_epochs: Number of times training should be repeated over all input data
        :param alpha: Learning rate
        :return: None
        """
        X = np.insert(X, 0, 1, axis = 0)
        for _ in range(num_epochs):
            for i in range(X.shape[1]):
                i_xT = X.T[i:i+1, 0:]
                net = np.dot(self.weights,i_xT.T)
                y_out = np.where(net >= 0.0, 1.0, 0.0)
                error = Y[:,[i]] - y_out
                self.weights[0:,1:] = self.weights[0:,1:] + alpha*error*X.T[i:i+1, 1:]
                self.weights[0:,:1] = self.weights[0:,:1] + alpha*error
                

    def calculate_percent_error(self,X, Y):
        """
        Given a batch of data this function calculates percent error.
        For each input sample, if the output is not hte same as the desired output, Y,
        then it is considered one error. Percent error is number_of_errors/ number_of_samples.
        :param X: Array of input [input_dimensions,n_samples]
        :param y: Array of desired (target) outputs [number_of_classes ,n_samples]
        :return percent_error
        """
        y_hat = self.predict(X)
        num_of_errors = 0
        for i in range(X.shape[1]):
            i_y_pred = y_hat[:,i]
            i_y_true = Y[:,i]
            if tuple(i_y_pred) == tuple(i_y_true):
                continue
            else:
                num_of_errors += 1
        return num_of_errors/X.shape[1]

if __name__ == "__main__":

    input_dimensions = 2
    number_of_classes = 2

    model = Perceptron(input_dimensions=input_dimensions, number_of_classes=number_of_classes, seed=1)
    X_train = np.array([[-1.43815556, 0.10089809, -1.25432937, 1.48410426],
                        [-1.81784194, 0.42935033, -1.2806198, 0.06527391]])
    Y_train = np.array([[1, 0, 0, 1], [0, 1, 1, 0]])
    model.initialize_all_weights_to_zeros()
    print("****** Model weights ******\n",model.weights)
    print("****** Input samples ******\n",X_train)
    print("****** Desired Output ******\n",Y_train)
    percent_error=[]
    for k in range (20):
        model.train(X_train, Y_train, num_epochs=1, alpha=0.0001)
        percent_error.append(model.calculate_percent_error(X_train,Y_train))
    print("******  Percent Error ******\n",percent_error)
    print("****** Model weights ******\n",model.weights)
