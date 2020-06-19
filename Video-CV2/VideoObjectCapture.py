'''
- 抓取指定影片的前景輪廓。

'''

import cv2
import numpy as np

def mark_img(img):
    t_img = cv2.inRange(img, (100, 0, 0), (255, 90, 90))
    t_img = cv2.dilate(t_img, np.ones((15,40)))
    ct, th = cv2.findContours(t_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    for d in range(len(ct)):
        x, y, w, h = cv2.boundingRect(ct[d])
        if h > 20:
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    return img

source_video = cv2.VideoCapture("homework3.mp4")

while source_video.isOpened() == True:
    r, img = source_video.read()
    if r == True:
        cv2.imshow("Video", mark_img(img))
    else:
        break
    if cv2.waitKey(33) != -1:
        break

cv2.destroyAllWindows()