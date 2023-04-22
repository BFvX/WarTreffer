import torch
import numpy as np
from cv2 import cvtColor, COLOR_BGR2RGB
from mss import mss
import time

from pynput import keyboard

def measure_distance():
    start_time = time.time()
    
    sct = mss()
    bounding_box = {'top': 450, 'left': 810, 'width': 300, 'height': 180}
    sct_img = sct.grab(bounding_box)
    scr_img = np.array(sct_img)
    scr_img = cvtColor(scr_img, COLOR_BGR2RGB)
    sct_img = model(scr_img)
    # scr_img.show()
    
    result = sct_img.xywhn
    if not result[0].size(0):
        print("No target detected")
    else:
        tar_h = result[0][0][3].item() * bounding_box['height'] / 1080  # screen height
        distance = -309.16 * np.log( 6.4239 * ( -0.0137 + tar_h ))  # not specified
        print("distance: ", distance)
    
    end_time = time.time()
    print("total_time: ", end_time - start_time, 's')

# 定义一个函数，当按键释放时执行
def on_release(key):
    # 如果按键是'`'，则打印一段消息
    try:
        if key.char == '`':
            measure_distance()
    # 如果按键是ctrl+c，退出程序
    except:
        pass

def on_press(key):
    if str(key) == r"<48>":
        quit()


if __name__ == "__main__":
    print("Initializing...")
    # 创建一个监听器
    model = torch.hub.load("../yolov5", 'custom', './best0.pt', source='local')
    
    listener = keyboard.Listener(on_release=on_release, on_press=on_press)
    listener.start()
    
    print("Ready to GO")
    
    # 等待监听器停止
    listener.join()
  