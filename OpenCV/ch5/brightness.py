import cv2
import numpy as np

def brightness():

    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = cv2.add(src, 100)

    cv2.imshow('img', src)
    cv2.imshow('image_plus',dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def brightness2():

    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = np.clip(src + 100., 0, 255).astype(np.uint8)

    cv2.imshow('img', src)
    cv2.imshow('image_plus',dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def saturated(value):
    if value > 255:
        value = 255
    elif value < 0:
        value = 0
    return value

def brightness3():

    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    dst = np.empty(src.shape, dtype=src.dtype)
    for y in range(src.shape[0]):
        for x in range(src.shape[1]):
            dst[y,x] = saturated(src[y,x]+100)

    cv2.imshow('img', src)
    cv2.imshow('image_plus',dst)
    cv2.waitKey()
    cv2.destroyAllWindows()

def brightness4():
    src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

    if src is None:
        print('Image load failed!')
        return

    def callback(pos):
        dst = cv2.add(src, pos)
        cv2.imshow('dst',dst)

    cv2.namedWindow('dst')
    cv2.createTrackbar('brightness5', 'dst', 0, 100, callback)
    callback(0)
    cv2.waitKey()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    brightness()
    brightness2()
    brightness3()
    brightness4()