import cv2
import numpy as np
import pyautogui
import time
import gc

def click_image(image,pos,action,timestamp,offset=5):
    img = cv2.imread(image)
    height, width, channels = img.shape
    pyautogui.moveTo(pos[0] + offset, pos[1] + offset, timestamp)
    pyautogui.click(button=action)

def imagesearch(image, precision=0.8):
    im = pyautogui.screenshot()
    img_rgb = np.array(im)
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
    template = cv2.imread(image, 0)
    template.shape[::-1]

    res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if max_val < precision:
        return [-1,-1]
    return max_loc

if __name__ == '__main__':
    print("Otogi Click Start!")

    exe = True

    while exe == True:
        if(pyautogui.locateOnScreen("Battle.PNG") is None):
            pp = imagesearch("Next.PNG")
            click_image("./Next.PNG", pp, "left", 0.5)
            time.sleep(5)
            pp = imagesearch("Confirm.PNG")
            click_image("./Confirm.PNG", pp, "left", 0.5)
            time.sleep(30)
        

