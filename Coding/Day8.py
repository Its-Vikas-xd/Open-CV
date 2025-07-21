# Image Filtering Process

import cv2
import numpy as np


# Gaussian Filtering Process

image = cv2.imread(r"C:\Users\Vikas\Desktop\OpenCV\Images\img10.jpg")
image = cv2.resize(image,(500,500))
blurred = cv2.GaussianBlur(image,(9,9),3)


cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()



# Median Filtering Process

image = cv2.imread(r"C:\Users\Vikas\Desktop\OpenCV\Images\img11.jpg")
image = cv2.resize(image, (500, 500))
blurred = cv2.medianBlur(image, 17)

cv2.imshow("Original Image",image)
cv2.imshow("Clear Image",blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()


# Sharpering Process

image = cv2.imread(r"C:\Users\Vikas\Desktop\OpenCV\Images\img12.jpg")
image = cv2.resize(image, (500, 500))

sharpening_kernal = np.array([[0, -1, 0],
                              [-1, 5, -1],
                              [0, -1, 0]])


sharpended = cv2.filter2D(image,-1,sharpening_kernal)

cv2.imshow("Original Image",image)
cv2.imshow("Sharpended Image",sharpended)

cv2.waitKey(0)
cv2.destroyAllWindows()