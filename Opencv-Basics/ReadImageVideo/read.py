# imports opencv packages
import cv2 as cv

#? Reading images in open Cv
#* This method takes a path of the images then returns the images as a matrix to pixels
# img = cv.imread("Images/baki.jpeg");

# displays the image as a new window
#* Receives two parameter window name , then the second param is the matrix to pixels to display which is in this case (img)
# cv.imshow("Baki",img)

#wait for a key to be pressed
# cv.waitKey(0)




#? Reading videos in OpenCv
# Takes also a path argument
# if you using webcams you will have to an integer argument (0)

capture = cv.VideoCapture(0)

# Videos is read frame by frame so we are gonna use a loop
while True:
    isTrue, frame = capture.read()
    #displays individual frame
    cv.imshow("Video",frame)
    
    #*breaks the loop
    # the ord('d') means if we press letter d the loop is breaked
    if cv.waitKey(20) and 0xFF == ord('d'):
        break

#cleans all window and stops the capture instance
capture.release()
cv.destroyAllWindows()
cv.waitKey(0)