import cv2
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np

face_image = cv2.imread('img_streetview/teste.jpg')

gray_img = cv2.cvtColor(face_image, cv2.COLOR_BGR2GRAY)

plt.figure(figsize=(10,10))
plt.imshow(gray_img, cmap='gray')