import cv2
import numpy as np

img = cv2.imread('prova.jpg')

def grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def sharpening(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    return cv2.filter2D(img, -1, kernel)

def noise_red(img):
    return cv2.medianBlur(img, 5)
