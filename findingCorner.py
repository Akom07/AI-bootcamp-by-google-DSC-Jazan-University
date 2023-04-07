import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("shapes.JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(img), plt.show
corner = cv2.goodFeaturesToTrack(gray, 30, 0.1, 10)
corner = np.int0(corner)

for i in corner:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 5, 255, -1)

plt.imshow(img)
plt.waitforbuttonpress()
