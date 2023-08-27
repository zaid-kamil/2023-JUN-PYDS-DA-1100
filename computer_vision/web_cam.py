import cv2 # library version 4

CAM_IDX = 0
cam = cv2.VideoCapture(CAM_IDX)     # Create a VideoCapture object
while cam.isOpened():               # Loop until the camera is available
    status, img = cam.read()        # Read the frame/image 
    if status:
        cv2.imshow('Webcam', img)   # Display the frame/image
        key = cv2.waitKey(10)       # Wait for a key press
        if key == 27:               # If the key pressed is ESC
            break                   # Exit the loop
    else:
        print('Webcam is not available')
        break
# free up resources
cv2.destroyAllWindows()             # Close all windows
cam.release()                       # Release the camera