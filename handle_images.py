import cv2 as cv
import sys

# READ IMAGE
img = cv.imread(cv.samples.findFile("./Data/test.jpg"))
if img is None:
    sys.exit("Could not read the image.")

# SHOW IMAGE
cv.imshow("Display window", img)

# SAVE IMAGE IF 'S' KEY PRESSED
while True:
    k = cv.waitKey(1)
    if k == ord("s"):
        cv.imwrite("test.png", img)
    if k == ord("q"):
        break
cv.destroyAllWindows()