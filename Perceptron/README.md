#Perceptron

The goal of this assignment is to implement a perceptron model from scratch.

## File Description:
  1. perceptron.py: Python file that containing the implementation of the perceptron model and all necessary helper functions.
  2. test_perceptron.py: Python file containing unit tests.
  
## Usage:
1. To run the perceptron.py:
  ```bash
  python perceptron.py
  ```

2. To run the unit tests on the perceptron.py:
  ```bash
  py.test --verbose test_perceptron.py
  ```

## Output:
1. Output from the perceptron.py file:
  ```bash
  ****** Model weights ******
 [[0. 0. 0.]
 [0. 0. 0.]]
****** Input samples ******
 [[-1.  1.  1.  3.]
 [ 2.  3.  1.  2.]]
****** Desired Output ******
 [[0 0 1 1]
 [0 1 0 1]]
****** Model weights ******
 [[-1.  1. -2.]
 [-1.  1. -2.]]
****** Model weights ******
 [[-1.  1. -2.]
 [ 0.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-1.  1.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-1.  1.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-1.  1.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-1.  1.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-2.  0. -1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-1.  3.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-1.  3.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-1.  3.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-2.  2.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-2.  2.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-2.  2.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-2.  2.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-3.  1. -1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-2.  4.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-2.  4.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-2.  4.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-3.  3.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-3.  3.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-3.  3.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-3.  3.  0.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2. -1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2. -1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2. -1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-3.  3.  2.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
****** Model weights ******
 [[ 0.  2. -1.]
 [-4.  2.  1.]]
******  Percent Error ******
 [0.25, 0.25, 0.25, 0.25, 0.25, 0.25, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
 ```

2. Output after running the test_perceptron.py:
  ```bash
  ================================================= test session starts =================================================
platform win32 -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- D:\Anaconda\python.exe
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('D:\\Assignment\\Neural_Networks\\Neural_Network\\Perceptron\\.hypothesis\\examples')
rootdir: D:\Assignment\Neural_Networks\Neural_Network\Perceptron
plugins: hypothesis-5.5.4, arraydiff-0.3, astropy-header-0.1.2, doctestplus-0.5.0, openfiles-0.4.0, remotedata-0.3.2
collected 4 items

test_perceptron.py::test_weight_dimension PASSED                                                                 [ 25%]
test_perceptron.py::test_weight_initialization PASSED                                                            [ 50%]
test_perceptron.py::test_predict PASSED                                                                          [ 75%]
test_perceptron.py::test_error_calculation PASSED                                                                [100%]

================================================== 4 passed in 0.05s ==================================================
```
