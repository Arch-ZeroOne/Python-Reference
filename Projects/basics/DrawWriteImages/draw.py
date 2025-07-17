import cv2 as cv
import numpy as np



#Creating blank image to draw with
# np.zeros(height,width,# of color channels)
blank = np.zeros((500,500,3),dtype="uint8")
# cv.imshow("Blank",blank)

# 1 Paint the image certain color

#* slice assignment  -> modifirs the original array in place
# blank[:] = 0,255,0

#* Coloring a specific portion
# first parameter -> rows (kataason)
# second parameter -> columns (kalaparon)
# blank[100:200 , 0:len(blank)] = 0,0,255

# cv.imshow("Red",blank)
# cv.waitKey(0)

# 2 Draws a rectangle 
# cv.rectangle(blank,(0,0),(250,250), (0,255,255), thickness=cv.FILLED)
cv.rectangle(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2), (0,255,255), thickness=cv.FILLED)
cv.imshow("Rectangle",blank)

# 3 Draws A Circle
cv.circle(blank,(250,250), 40, (0,0,255) ,thickness=3)
cv.imshow("Circle",blank)



# 4 Draws a standalone line
cv.line(blank,(0,0),(blank.shape[1]//2 , blank.shape[0]//2), (255,255,255),thickness=3 )
cv.imshow("Line",blank)


# 5 Write a text on an image

cv.putText(blank,'Nigga Green', (225,225), cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)

cv.imshow("Text",blank)




cv.waitKey(0)


