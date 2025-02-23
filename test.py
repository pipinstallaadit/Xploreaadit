import cv2 as cv
img=cv.imread("car.png")
cv.imshow("Display window", img)
cv.waitKey(0)
cv.destroyAllWindows()