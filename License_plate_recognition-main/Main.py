import torch
import cv2
import os
import random
import sys
from Func_img2str import Img2Str
from Func_normalize import normalize
from Func_draw_boudingbox import drawBoundingBoxes
from Func_change_brightness import change_brightness
from Func_add_boder import add_boder

print(torch.cuda.is_available())

model = torch.hub.load('ultralytics/yolov5', 'custom', path='./best.pt') 
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(device)

#using when we have more than 1 device
#model.to(device)

def detect(img):
    results = model(img[:, :, ::-1] , size=640) #img[:, :, ::-1] because model run with BGR image
    for i in range(len(results.xyxy[0])):
        xmin, ymin, xmax, ymax, conf = results.xyxy[0][i][:-1].tolist()
        text = Img2Str(img[int(ymin):int(ymax), int(xmin):int(xmax)])
        try:
            text = normalize(text)
        except:
            text = ""
        if len(text) > 0:
            lb = str(round(conf, 2)) + ' ('+ text + ')'
        else:
            lb = str(round(conf, 2)) + " (Can't Detect!)"
        shape = list(img.shape)
        re_resize = cv2.resize(img, (shape[1]*2, shape[0]*2))
        img = drawBoundingBoxes(re_resize, int(xmin)*2, int(ymin)*2, int(xmax)*2, int(ymax)*2, color=(0, 255, 0), label=lb, thick=1)

    return img, len(text), str(round(conf, 2)), text

def Solve(img):
    try:
        img_detect, len_text, conf, lb = detect(img)
        img_yuv = cv2.cvtColor(img_detect, cv2.COLOR_BGR2YUV)
        img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
        img_detect = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
        return img_detect, len_text, conf, lb
    except:
        print("\n*Warning* Can't detect any License Plate!")
        exit()

os.system('cls')
print('Choose your image!')
import easygui
file = easygui.fileopenbox()
os.system('cls')
print("Image's path:", str(file))
print('\nDETECTING... \nUsing device: ' + str(torch.cuda.get_device_name(device)) + ' (' + str(torch.cuda.get_device_properties(device).total_memory) + ' bytes)')
try:
    img = cv2.imread(str(file))
except:
    print("*Warning* Incorrect image's path!")
    exit()

img_detect, len_text, conf, lb = Solve(img)

img1 = change_brightness(img, 50).astype('uint8')
img_detect1, len_text1, conf1, lb1 = Solve(img1)

img2 = change_brightness(img, -50).astype('uint8')
img_detect2, len_text2, conf2, lb2 = Solve(img2)

img3 = add_boder(img, 80, 80).astype('uint8')
img_detect3, len_text3, conf3, lb3 = Solve(img3)

l = [len_text, len_text1, len_text2, len_text3]
index = l.index(max(l))
if (index == 0):
    final = img_detect
    lb_final = lb
    conf_final = conf
elif (index == 1):
    final = img_detect1
    lb_final = lb1
    conf_final = conf1
elif (index == 2):
    final = img_detect2
    lb_final = lb2
    conf_final = conf2
else:
    final = img_detect3
    lb_final = lb3
    conf_final = conf3

if (len(sys.argv) > 1):
    if (sys.argv[1] == '1'):
        if (lb_final == ''):
                lb_final = 'null' + str(random.randint(0, 1000))
        cv2.imwrite('C:\\License_plate_reading\\Result\\' + lb_final + '.jpg', final)
        print('Your result was saved in: ' + 'C:\\License_plate_reading\\Result\\' + lb_final + '.jpg')
else:
    print("The result is unsaved!")

print('\n--- Result: ', lb_final, '(conf=' + conf_final + ')', '\n')
cv2.imshow(lb_final, final)
cv2.waitKey(delay=10000)
cv2.destroyAllWindows()
