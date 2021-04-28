import cv2
import numpy as np

image = cv2.imread('abhiyaan_opencv_qn1.png')
blur = cv2.GaussianBlur(image, (5, 5), 0)
hsv_image = cv2.cvtColor(blur, cv2.COLOR_RGB2HSV)

lower_red = np.array([100, 50, 50])
upper_red = np.array([200, 255, 255])
mask = cv2.inRange(hsv_image, lower_red, upper_red)

contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 80:
        cv2.drawContours(image, contour, -1, (0, 255, 0), 3)

cv2.imshow('obstacle detector', image)
cv2.waitKey()