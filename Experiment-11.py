import cv2
import numpy as np

# Read image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found")
    exit()

rows, cols = img.shape[:2]

# Source points (from original image)
src_pts = np.float32([[50,50], [200,50], [50,200], [200,200]])

# Destination points
dst_pts = np.float32([[10,100], [220,50], [100,250], [250,220]])

# Compute homography using DLT
H, status = cv2.findHomography(src_pts, dst_pts)

# Apply transformation
result = cv2.warpPerspective(img, H, (cols, rows))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("DLT Transformed Image", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
