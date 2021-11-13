# in Tensorflow > 2.0 you don't have to draw the graph anymore (sess)
import os
import tensorflow as tf 
import cProfile

# eager execution is set by default
print(tf.executing_eagerly()) # True

# That meas you can run Tensorflow operations immediately
x = [[2.]]
m = tf.matmul(x, x)
print("hello, {}".format(m))

# Easiest way to create a Tensor: tf.constant
# but remember tf.constant canot calculate gradients
a = tf.constant([1.]) # for float the default is float32
print(a)
a = tf.constant([1]) # for int the default is int32
print(a)

# Eager execution works nicely with NumPy.
# and the tf Tensor act as numpy array as well

a = tf.constant([[1, 2],
                 [3, 4]])
# Broadcasting support
b = tf.add(a, 1)
print(b)
# Operator overloading is supported
print(a * b)

# Use NumPy values
import numpy as np
c = np.multiply(a, b)
print(c) # c becomes Numpy array 

# Cal Gradient, note that only
# tf.Variable with dtype as float can be 
# used to cal gradients
# tf.Variable objects store mutable tf.Tensor
w = tf.Variable([[1., 2.],
                 [3., 4.]])
with tf.GradientTape() as tape:
  loss = w * w

grad = tape.gradient(loss, w)
print(grad) # => tf.Tensor([[2. 4.]
                          # [6. 8.]], shape=(2, 2), dtype=float32)

# tf.constant cannot
w = tf.constant([[1., 2.],
                 [3., 4.]])
with tf.GradientTape() as tape:
  loss = w * w

grad = tape.gradient(loss, w)
print(grad) # None

