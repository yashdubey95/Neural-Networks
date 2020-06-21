# Perceptron Learning Rules

The goal of this assignment is to train a neural network on MNIST Data using various perceptron learninig rule like: Delta, Filtered and Unsupervised_hebb.

## File Description:

1. hebbian.py: Python file containing the implementation of the perceptron and all the helper functions.
2. test_hebbian.py: Python file containing unit tests.

## Usage:
1. To run the hebbian.py:
  ```bash
  python hebbian.py
  ```

2. To run the unit tests on the hebbian.py:
  ```bash
  py.test --verbose test_hebbian.py
  ```

## Output:
1. Output from the hebbian.py file:
  ```bash
  ******  Percent Error ******
 [0.75, 0.46, 0.34, 0.28, 0.28, 0.26, 0.24, 0.22, 0.27, 0.25]
[[ 8., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [ 2.,12., 0., 0., 0., 0., 0., 0., 0., 0.],
 [ 1., 0., 7., 0., 0., 0., 0., 0., 0., 0.],
 [ 2., 0., 0., 8., 0., 1., 0., 0., 0., 0.],
 [ 1., 0., 0., 1.,12., 0., 0., 0., 0., 0.],
 [ 2., 0., 0., 0., 0., 5., 0., 0., 0., 0.],
 [ 3., 0., 0., 0., 1., 1., 5., 0., 0., 0.],
 [ 2., 0., 0., 2., 0., 0., 0.,10., 0., 1.],
 [ 2., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [ 3., 0., 0., 0., 0., 0., 0., 0., 0., 8.]]
 ```
2. Output after running the test_hebbian.py:
  ```bash
  ================================================= test session starts =================================================
platform win32 -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- D:\Anaconda\python.exe
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('D:\\Assignment\\Neural_Networks\\Neural_Network\\Kamangar-02\\.hypothesis\\examples')
rootdir: D:\Assignment\Neural_Networks\Neural_Network\Kamangar-02
plugins: hypothesis-5.5.4, arraydiff-0.3, astropy-header-0.1.2, doctestplus-0.5.0, openfiles-0.4.0, remotedata-0.3.2
collected 7 items

test_hebbian.py::test_weight_dimension PASSED                                                                    [ 14%]
test_hebbian.py::test_weight_initialization PASSED                                                               [ 28%]
test_hebbian.py::test_predict PASSED                                                                             [ 42%]
test_hebbian.py::test_predict_2 PASSED                                                                           [ 57%]
test_hebbian.py::test_confusion_matrix PASSED                                                                    [ 71%]
test_hebbian.py::test_percent_error PASSED                                                                       [ 85%]
test_hebbian.py::test_training PASSED                                                                            [100%]

================================================== 7 passed in 3.19s ==================================================
```
