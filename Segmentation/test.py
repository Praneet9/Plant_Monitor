import cv2
import numpy as np
from matplotlib import pyplot as plt
import matplotlib
import imutils
#%matplotlib inline #uncomment if in notebook

# def mask_leaf(im_name, external_mask=None):
#     og = cv2.imread(im_name)
#     im = cv2.imread(im_name)
#     im = cv2.blur(im, (3,3))

#     height, width = im.shape[:2]

#     mask = np.ones(im.shape[:2], dtype=np.uint8) * 2 #start all possible background
#     '''
#     #from docs:
#     0 GC_BGD defines an obvious background pixels.
#     1 GC_FGD defines an obvious foreground (object) pixel.
#     2 GC_PR_BGD defines a possible background pixel.
#     3 GC_PR_FGD defines a possible foreground pixel.
#     '''

#     #2 circles are "drawn" on mask. a smaller centered one I assume all pixels are definite foreground. a bigger circle, probably foreground.
#     r = 10
#     cv2.circle(mask, (int(width/2.), int(height/2.)), 2*r, 3, -3) #possible fg
#     #next 2 are greens...dark and bright to increase the number of fg pixels.
#     mask[(im[:,:,0] < 45) & (im[:,:,1] > 55) & (im[:,:,2] < 55)] = 1  #dark green
#     mask[(im[:,:,0] < 190) & (im[:,:,1] > 190) & (im[:,:,2] < 200)] = 1  #bright green
#     mask[(im[:,:,0] > 200) & (im[:,:,1] > 200) & (im[:,:,2] > 200) & (mask != 1)] = 0 #pretty white

#     cv2.circle(mask, (int(width/2.), int(height/2.)), r, 1, -3) #fg

#     #if you pass in an external mask derived from some other operation it is factored in here.
#     if external_mask is not None:
#         mask[external_mask == 1] = 1

#     bgdmodel = np.zeros((1,65), np.float64)
#     fgdmodel = np.zeros((1,65), np.float64)
#     cv2.grabCut(og, mask, None, bgdmodel, fgdmodel, 1, cv2.GC_INIT_WITH_MASK)

#     #show mask
#     plt.figure(figsize=(10,10))
#     plt.imshow(mask)
#     plt.show()

#     #mask image
#     mask2 = np.where((mask==1) + (mask==3), 255, 0).astype('uint8')
#     output = cv2.bitwise_and(og, og, mask=mask2)
#     plt.figure(figsize=(10,10))
#     plt.imshow(output)
#     plt.show()
#     cv2.imwrite('abc.jpg', output)

# mask_leaf('newcheck.jpeg', external_mask=None)




check = cv2.imread('newcheck.jpeg', 0)
canny = cv2.Canny(check, 30, 100)
canny = cv2.dilate(canny, None, iterations=2)
canny = cv2.resize(canny, (500, 500))
cnts = cv2.findContours(canny.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key=cv2.contourArea)

og = cv2.imread('newcheck.jpeg', 0)
og = cv2.resize(og, (500, 500))
cv2.drawContours(og, [c], -1, (0, 255, 255), 8)





cv2.imshow('title', og)
cv2.waitKey(0)
cv2.destroyAllWindows()