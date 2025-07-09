import numpy as np
import matplotlib.pyplot as plt
from PIL import Image#python imaging library
img=Image.open(r'c:\Users\Lenovo\Desktop\elephant.jfif')
print(plt.imshow(img))
print(plt.show())