import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_file(filename):
    img=cv2.imread(filename)
    img=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.show
    return img

filename= "gukesh.jpg"
print(read_file(filename))

