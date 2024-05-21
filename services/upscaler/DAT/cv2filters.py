import cv2
import numpy as np


def grayscale(img: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def sharpening(img: np.ndarray) -> np.ndarray:
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    return cv2.filter2D(img, -1, kernel)

def noise_red(img: np.ndarray) -> np.ndarray:
    return cv2.medianBlur(img, 5)

def display_image(img):
    cv2.imshow('edited',img)
    cv2.waitKey(0)

