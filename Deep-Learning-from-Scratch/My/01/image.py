import matplotlib.pyplot as plt
from matplotlib.image import imread

img = imread('./candy.png')
plt.imshow(img)

plt.show()