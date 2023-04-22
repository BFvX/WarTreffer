# WarTreffer
A Yolov5 based WarThunder rangefinder. It's a very simple program just for fun and basically have no any value in the actual battle. If you Really want a extra rangfinder I would recommand you the one based on detecting the Suqard Mark.

## Theory and Usage
The basic principle of the program is to detect the enemy tank model in the screen by yolov5 and obtain the ratio of its pixel height to the pixel height of the whole game screen. Then the program will calculate the distance estimate of the identified tank based on the non-linear relationship between the distance and height ratio of the target under a priori fitted characteristic curve of the scope.  
It's quite familiar with using those custom sights with Height-Distance Baselines(sorry for not knowing their name) to measure, this program just automate this step.

## Deploy
1. Download the code file `measure.py` and requirement file `requirements.txt`
2. Install requirements by running `pip install -r requirements.txt` in your env
3. Download YOLOv5 source code or just run `git clone https://github.com/ultralytics/yolov5.git` in the same level as `measure.py`
4. Download the trained model best0.pt from the given link below, and put it in the same level as well
5. Run `python measure.py` and wait the program to initialize. If everything is fine, you shall see the line **Ready to GO** on the command line
6. Just use it! The DEFAULT parameter and Hotkey could be found from the source code since it's not a quite long code. A simple config file would be added in the near future 

## Maybe Important
You might need to change the graphics mode to fullscreen window to ensure the keyboard listener works fine.

## Model Download Link
