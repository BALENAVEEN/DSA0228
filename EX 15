import cv2

# Read image in grayscale
img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found")
    exit()

# Sobel X
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)

# Sobel Y
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Combine X and Y
sobelxy = cv2.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sobel X", sobelx)
cv2.imshow("Sobel Y", sobely)
cv2.imshow("Sobel XY", sobelxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
