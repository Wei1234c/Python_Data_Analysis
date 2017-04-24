import jpype
import numpy as np
from numpy import random

jpype.startJVM(jpype.getDefaultJVMPath())

random.seed(44)
values = np.random.randn(7)
java_array = jpype.JArray(jpype.JDouble, 1)(values.tolist())

for item in java_array:
   jpype.java.lang.System.out.println(item)

jpype.shutdownJVM()
