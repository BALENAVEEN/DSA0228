import cv2

# Read image in grayscale
img = cv2.imread("image.jpg", 0)

if img is None:
    print("Image not found")
    exit()

# Apply Sobel edge detection along Y-axis
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Sobel Edge Detection (Y-axis)", sobely)

cv2.waitKey(0)
cv2.destroyAllWindows()
