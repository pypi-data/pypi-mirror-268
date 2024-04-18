from VisionCraft.vision.utils import imRead, imShow 
import matplotlib.pyplot as plt
import numpy as np
from typing import Union, List


def pointDectection(img : np.ndarray = None, 
                    path : str = "",
                    THRESHOLD = 100,
                    show : bool = False,
                    height : int = 8, 
                    width : int = 10) -> Union[np.ndarray,None]:
    """
    Detects points in an image using a specific threshold-based technique.

    Args:
    - img (np.ndarray): The input image. If not provided, it will be read from the specified path.
    - path (str): The path to the image file if `img` is not provided.
    - THRESHOLD (int): The threshold value for point detection. Points with a sum of products greater than this threshold will be considered.
    - show (bool): If True, displays the original image and the point detection result using matplotlib.
    - height (int): Height of the displayed figure if `show` is True.
    - width (int): Width of the displayed figure if `show` is True.

    Returns:
    - np.ndarray or None: The resulting image after point detection, or None if the image loading fails.

    The point detection is based on the following algorithm:
    1. Convolution of the input image with a predefined mask.
    2. Thresholding the convolution result to identify points.

    The algorithm uses a 3x3 mask for convolution:
          |-1|-1|-1|
    mask =|-1|+8|-1|
          |-1|-1|-1|

    For each pixel in the input image, the sum of products of the mask coefficients and the corresponding grey level values of the image area covered by the mask is computed. If this sum exceeds the threshold value, the pixel is identified as a point.

    If `show` is True, the original image and the resulting image after point detection will be displayed using matplotlib.

    Example:
    result = pointDetection(img, THRESHOLD=120, show=True)
    """
    
    if img is None:
        img = imRead(path)
        if img is None:
            return img
    rows, cols = img.shape
    img1 = np.pad(img, pad_width=1, mode='constant', constant_values=255)
    filtered_img = np.zeros_like(img)
    mask = np.array([[-1,-1,-1],
                    [-1, 8,-1],
                    [-1,-1,-1]])
    for row in range(rows):
        for col in range(cols):
            replace = np.sum(img1[row:row+3, col:col+3] * mask)
            if replace > THRESHOLD:
                filtered_img[row,col]=  255
            else:
                filtered_img[row,col]=  0
    if show:
        plt.figure(figsize=(width, height))
        imShow("Original Image",img, subplot=True, row=1,col=2, num=1)
        imShow("Point Detection Image",filtered_img,subplot=True, row=1, col=2, num=2)
        plt.show()
    return filtered_img


def lineDetection(img : np.ndarray = None, 
                path : str = "",
                THRESHOLD = 100,
                show : bool = False,
                height : int = 8, 
                width : int = 10) ->List[Union[np.ndarray,None]]:
    
    """
    Detects lines in an image using multiple masks for horizontal, vertical, diagonal, and anti-diagonal directions.

    Args:
    - img (np.ndarray): The input image. If not provided, it will be read from the specified path.
    - path (str): The path to the image file if `img` is not provided.
    - THRESHOLD (int): The threshold value for line detection. Lines with a sum of products greater than this threshold will be considered.
    - show (bool): If True, displays the original image and the line detection results for different directions using matplotlib.
    - height (int): Height of the displayed figure if `show` is True.
    - width (int): Width of the displayed figure if `show` is True.

    Returns:
    - List[Union[np.ndarray, None]]: A list containing the resulting images after line detection for horizontal, vertical, diagonal, and anti-diagonal directions, and the merged result, in that order. If image loading fails, None is returned for the corresponding element.

    Line detection is performed using convolution with multiple masks:
    > Horizontal Mask:
        |-1|-1|-1|
        | 2| 2| 2|
        |-1|-1|-1|
    > Vertical Mask:
        |-1| 2|-1|
        |-1| 2|-1|
        |-1| 2|-1|
    > +45 Degree Mask:
        |-1|-1| 2|
        |-1| 2|-1|
        | 2|-1|-1|
    > -45 Degree Mask:
        | 2|-1|-1|
        |-1| 2|-1|
        |-1|-1| 2|

    For each direction, the algorithm convolves the input image with the corresponding mask and compares the result against the threshold value. Pixels with a sum of products greater than the threshold are identified as part of a line.

    If `show` is True, the original image and the resulting images after line detection for different directions, as well as the merged result, will be displayed using matplotlib.

    Example:
    results = lineDetection(img, THRESHOLD=120, show=True)
    """
    THRESHOLD = 100

    if img is None:
        img = imRead(path)
        if img is None:
            return img
        
    rows, cols = img.shape
    img1 = np.pad(img, pad_width=1, mode='constant', constant_values=255)
    filtered_img = np.zeros_like(img)

    horizontal_mask = np.array([[-1,-1,-1],
                                [ 2, 2, 2],
                                [-1,-1,-1]])

    vertical_mask = np.array([[-1, 2,-1],
                            [-1, 2,-1],
                            [-1, 2,-1]])
    # +45*
    deg45_mask = np.array([[-1,-1, 2],
                        [-1, 2,-1],
                        [ 2,-1,-1]])

    # -45*
    degn45_mask = np.array([[ 2,-1,-1],
                            [-1, 2,-1],
                            [-1,-1, 2]])
    masks = [horizontal_mask, vertical_mask, deg45_mask, degn45_mask]
    merged_img = np.zeros_like(img)
    output  = []

    for mask in masks:
        filtered_img = np.zeros_like(img)
        for row in range(rows):
            for col in range(cols):
                replace = np.sum(img1[row:row+3, col:col+3] * mask)
                if replace > THRESHOLD:
                    filtered_img[row,col]=  255
                    merged_img[row,col] = 255
                else:
                    filtered_img[row,col] =  0
        output.append(filtered_img)
    output.append(merged_img)
    
    if show:
        plt.figure(figsize=(width, height))
        imShow("Original Image",img, subplot=True, row=2,col=3, num=1)
        imShow("Horizontal Detection Image",output[0],subplot=True, row=2, col=3, num=2)
        imShow("Vertical Detection Image",output[1],subplot=True, row=2, col=3, num=3)
        imShow("+45 degree Detection Image",output[2],subplot=True, row=2, col=3, num=4)
        imShow("-45 degree Detection Image",output[3],subplot=True, row=2, col=3, num=5)
        imShow("Mixed Detection Image",merged_img,subplot=True, row=2, col=3, num=6)
        plt.show()
        
    return output

# TODO: Write its Funtion        
# img = imRead('/content/drive/MyDrive/dip_Images/Fig0354(a)(einstein_orig).tif')
# imShow("Original Image", img=img, subplot=True, row=1, col=2, num=1)
# delta = 3
# Tnew = np.min(img)+1
# while abs(T-Tnew) >= delta:
#     T = Tnew
#     rows, cols = img.shape
#     totalCells = rows*cols

#     G1 = []
#     G2 = []
#     for row in range(rows):
#         for col in range(cols):
#             if img[row][col] > T:
#                 G1.append(img[row][col])
#             else:
#                 G2.append(img[row][col])
#     m1 = np.mean(G1)
#     m2 = np.mean(G2)

#     Tnew = (m1+m2)/2
# for row in range(rows):
#     for col in range(cols):
#         if img[row][col] > T:
#             img[row][col] = 255
#         else:
#             img[row][col] = 0
# imShow("Global Thresholding",img=img, subplot=True, row=1, col=2, num=2)