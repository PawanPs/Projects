import cv2
import numpy as np

def view(x):
    #print(x)
    pass



img = np.zeros((312,512,3),np.uint8)
cv2.namedWindow('Color Selector')
cv2.createTrackbar('Red','Color Selector',0,255,view)
cv2.createTrackbar('Blue','Color Selector',0,255,view)
cv2.createTrackbar('Green','Color Selector',0,255,view)

font = cv2.FONT_HERSHEY_DUPLEX


while True:
    cv2.imshow('Color Selector',img)
    if cv2.waitKey(1) == ord('q'):
        break
    elif cv2.getWindowProperty('Color Selector',1) == -1:
        break
    Red = cv2.getTrackbarPos('Red','Color Selector')
    Blue = cv2.getTrackbarPos('Blue','Color Selector')
    Green = cv2.getTrackbarPos('Green','Color Selector')
    img[:] = [Blue,Green,Red]
    
    if (Blue+Green+Red) < 255:
        cv2.putText(img,'Red = {}'.format(Red), (25,200), font, 0.8, (255,255,255))
        cv2.putText(img,'Blue = {}'.format(Blue), (25,230), font, 0.8, (255,255,255))
        cv2.putText(img,'Green = {}'.format(Green), (25,260), font, 0.8, (255,255,255))
        cv2.putText(img,'#{:02x}{:02x}{:02x}'.format(Blue,Green,Red), (25,290), font, 0.8, (255,255,255))
    else:
        cv2.putText(img,'Red = {}'.format(Red), (25,200), font, 0.8, (0,0,0))
        cv2.putText(img,'Blue = {}'.format(Blue), (25,230), font, 0.8, (0,0,0))
        cv2.putText(img,'Green = {}'.format(Green), (25,260), font, 0.8, (0,0,0))
        cv2.putText(img,'#{:02x}{:02x}{:02x}'.format(Blue,Green,Red), (25,290), font, 0.8, (0,0,0))

cv2.destroyAllWindows()

