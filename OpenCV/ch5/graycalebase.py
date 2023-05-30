import cv2
import numpy as np

def graycale1():
    img = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if img is None:
        print('Image load failed!')
        return

    img2 = np.zeros((480, 640), np.uint8)

    img3 = cv2.imread('lenna.bmp', cv2.IMREAD_COLOR)
    img4 = cv2.cvtColor(img3, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image1',img)
    cv2.imshow('image2',img2)
    cv2.imshow('image3',img3)
    cv2.imshow('image4',img4)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    graycale1()


