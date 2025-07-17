import cv2 as cv
import numpy as np

# TODO Master how to combine colors in HSV

# Opens the camera
video = cv.VideoCapture(0)

#create color we want to detect
#Sets the upper color and the lower color via HSV (Hue, Saturation, Value)
# Hue -> The color itself
#Saturation -> indicated how pure and vibrant the color is
#Value -> Highest value, Highest brightness
lower_green = np.array([35, 100, 100])  # This is the lightest green we want to detect
upper_green = np.array([85, 255, 255])  # This is the darkest green we want to detect


lower_black = np.array([0,100,0]);
upper_black = np.array([0,100,24])

# lower_pink = np.array([290,40,100])
# upper_pink = np.array([290,100,95])


#* RGB Version
# lower_green = np.array([153,255,153])
# upper_green = np.array([0,153,76])



while True:
    #reading the frame 
    # We get the two values here from the read functions
    isTrue,frame = video.read()
    # cv.imshow("Original",frame)
    
    # Stops the video if any of the condition is granted
    if cv.waitKey(20) and 0xFF == ord('d') or not isTrue :
        break
    
    
    # Extracts the HSV value from an image or a value
    
    #* HSV Version -> extracts the HSV color from an Image or A Video
    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    #* RGB Version
    # rgb = cv.cvtColor(frame,cv.COLOR_BGR2RGB)
    
    #shows grey color when the specific color is detected
    green_mask2= cv.inRange(hsv,lower_green,upper_green)
    black_mask = cv.inRange(hsv,lower_black,upper_black)


    # cv.imshow("RGB",green_mask2)
    cv.imshow('Original',frame)
    cv.imshow("HSV_GREEN",green_mask2)
    cv.imshow("HSV_BLACK",black_mask)
    

    
#Clean Up    
video.release()
cv.destroyAllWindows()
cv.waitKey(0)   