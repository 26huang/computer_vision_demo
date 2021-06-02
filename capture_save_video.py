import cv2 as cv

# # Define the codec and create VideoWriter object
# # In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2.
# # (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
# # In Windows: DIVX (More to be tested and added)
# # In OSX: MJPG (.mp4), DIVX (.avi), X264 (.mkv).

cap = cv.VideoCapture(0)
# Define the codec and create VideoWriter object
# width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH) + 0.5)
# height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT) + 0.5)
width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))
# width = int(cap.get(3))
# height = int(cap.get(4))
size = (width, height)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 60.0, size)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # frame = cv.flip(frame, 0)
    # write the flipped frame
    out.write(frame)
    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# Release everything if job is finished
cap.release()
out.release()
cv.destroyAllWindows()
