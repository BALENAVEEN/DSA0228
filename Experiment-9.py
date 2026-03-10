import cv2
import numpy as np

# Capture video from webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    rows, cols, ch = frame.shape

    # Four points from original frame
    pts1 = np.float32([[50,50], [cols-50,50], [50,rows-50], [cols-50,rows-50]])

    # Four points in output frame
    pts2 = np.float32([[0,0], [cols,0], [100,rows], [cols-100,rows]])

    # Perspective transformation matrix
    M = cv2.getPerspectiveTransform(pts1, pts2)

    # Apply transformation
    transformed = cv2.warpPerspective(frame, M, (cols, rows))

    # Display frames
    cv2.imshow("Original Video", frame)
    cv2.imshow("Perspective Transformed Video", transformed)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
