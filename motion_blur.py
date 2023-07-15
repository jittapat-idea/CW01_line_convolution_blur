import cv2
import numpy as np

img = cv2.imread('pic/Gonzo.jpeg', cv2.IMREAD_GRAYSCALE)

size = 15
angle = 45  # องศาของเส้นตรงที่ต้องการให้เกิด Motion Blur

# สร้างภาพขาวดำที่เป็นเส้นตรงที่กำหนดองศา
line_image = np.zeros((size, size), dtype=np.uint8)
cv2.line(line_image, (0, int(size / 2)), (size - 1, int(size / 2)), 255, 1)
M = cv2.getRotationMatrix2D((size / 2, size / 2), angle, 1)
line_image = cv2.warpAffine(line_image, M, (size, size))

# แปลงภาพเป็น kernel โดยปรับค่าจากขาวเป็นค่าที่ใช้ในการคำนวณ
kernel_motion_blur = line_image.astype(np.float32) / 255

# ทำการทำ convolution กับภาพโดยใช้ kernel ที่กำหนด
output = cv2.filter2D(img, -1, kernel_motion_blur, borderType=cv2.BORDER_REFLECT)

cv2.imshow('Motion Blur', output)
cv2.waitKey(0)
cv2.destroyAllWindows()





