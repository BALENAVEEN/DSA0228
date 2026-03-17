import cv2

# Capture video from webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam")
    exit()

print("Press 'q' to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Display video
    cv2.imshow("Webcam Video", frame)

    # Change delay to control speed
    delay = 30   # Normal speed
    # delay = 100  # Slow motion
    # delay = 5    # Fast motion

    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
