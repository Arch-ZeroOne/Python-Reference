import cv2 as cv
import numpy as np

img = cv.imread("../ReadImageVideo/Images/baki.jpeg")
cv.imshow("Baki",img)

# Converting BGR images to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image",gray)

# Blurring the image
"""You can increase the blur by increasing the KERNEL size (3,3)"""
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur",blur)

# Edge Cascade
"""This will find the edges present in the image"""
canny = cv.Canny(blur,125,175)
cv.imshow("Canny",canny)

# Dilating an image
dilated = cv.dilate(canny, np.ones((3,3)), iterations=1)
cv.imshow('Dilated',dilated)


# Eroding
eroded = cv.erode(dilated,np.ones((3,3)), iterations=1)
cv.imshow("Eroded",eroded)

# Resizing
"""This will resize the image to 500 by 500"""
resized = cv.resize(img,(500,500), interpolation=cv.INTER_AREA)
cv.imshow('Resized',resized)

#Cropping
""" Thi will assume that the imag is an array and we are gonna slice it to get the specific portions """
cropped = img[50:200 , 200:400] 
cv.imshow("Cropped",cropped)

cv.waitKey(0)