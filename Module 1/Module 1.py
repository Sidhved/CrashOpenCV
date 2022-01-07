import cv2
import matplotlib.pyplot as plt

z_im = cv2.imread("Zendaya.jpg")

plt.imshow(z_im)
plt.title('matplotlib imshow')
plt.show()

window1 = cv2.namedWindow('w1')
cv2.imshow(window1, z_im)
cv2.waitKey(0)
cv2.destroyWindow(window1)

window2 = cv2.namedWindow('w2')
Alive = True
while Alive:
    cv2.imshow(window2, z_im)
    keypress = cv2.waitKey(1)
    if keypress == ord('q'):
        Alive = False
cv2.destroyWindow(window2)

cv2.destroyAllWindows()
stop = 1