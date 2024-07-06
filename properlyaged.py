#!/usr/bin/python3
from picamera2 import Picamera2
from libcamera import controls
import os
import time

mode = "properlyaged"

# folder path
dir_path = r'/home/admin/cam/properlyaged/'

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        buff = os.path.splitext(path)[0]
        res.append(buff)

#create a list of file names
res=list(map(int, res))
#determine the maximum
if res:
    maxnum=max(res)
else:
    maxnum=0

plusone=int(maxnum)+1
#convert to string for concatenation
last = str(plusone)
print(last)

picam2 = Picamera2()
picam2.options["quality"] = 95
#2304,1296
config = picam2.create_still_configuration(main={'size': (4608, 2592)},
                                           buffer_count=3)
picam2.configure(config)
picam2.start()
picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous,
#                     "AeFlickerMode":controls.AeFlickerModeEnum.Manual,
#                     "AeFlickerPeriod":21500,
                     "Brightness":0.1,
#                     "AnalogueGain":3,
                     "Contrast":1.3
                    })
time.sleep(2)
picam2.capture_file(dir_path + last +".jpg")
picam2.stop()

#***************************************************************************************
#check if the last file name is saved successfully

# list to store files
res = []

# Iterate directory
for path in os.listdir(dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_path, path)):
        buff = os.path.splitext(path)[0]
        res.append(buff)
#create a list of file names
res=list(map(int, res))
#determine the maximum
maxnum=max(res)
#+1 for the next file name to use
last2 = str(maxnum)
if last==last2:
    print("Successfully saved " + last+ ".jpg in properlyaged folder!")
else:
    print("ERROR Please try again!")