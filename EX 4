import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check if image loaded
if img is None:
    print("Image not found")
    exit()

# Bigger image (2 times larger)
bigger = cv2.resize(img, None, fx=2, fy=2)

# Smaller image (half size)
smaller = cv2.resize(img, None, fx=0.5, fy=0.5)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Bigger Image", bigger)
cv2.imshow("Smaller Image", smaller)

cv2.waitKey(0)
cv2.destroyAllWindows()
