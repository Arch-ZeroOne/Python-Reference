import cv2 as cv
import numpy as np


video_url = "./video/test_video.mp4"
capture = cv.VideoCapture(video_url)

#Color We want to detect 

#Displaying the video
while True:
    isTrue,frame = capture.read()
    cv.imshow("Frame",frame)
    
    if cv.waitKey(20) and 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)