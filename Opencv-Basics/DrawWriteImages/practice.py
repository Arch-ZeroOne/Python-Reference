import cv2 as cv
import numpy as py


# Creates a blank canvas


# py.zeros((height,width),number of rgb values to be accepted)
blank = py.zeros((500,800,3),dtype="uint8")
# cv.imshow("Blank",blank)

# blank[:] = (255,255,255)
# cv.imshow("White",blank)

# blank[:] = (204,204,255)
# cv.imshow("Pinkish", blank)   


# blank[:] = (255,51,51)
# cv.imshow("Blue",blank)


# blank[:] = (255,255,229)
# cv.imshow("Blue",blank)


# draws a rectangle
cv.rectangle(blank,(0,0),(blank.shape[1] // 2, blank.shape[0]//2), (11,171,2055),thickness=cv.FILLED)
cv.imshow("Rectangle", blank)




cv.waitKey(0)