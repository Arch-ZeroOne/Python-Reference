import cv2 as cv


capture = cv.VideoCapture(0)

# cv.imshow("Baki",image)


while True:
    isTrue,frame = capture.read()
    
    cv.imshow("Sea",frame)
    
    #cv.waitKey -> Listens for a keypress 
    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)