import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from PIL import Image


my_array = np.array([1.1, 9.2, 8.1, 4.7])

print(my_array.shape)
print(my_array[2])
print(my_array.ndim)

array_2d = np.array([[1, 2, 3, 9], [5, 6, 7, 8]])

print(f'array_2d has {array_2d.ndim} dimensions')
print(f'Its shape is {array_2d.shape}')
print(f'It has {array_2d.shape[0]} rows and {array_2d.shape[1]} columns')
print(array_2d)

print(array_2d[1,2])
print(array_2d[0, :])

mystery_array = np.array([[[0, 1, 2, 3],
                           [4, 5, 6, 7]],

                          [[7, 86, 6, 98],
                           [5, 1, 0, 4]],

                          [[5, 36, 32, 48],
                           [97, 0, 27, 18]]])

print(f'We have {mystery_array.ndim} dimensions')
print(f'The shape is {mystery_array.shape}')
print(mystery_array[2, 1, 3])
print(mystery_array[2, 1, :])
print(mystery_array[:, :, 0])

# Generating and Manipulating ndarrays
a = np.arange(10, 30)
print(a)
a[-3:]
a[3:6]
a[12:]
a[::2]
np.flip(a)
# or
a[::-1]

b = np.array([6, 0, 9, 0, 0, 5, 0])
nz_indices = np.nonzero(b)
nz_indices # note this is a tuple

from numpy.random import random
z = random((3, 3, 3))
z
# or
z = np.random.random((3, 3, 3)) # without an import statement
print(z.shape)
z

x = np.linspace(0, 100, num=9)
print(x)
x.shape

y = np.linspace(start=-3, stop=3, num=9)
plt.plot(x, y)
plt.show()

noise = np.random.random((128, 128, 3))
print(noise.shape)
plt.imshow(noise)

# Broadcasting, Scalars and Matrix Multiplication

v1 = np.array([4, 5, 2, 7])
v2 = np.array([2, 1, 3, 3])
v1 + v2

list1 = [4, 5, 2, 7]
list2 = [2, 1, 3, 3]
list1 + list2

v1 * v2
# list1 * list2 won't work as they are lists

array_2d = np.array([[1, 2, 3, 4],
                     [5, 6, 7, 8]])

array_2d + 5
array_2d * 10

a1 = np.array([[1, 3],
               [0, 1],
               [6, 2],
               [9, 7]])

b1 = np.array([[4, 1, 3],
               [5, 8, 5]])

c = np.matmul(a1, b1)


# Manipulating Images as ndarrays
img = misc.face()
plt.imshow(img)

type(img)
img.shape
img.ndim

# convert to black and white
sRGB_array = img / 255
grey_vals = np.array([0.2126, 0.7152, 0.0722])
img_gray = sRGB_array @ grey_vals

img_gray = sRGB_array @ grey_vals
img_gray = np.matmul(sRGB_array, grey_vals)

plt.imshow(img_gray, cmap='gray')
plt.imshow(np.flip(img_gray), cmap='gray')
plt.imshow(np.rot90(img))

solar_img = 255 - img
plt.imshow(solar_img)




