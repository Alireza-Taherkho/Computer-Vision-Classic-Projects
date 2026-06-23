import numpy as np
import cv2 as cv


lower_green = np.array([65,200,70])
upper_green = np.array([90,255,255])


ball = [50,50,8]


cap = cv.VideoCapture(0)
while True:
    rec, frame = cap.read()
    if not rec:
        break

    
    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    green_mask = cv.inRange(hsv_frame, lower_green, upper_green)
    frame_mask = cv.bitwise_and(frame, frame, mask=green_mask)


    frame_mask = cv.morphologyEx(frame_mask, cv.MORPH_CLOSE, (15,15))
    frame_mask = cv.erode(frame_mask, (3,3), 1)
    frame_mask = cv.morphologyEx(frame_mask, cv.MORPH_OPEN, (7,7))


    cv.circle(frame_mask, (ball[0], ball[1]), ball[2], (255,255,255), -1)
    cv.line(frame_mask, (0, frame_mask.shape[0]//2), (frame_mask.shape[1], frame_mask.shape[0]//2), (255,255,255), 2)

    ball[1] += 4




    cv.imshow("frame", frame)
    cv.imshow("frame_mask", frame_mask)
    if cv.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv.destroyWindow()


















































