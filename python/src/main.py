import cv2
import numpy as np
 
img = cv2.imread('sample.png', -1)  #(-1: alpha, 0:グレー, 1:カラー)

img[:, :, 3] = np.where(np.all(img != 0, axis=-1), 0, 255)  # 白色のみTrueを返し、Alphaを0にする

cv2.imwrite('out.png', img)