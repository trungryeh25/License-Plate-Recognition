import random
import cv2

def add_boder(image, low, high):
    """
    low: kich thuoc bien thap nhat (pixel)
    hight: kich thuoc bien lon nhat (pixel)
    """
    # random cac kich thuoc bien trong khoang (low, high)
    top = random.randint(low, high)
    bottom = random.randint(low, high)
    left = random.randint(low, high)
    right = random.randint(low, high)

    original_width, original_height = image.shape[1], image.shape[0]

    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_REPLICATE)

    image = cv2.resize(image, (original_width, original_height))
    
    return image