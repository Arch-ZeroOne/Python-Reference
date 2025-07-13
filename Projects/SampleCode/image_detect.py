# color_detector.py
import cv2 as cv  # OpenCV helps us work with images and video
import numpy as np  # NumPy helps us make and handle lists of numbers easily

# 🎥 Start capturing from the webcam so we can work with live video
cap = cv.VideoCapture(0)  # This grabs the camera input

# 🎯 We're going to look for green color, so we set the color range in HSV color space
# HSV is like a smarter version of colors that makes it easier to find exact colors
# Hue 35 to 85 means different shades of green
lower_green = np.array([35, 100, 100])  # This is the lightest green we want to detect
upper_green = np.array([85, 255, 255])  # This is the darkest green we want to detect

while True:
    ret, frame = cap.read()  # 📸 Take one picture from the webcam (called a "frame")
    if not ret:
        break  # If the camera didn’t work, stop the loop

    # 🎨 Convert the picture from BGR (normal OpenCV color format) to HSV
    # This helps us find colors better, like green in our case
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # 🖼️ Make a black-and-white picture where white means "this is green!"
    # and black means "this is not green"
    mask = cv.inRange(hsv, lower_green,upper_green)

    # 🧪 Show only the green parts by combining the original image and the mask
    # It’s like using a stencil — only the green parts are kept
    result = cv.bitwise_and(frame, frame, mask=mask)

    # 🪞 Show the normal video feed
    cv.imshow("Original", frame)

    # 🎭 Show the green mask (white = green detected, black = not green)
    cv.imshow("Green Mask", mask)

    # 🎨 Show the result where only green parts are visible
    cv.imshow("Filtered Result", result)

    # ⌨️ If you press the 'q' key, the program will stop
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# 🧹 Cleanup: Turn off the webcam and close the windows
cap.release()  # Stop using the webcam
cv.destroyAllWindows()  # Close all the image display windows
