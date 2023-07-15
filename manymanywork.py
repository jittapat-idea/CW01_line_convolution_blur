import cv2
import numpy as np

# def draw_line(image, P1, P2):
#     x1, y1 = P1
#     x2, y2 = P2
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     if dx > dy:
#         steps = dx
#     else:
#         steps = dy
#     x_increment = dx / steps
#     y_increment = dy / steps
#     x = x1
#     y = y1
#     for i in range(steps):
#         image[int(y), int(x)] = 255
#         x += x_increment
#         y += y_increment

image = np.zeros((15, 15), dtype=np.uint8)

P1 = (0, 13)
P2 = (13,0 )
cv2.line(image, P1 , P2 , (255,255,255)) 
# วาดเส้นตรงในภาพ
#draw_line(image, P1, P2)

img = cv2.imread('pic/Gonzo.jpeg', cv2.IMREAD_GRAYSCALE)

line_image = image
# line_image_resized = cv2.resize(image, (15,15))
# print(image)
# kernel = np.where(image == 255, 1, 0).astype(np.float32)
kernel = np.zeros((10000,10000))
kernel = line_image
kernel = kernel/10000


output = cv2.filter2D(img, -1, kernel, borderType=cv2.BORDER_REFLECT)



cv2.imshow('Motion Blur', output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# cv2.imshow("img", image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()