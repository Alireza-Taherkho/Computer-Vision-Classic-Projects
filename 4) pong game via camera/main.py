import numpy as np
import cv2 as cv



lower_green = np.array([65,155,70])
upper_green = np.array([90,255,255])


ball = [50,50,16]

ball_status = "down"
status_LR = "right"
player = False
level = 4
score = 0
levelUp = False
def ball_movement(line, w_shape, status1=ball_status, status2=status_LR, score=score, level=level, lup=levelUp):
    
    if ball[1] <= 0:
        status1 = "down"
    elif player and status1 != "up":
        if y > line:
            if (ball[0] > x) and (ball[1] > y) and (ball[0] < x+w) and (ball[1] < y+h):
                status1 = "up"
                score += 1
    
        
    if status1 == "down":
        ball[1] += level
    elif status1 == "up":
        ball[1] -= level



    if ball[0] >= w_shape[1]:
        status2 = "left"
    elif ball[0] <= 0:
        status2 = "right"
        
    if status2 == "right":
        ball[0] += level
    elif status2 == "left":
        ball[0] -= level

    score_list = [5,10,15,20,25,30,50,100,150,200,250,300]
    if lup == False:
        if score == 5 or score == 10 or score == 15 or score == 20 or score == 25 or score == 30:
            level += 2
            lup = True
        if score == 50 or score == 100 or score == 150 or score == 200 or score == 250:
            level += 5
            lup = True
        if score == 300:
            level += 10
            lup = True
    elif lup == True and score not in score_list:
        lup = False


    if ball[1] >= w_shape[0]:
        return -1,-1,score,level,lup
    

    return status1, status2, score, level, lup
    



    

# ----------
cap = cv.VideoCapture(0)
while True:
    rec, frame = cap.read()
    if not rec:
        break
    frame = cv.flip(frame, 1)


    hsv_frame = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    green_mask = cv.inRange(hsv_frame, lower_green, upper_green)

    dilated = cv.dilate(green_mask, (15,15), iterations=2)
    morph_close = cv.morphologyEx(dilated, cv.MORPH_CLOSE, (55,55))

    frame_mask = cv.bitwise_and(frame, frame, mask=morph_close)


    edges = cv.Canny(frame_mask, 50,200)
    contours, _ = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    sorted_contours = sorted(contours, key=cv.contourArea, reverse=True)
    if sorted_contours:
        player = True
        x,y,w,h = cv.boundingRect(sorted_contours[0])

        
    


    cv.circle(frame_mask, (ball[0], ball[1]), ball[2], (255,255,255), -1)
    line_height =  frame_mask.shape[0]//2
    cv.line(frame_mask, (0, line_height), (frame_mask.shape[1], line_height), (255,255,255), 2)
    cv.putText(frame_mask, f"score: {score}", (10,25), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)
    cv.putText(frame_mask, f"speed: {level}", (10,50), cv.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 1)

    if ball_status != -1:
        ball_status, status_LR, score, level, levelUp = ball_movement(line_height, frame_mask.shape, ball_status, status_LR, score, level, levelUp)
    else:
        coor = frame_mask.shape
        cv.rectangle(frame_mask, (coor[1]//4, coor[0]//4), (coor[1] - coor[1]//4, coor[0] - coor[0]//4),
        (0,0,255), -1)
        cv.putText(frame_mask, "You loss", ((coor[1]//4, coor[0]//2)), cv.FONT_HERSHEY_COMPLEX, 2, (255,255,255), 2)



    cv.imshow("frame", frame)
    cv.imshow("frame_mask", frame_mask)
    if cv.waitKey(1) & 0xFF == 27:
        break
    


# ------
cap.release()
cv.destroyWindow()


















































