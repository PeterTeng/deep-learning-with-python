# Import extenal library
import numpy as np

x = np.array([1.0, 2.0, 3.0]) #=> array([ 1.,  2.,  3.])
y = np.array([2.0, 5.0, 10.0])

type(x) #=> <class 'numpy.ndarray'>

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x / 2.0)


A = np.array([[1, 2], [3, 4]])
B = np.array([100, 200])

print(A * B) #=> [[100, 400], [300, 800]]


# Access the array
X = np.array([[20, 30], [90, 100], [50, 200]])

X[0] #=> array([20, 30])
X[0][1] #=> 30

# First element in each array
for row in X:
    print(row[0])

X = X.flatten()
print(X) #=> [ 20  30  90 100  50 200]

X[np.array([0, 2, 4])] #=> array([20, 90, 50])

print(X > 30) #=> [False False  True  True  True  True]
print(X[X > 30]) #=> [ 90 100  50 200]
