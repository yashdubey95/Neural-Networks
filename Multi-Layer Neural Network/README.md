# MNIST Classifier

The purpose of the this assignment is to create multi-layer neural networks using Tensorflow (without using Keras).

## File Description:

1. multinn.py: Python file containing the implementation of the neural network model and all the helper functions.
2. test_multinn.py: Python file containing unit tests.

## Usage:
1. To run the multinn.py:
  ```bash
  python multinn.py
  ```

2. To run the unit tests on the multinn.py:
  ```bash
  py.test --verbose test_multinn.py
  ```

## Output:
1. Output from the multinn.py file:
  ```bash
  Percent error:  [0.452,0.204,0.064,0.016,0.   ,0.   ,0.   ,0.   ,0.   ,0.   ]
************* Confusion Matrix ***************
 [[50., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
 [ 0.,66., 0., 0., 0., 0., 0., 0., 0., 0.],
 [ 0., 0.,52., 0., 0., 0., 0., 0., 0., 0.],
 [ 0., 0., 0.,50., 0., 0., 0., 0., 0., 0.],
 [ 0., 0., 0., 0.,52., 0., 0., 0., 0., 0.],
 [ 0., 0., 0., 0., 0.,39., 0., 0., 0., 0.],
 [ 0., 0., 0., 0., 0., 0.,45., 0., 0., 0.],
 [ 0., 0., 0., 0., 0., 0., 0.,52., 0., 0.],
 [ 0., 0., 0., 0., 0., 0., 0., 0.,39., 0.],
 [ 0., 0., 0., 0., 0., 0., 0., 0., 0.,55.]]
 ```

2. Output after running the test_perceptron.py:
  ```bash
  ================================================= test session starts =================================================
platform win32 -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- D:\Anaconda\python.exe
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('D:\\Assignment\\Neural_Networks\\Neural_Network\\Kamangar-03\\Multi-Layer Neural Network\\.hypothesis\\examples')
rootdir: D:\Assignment\Neural_Networks\Neural_Network\Kamangar-03\Multi-Layer Neural Network
plugins: hypothesis-5.5.4, arraydiff-0.3, astropy-header-0.1.2, doctestplus-0.5.0, openfiles-0.4.0, remotedata-0.3.2
collected 5 items

test_multinn.py::test_weight_and_biases_dimensions PASSED                                                        [ 20%]
test_multinn.py::test_get_and_set_weight_and_biases PASSED                                                       [ 40%]
test_multinn.py::test_predict PASSED                                                                             [ 60%]
test_multinn.py::test_predict_02 PASSED                                                                          [ 80%]
test_multinn.py::test_train PASSED                                                                               [100%]

================================================= 5 passed in 12.67s ==================================================
```
