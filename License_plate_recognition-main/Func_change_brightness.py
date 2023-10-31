import numpy as np

def change_brightness(image, value):
    """
    value: do sang thay doi
    """
    ones = np.ones(list(image.shape), dtype=int)
    lighter = image + ones * value

    temp = lighter.ravel()
    for i in range(len(temp)):
        if (temp[i] < 0): 
            temp[i] = 0
        if (temp[i] > 255):
            temp[i] = 255
    
    temp = temp.reshape(list(image.shape))
    
    return temp