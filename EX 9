import cv2
import numpy as np

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

rows, cols, ch = img.shape

# Four points in original image
pts1 = np.float32([[50,50], [200,50], [50,200], [200,200]])

# Four points in output image
pts2 = np.float32([[10,100], [200,50], [100,250], [200,200]])

# Perspective transformation matrix
M = cv2.getPerspectiveTransform(pts1, pts2)

# Apply perspective transformation
result = cv2.warpPerspective(img, M, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Perspective Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
