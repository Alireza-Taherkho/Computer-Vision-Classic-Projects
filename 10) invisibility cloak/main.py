import cv2 as cv
import numpy as np



bg = cv.imread(r"10) invisibility cloak\data\background.jpg")
obj = cv.imread(r"10) invisibility cloak\data\object.jpg")


bg = cv.pyrDown(bg)
obj = cv.pyrDown(obj)

hsv_obj = cv.cvtColor(obj, cv.COLOR_BGR2HSV)
lower_color = np.array([50,0,50])
upper_color = np.array([110,255,250])
mask = cv.inRange(hsv_obj, lower_color, upper_color)

opened = cv.morphologyEx(mask, cv.MORPH_OPEN, (25,25))
dilated = cv.dilate(opened, (65,65), iterations=2)
closed = cv.morphologyEx(dilated, cv.MORPH_CLOSE, (99,99))
dilated = cv.dilate(closed, (65,65), iterations=2)
closed = cv.morphologyEx(dilated, cv.MORPH_CLOSE, (99,99))


bg_cloak = cv.bitwise_and(bg, bg, mask=closed)
reverse_closed = cv.bitwise_not(closed)
reverse_closed = cv.bitwise_and(obj, obj, mask=reverse_closed)

cloak_replace = np.where(reverse_closed == 0, bg_cloak, reverse_closed)



cv.imshow("obj", obj)
cv.imshow("cloak_replace", cloak_replace)
cv.waitKey()
cv.destroyAllWindows()


cv.imwrite(r"10) invisibility cloak\output\result.png", cloak_replace)





















































