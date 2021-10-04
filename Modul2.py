import cv2

img = cv2.imread("2.jpg", 0)
img_1 = 255 - img

cv2.imshow("Original", img)
cv2.imshow("Negative", img_1)

cv2.waitKey(0)
cv2.destroyAllWindows()
