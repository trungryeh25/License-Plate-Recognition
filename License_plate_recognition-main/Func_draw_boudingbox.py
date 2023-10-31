import cv2

def drawBoundingBoxes(imageData, left, top, right, bottom, color, label, thick):
    # left = xmin, top = ymin, right = xmax, bottom = ymax
    cv2.rectangle(imageData, (left, top), (right, bottom), color, thick)
    cv2.putText(imageData, label, (left, top-5), 0, 0.7, (0, 255, 50), 2)
    return imageData