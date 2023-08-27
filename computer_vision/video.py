import cv2

VIDEO_PATH = r"C:\Users\ZAID\Videos\tll.exe\tll.exe 2023.07.19 - 00.22.33.02.DVR.mp4"
vid = cv2.VideoCapture(VIDEO_PATH) 

while True:
    status, img = vid.read()
    if not status:
        print('Video is not available')
        break
    # vision operations
    img = cv2.resize(img, None, fx=.25, fy=.25)
    cv2.imshow('Video', img)
    key = cv2.waitKey(10) # lower the value to increase fps
    if key == 27:
        break
cv2.destroyAllWindows()
vid.release()