import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

# Translation values
tx = 100   # move right
ty = 50    # move down

# Translation matrix
T = np.float32([[1, 0, tx],
                [0, 1, ty]])

# Apply translation
moved = cv2.warpAffine(img, T, (img.shape[1], img.shape[0]))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Translated Image", moved)

cv2.waitKey(0)
cv2.destroyAllWindows()

