import cv2 as cv
import numpy as np



cap = cv.VideoCapture(r"9) road detection\data\road1.mp4")

# fps = cap.get(cv.CAP_PROP_FPS)
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv.VideoWriter_fourcc(*"mp4v")
# out = cv.VideoWriter(r"9) road detection\output\result1.mp4", fourcc, fps, (width, height))


votes = []
while True:
    rec, main_frame = cap.read()
    if not rec:
        break


    # extracting interest or vital region
    f = main_frame.shape[0] - main_frame.shape[0]//5
    frame = main_frame[f: , :]

    #  our car point
    car_point = [frame.shape[1]//2, frame.shape[0]]
    cv.circle(frame, car_point, 5, (255,0,0), 2)


    # detecting lines
    edges = cv.Canny(frame, 50, 200)
    lines = cv.HoughLinesP(image=edges, rho=1, theta=np.pi/180, threshold=50, minLineLength=40, maxLineGap=50)

    
    x_list = []
    for line in lines:
        x1, y1, x2, y2 = line[0]

        # calcuting the angle of lines; -30 <= angle <= 30 means right, -140 > angle > 140 means left.
        # actully we ignored horizontal lines
        dx = x2 - x1
        dy = y2 - y1
        angle = int(np.degrees(np.arctan2(-dy, dx)))
        if (-30 <= angle <= 30) or (-140 > angle > 140):
            continue

        cv.line(frame, (x1,y1), (x2, y2), (255,0,0), 2)
        
        # calcuting and extracting center points of lines
        center_x = (x2 + x1) // 2
        x_list.append(int(center_x))


    # calcuting and extracting center points of between lines. (len(x_list) > 4) gives us more clear output.
    if x_list and len(x_list) > 4:
        leftmost_x = min(x_list)
        rightmost_x = max(x_list)
        center_x = (leftmost_x + rightmost_x) // 2
        center_point = [center_x, frame.shape[0]//2]
        cv.circle(frame, center_point, 5, (0,0,255), -1)

        cv.line(frame, car_point, (center_point), (0,255,255), 1)

        # calcuting the angle of deviation
        dx = center_point[0] - car_point[0]
        dy = center_point[1] - car_point[1]
        angle = int(np.degrees(np.arctan2(-dy, dx)))
        angle_of_deviation = 90 - angle

        if -15 < angle_of_deviation < 15:
            color = (0,255,0)
            result = True
        else:
            color = (0,0,255)
            result = False
        cv.putText(frame, str(angle_of_deviation), (car_point[0], car_point[1]-10), cv.FONT_HERSHEY_PLAIN, 2, color, 2)


        # alarm base on more false votes
        if len(votes) > 5:
            votes.clear()
        votes.append(result)

        alarm = votes.count(False)
        if alarm >= 3:
            cv.circle(frame, (30,30), 30, (0,0,255), -1)
            cv.putText(frame, "!", (25,40), cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)



    

    cv.imshow("frame",main_frame)
    # out.write(main_frame)


    if cv.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()



