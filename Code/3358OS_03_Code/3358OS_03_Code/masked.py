import numpy
import scipy.misc
import matplotlib.pyplot as plt

lena = scipy.misc.lena()
random_mask = numpy.random.randint(0, 2, size=lena.shape)

plt.subplot(221)
plt.title("Original")
plt.imshow(lena)
plt.axis('off')

masked_array = numpy.ma.array(lena, mask=random_mask)
print masked_array

plt.subplot(222)
plt.title("Masked")
plt.imshow(masked_array)
plt.axis('off')

plt.subplot(223)
plt.title("Log")
plt.imshow(numpy.log(lena))
plt.axis('off')

plt.subplot(224)
plt.title("Log Masked")
plt.imshow(numpy.log(masked_array))
plt.axis('off')

plt.show()
