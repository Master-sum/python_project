import matplotlib.pyplot as plt
import pylab

img = plt.imread('./t1.jpg')
plt.imshow(img)
print(img.shape)