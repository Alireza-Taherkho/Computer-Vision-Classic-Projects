import numpy as np
import cv2 as cv



img = cv.imread(r"7) chess map detection\data\2.webp")
img = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
blur = cv.GaussianBlur(gray, (3,3), 1)



corners = cv.goodFeaturesToTrack(blur, 85, 0.00005, 35)
corners = corners.reshape((corners.shape[0],2))


inx = np.lexsort((corners[:, 1], corners[:, 0]))
corners = np.astype(corners[inx], int) 
corners = corners[2:-2]



set_zero = 0
x = 0
for i in range(len(corners)):
    if set_zero == 0:
        x = corners[i][0]
        set_zero = 9

    if set_zero != 0:
        set_zero -= 1

    corners[i][0] = x

inx = np.lexsort((corners[:, 1], corners[:, 0]))
corners = np.astype(corners[inx], int) 

    



columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
rows = ['8', '7', '6', '5', '4', '3', '2', '1']
set_zero = 0
column = -1

for i, corner in enumerate(corners):
    x, y = corner
    x = int(x)
    y = int(y)
    # cv.circle(img, (x,y), 3, (0,0,255), 3)
    # cv.putText(img, str(i + 1), (x,y), cv.FONT_HERSHEY_PLAIN, 1, (0,200,0), 1)

    if set_zero == 0:
        column += 1
        set_zero = 9

    if set_zero != 0:
        set_zero -= 1

    row = i % 9

    if (i+1) % 9 != 0 and (i+1) <= 72:
        
        cv.putText(img, rows[row]+columns[column], (x+25,y+25), cv.FONT_HERSHEY_PLAIN, 1, (0,0,0), 1)
        


cv.imshow("img",img)
cv.waitKey()
cv.destroyAllWindows()


cv.imwrite(r"7) chess map detection\result\chess.png", img)
























