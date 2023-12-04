import cv2

video = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame = cv2.resize(frame, (640, 480))

    cv2.imshow("Video", frame)

    if cv2.waitKey(25) == 27:
        break

video.release()
cv2.destroyAllWindows()
