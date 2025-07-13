1. Capture video from webcam
2. Read each frame
3. Convert frame to HSV color space
4. Define color range (e.g., green)
5. Create a mask using inRange()
6. Use bitwise_and() to isolate that color
7. Show original, mask, and result side by side
8. Exit when 'q' key is pressed

Concept Why It’s Important
cv2.VideoCapture() Use webcam/video stream
cv2.cvtColor() Convert BGR to HSV (for better color detection)
cv2.inRange() Create masks to isolate specific colors
cv2.bitwise_and() Show only parts of the image that match the color
np.array() Define color thresholds
cv2.imshow() Display multiple windows simultaneously
