import cv2
import numpy as np

video = cv2.VideoCapture("video.mp4")

if not video.isOpened():
    print("Error: Could not open video.")
    exit()

image = cv2.imread("Sand.webp")

if image is None:
    print("Error: Could not open image.")
    exit()

image = cv2.resize(image, (640, 480))

while True:
    ret, frame = video.read()

    if not ret:
        print("Error: Could not read frame.")
        break

    frame = cv2.resize(frame, (640, 480))

    u_green = np.array([104, 153, 70])
    l_green = np.array([30, 30, 0])

    mask = cv2.inRange(frame, l_green, u_green)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    f = res - frame

    f = np.where(f == 0, f, image)

    cv2.imshow("Original Video", frame)
    cv2.imshow("Processed Frame", f)

    if cv2.waitKey(25) == 27:
        break

video.release()
cv2.destroyAllWindows()
