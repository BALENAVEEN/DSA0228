import cv2

# Read video file
cap = cv2.VideoCapture("video.mp4")   # change to your video name

if not cap.isOpened():
    print("Error: Cannot open video")

while True:
    ret, frame = cap.read()

    if not ret:
        print("End of video or cannot read frame")
        break

    cv2.imshow("Video", frame)

    # Press q to exit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
