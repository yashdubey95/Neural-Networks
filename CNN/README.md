# CNN

The purpose of the this assignment is either to create a sequential Convolutional Neural Networks (CNN) or fine-tune (retrain) an existing CNN model.

## File Description:

1. cnn.py: Python file containing the implementation of the neural network model and all the helper functions.
2. test_cnn.py: Python file containing unit tests.

## Usage:
1. To run the cnn.py:
  ```bash
  python cnn.py
  ```

2. To run the unit tests on the cnn.py:
  ```bash
  py.test --verbose test_cnn.py
  ```

## Output:
1. Output from the cnn.py file:
  ```bash
  Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv1 (Conv2D)               (None, 32, 32, 16)        448       
_________________________________________________________________
pool1 (MaxPooling2D)         (None, 16, 16, 16)        0         
_________________________________________________________________
conv2 (Conv2D)               (None, 16, 16, 8)         1160      
_________________________________________________________________
flatten (Flatten)            (None, 2048)              0         
_________________________________________________________________
dense1 (Dense)               (None, 10)                20490     
_________________________________________________________________
dense2 (Dense)               (None, 2)                 22        
=================================================================
Total params: 22,120
Trainable params: 22,120
Non-trainable params: 0
_________________________________________________________________
None
w0 None <class 'NoneType'>
b0 None <class 'NoneType'>
w1 (3, 3, 3, 16) <class 'numpy.ndarray'>
b1 (16,) <class 'numpy.ndarray'>
w2 None <class 'NoneType'>
b2 None <class 'NoneType'>
w3 (3, 3, 16, 8) <class 'numpy.ndarray'>
b3 (8,) <class 'numpy.ndarray'>
w4 None <class 'NoneType'>
b4 None <class 'NoneType'>
w5 (2048, 10) <class 'numpy.ndarray'>
b5 (10,) <class 'numpy.ndarray'>
input weights:  None <class 'NoneType'>
input biases:  None <class 'NoneType'>
conv1 weights:  (3, 3, 3, 16) <class 'numpy.ndarray'>
conv1 biases:  (16,) <class 'numpy.ndarray'>
pool1 weights:  None <class 'NoneType'>
pool1 biases:  None <class 'NoneType'>
conv2 weights:  (3, 3, 16, 8) <class 'numpy.ndarray'>
conv2 biases:  (8,) <class 'numpy.ndarray'>
flat1 weights:  None <class 'NoneType'>
flat1 biases:  None <class 'NoneType'>
dense1 weights:  (2048, 10) <class 'numpy.ndarray'>
dense1 biases:  None <class 'NoneType'>
dense2 weights:  (10, 2) <class 'numpy.ndarray'>
dense2 biases:  None <class 'NoneType'>
```

2. Output after running the test_cnn.py:
  ```bash
  ================================================= test session starts =================================================
platform win32 -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- D:\Anaconda\python.exe
cachedir: .pytest_cache
hypothesis profile 'default' -> database=DirectoryBasedExampleDatabase('D:\\Assignment\\Neural_Networks\\Neural_Network\\Kamangar-04\\Dubey-04\\CNN\\.hypothesis\\examples')
rootdir: D:\Assignment\Neural_Networks\Neural_Network\Kamangar-04\Dubey-04\CNN
plugins: hypothesis-5.5.4, arraydiff-0.3, astropy-header-0.1.2, doctestplus-0.5.0, openfiles-0.4.0, remotedata-0.3.2
collected 14 items

test_cnn.py::test_add_input_layer PASSED                                                                         [  7%]
test_cnn.py::test_append_conv2d_layer PASSED                                                                     [ 14%]
test_cnn.py::test_append_maxpooling2d_layer PASSED                                                               [ 21%]
test_cnn.py::test_add_flatten_layer PASSED                                                                       [ 28%]
test_cnn.py::test_append_dense_layer PASSED                                                                      [ 35%]
test_cnn.py::test_get_weights_without_biases_1 PASSED                                                            [ 42%]
test_cnn.py::test_get_weights_without_biases_2 PASSED                                                            [ 50%]
test_cnn.py::test_get_weights_without_biases_3 PASSED                                                            [ 57%]
test_cnn.py::test_get_biases_1 PASSED                                                                            [ 64%]
test_cnn.py::test_get_biases_2 PASSED                                                                            [ 71%]
test_cnn.py::test_set_weights_without_biases PASSED                                                              [ 78%]
test_cnn.py::test_load_and_save_model PASSED                                                                     [ 85%]
test_cnn.py::test_predict PASSED                                                                                 [ 92%]
test_cnn.py::test_remove_last_layer PASSED                                                                       [100%]

================================================= 14 passed in 24.18s =================================================
```
