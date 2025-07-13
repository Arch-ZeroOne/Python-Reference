import cv2 as cv
import numpy as np

video = cv.VideoCapture(0)

#create color we want to detect


lower_green = np.array([35, 100, 100])  # This is the lightest green we want to detect
upper_green = np.array([85, 255, 255])  # This is the darkest green we want to detect
upper_blue = np.array([0,0,255])
lower_blue = np.array([135, 206, 235])

while True:
    #reading the frame 
    # We get the two values here from the read functions
    isTrue,frame = video.read()
    cv.imshow("Frame",frame)
    
    # Stops the video if any of the condition is granted
    if cv.waitKey(20) and 0xFF == ord('d') or not isTrue :
        break
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)

    
    #shows grey color when the specific color is detected
    green_mask = cv.inRange(hsv,lower_green,upper_green)
    blue_mask = cv.inRange(hsv,lower_blue,upper_blue)
    
    
    cv.imshow("Green Mask",green_mask)
    cv.imshow("Blue Mask",blue_mask)

    
#Clean Up    
video.release()
cv.destroyAllWindows()
cv.waitKey(0)