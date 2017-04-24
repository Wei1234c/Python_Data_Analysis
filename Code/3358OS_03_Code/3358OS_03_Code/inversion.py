import numpy as np

A = np.mat("2 4 6;4 2 6;10 -4 18")
print "A\n", A

inverse = np.linalg.inv(A)
print "inverse of A\n", inverse

print "Check\n", A * inverse
print "Error\n", A * inverse - np.eye(3)
