import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("randomFaces.png")

rgp = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imwrite("randomFaces2.jpg", gray)


# 1
plt.imshow(rgp)
plt.waitforbuttonpress()

# 2
# cv2.imshow("asd", gray)

# i = cv2.waitKey(0)

# if i == ord('s'):
#     cv2.destroyAllWindows
