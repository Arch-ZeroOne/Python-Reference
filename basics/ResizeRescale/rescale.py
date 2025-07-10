import cv2 as cv



#* resizes frame to a particular dimension
#* works for Images, Videos and Live Video
def rescaleFrame(frame,scale=0.75):
    #frame.shape[1] -> the width of the image
    #frame.shape[0] -> height of the image
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    
    #tupple
    dimension = (width,height)
    
    return cv.resize(frame,dimension,interpolation=cv.INTER_AREA)

#================================================================================

img = cv.imread("../ReadImageVideo/Images/baki.jpeg")
# Also resize the image
resized_image = rescaleFrame(img,0.7)
cv.imshow("Resized Image",resized_image)

#===============================================================================
#* Works for live video
def changeRes(width,height):
    # 3 -> references the video width
    # 4 -> references the height
    capture.set(3,width)
    capture.set(4,height)   
    
    
    
    
capture = cv.VideoCapture(0)


while True:
    isTrue,frame = capture.read()
    
    # sets the value to our custom sized frame
    #scale can set by percentage in decimal point form 0.2, = 20%
    frame_resized = rescaleFrame(frame,0.5)

    
    cv.imshow("Video",frame)
    # displays the resized frames
    cv.imshow('Video Resized',frame_resized,)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.waitKey
cv.destroyAllWindows()


