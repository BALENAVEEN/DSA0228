import cv2

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Get image height and width
(h, w) = img.shape[:2]

# Find center of image
center = (w // 2, h // 2)

# Counter-clockwise rotation (45 degrees)
M1 = cv2.getRotationMatrix2D(center, 45, 1.0)
ccw = cv2.warpAffine(img, M1, (w, h))

# Clockwise rotation (-45 degrees)
M2 = cv2.getRotationMatrix2D(center, -45, 1.0)
cw = cv2.warpAffine(img, M2, (w, h))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Counter Clockwise Rotation", ccw)
cv2.imshow("Clockwise Rotation", cw)

cv2.waitKey(0)
cv2.destroyAllWindows()
