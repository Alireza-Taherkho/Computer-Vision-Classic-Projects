import numpy as np
import cv2 as cv
import pickle




with open(r"8) fall warning alarm\model\model1.pkl", "rb") as file:
    model = pickle.load(file)



cap = cv.VideoCapture(r"8) fall warning alarm\data\vid1.mp4")


# fps = cap.get(cv.CAP_PROP_FPS)
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# fourcc = cv.VideoWriter_fourcc(*"mp4v")
# out = cv.VideoWriter(r"8) fall warning alarm\output\output.mp4", fourcc, fps, (width, height))

y_list = []
while True:
    rec, frame1 = cap.read()
    rec, frame2 = cap.read()
    if not rec:
        break

    frame_diff = cv.absdiff(frame1, frame2)

    gray = cv.cvtColor(frame_diff, cv.COLOR_BGR2GRAY)
    edges = cv.Canny(gray, 50, 200)
    blur = cv.GaussianBlur(edges, (3,3), 1)
    contours, _ = cv.findContours(blur, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)


    for c in contours:
        if cv.contourArea(c) > 250:
            x,y,w,h = cv.boundingRect(c)
            y_list.append(y)
        



    if len(y_list) >= 10:
        data = y_list[-10:].copy()
        result = model.predict([data])
        if result[0] == 1:
            cv.putText(frame2, "Falling", (25,25), cv.FONT_HERSHEY_PLAIN, 2, (0,0,255), 2)




    # out.write(frame2)

    cv.imshow("frame", frame2)
    if cv.waitKey(10) & 0xFF == 27:
        break

cap.release()
cv.destroyAllWindows()


























