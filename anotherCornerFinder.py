import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread("shapes.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

des = cv2.cornerHarris(gray, 5, 5, 0.07)
des = cv2.dilate(des, None)

img[des > 0.01*des.max()] = [255, 0, 0]

plt.imshow(img)
plt.waitforbuttonpress()
