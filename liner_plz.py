import cv2
import numpy as np

# image = np.zeros((200, 300), dtype=np.uint8)

# P1 = [10,20]
# P2 = [100,150]

# #cv2.line(image,P1,P2,(255,0,0),5)

# X = P1[0] - P2[1]
# Y = P1[1] - P2[0]

# def draw_line(image, X, Y, radius):
#     height, width = image.shape[:2]

# cv2.imshow("img",image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

def draw_line(image, P1, P2):
    x1, y1 = P1
    x2, y2 = P2
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    if dx > dy:
        steps = dx
    else:
        steps = dy
    x_increment = dx / steps
    y_increment = dy / steps
    x = x1
    y = y1
    for i in range(steps):
        image[int(y), int(x)] = 255
        x += x_increment
        y += y_increment

# สร้างภาพขนาด 200x300 เป็นภาพดำ
image = np.zeros((200, 300), dtype=np.uint8)

P1 = (10, 10)
P2 = (180, 180)
color = 255  # สีของเส้นตรง (ขาว)
thickness = 5  # ความหนาของเส้นตรง

# วาดเส้นตรงในภาพ
draw_line(image, P1, P2)

cv2.imshow("img", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

