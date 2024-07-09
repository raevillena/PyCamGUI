#!/usr/bin/python3
from picamera2 import Picamera2, Preview
from libcamera import controls
import os
import time
import numpy as np


# folder path
dir_path = r'/home/admin/PyCamGUI/tmp/'
picam2 = Picamera2()

half = (2304,1296)
full = (4608, 2592)
config_capture = picam2.create_still_configuration(main={'size': full},
                                           buffer_count=3)

normalSize = (640, 480)
lowresSize = (320, 240)
config_preview = picam2.create_preview_configuration()

def cam_preview():
    picam2.configure(config_preview)
    picam2.start(show_preview=True)

def cam_capture_array(peeled=False):
    picam2.options["quality"] = 95

    if peeled:
        picam2.set_controls({"AfMode": controls.AfModeEnum.Manual,
                            #"AfMode":controls.AfModeEnum.Continuous,
                            "LensPosition":6.5,
                            "Brightness":0.1,
                            "AnalogueGain":10,#disabled when not closeup
                            "Contrast":1.3
                            })
    else:
        picam2.set_controls({"AfMode":controls.AfModeEnum.Continuous,
                            "Brightness":0.1,
                            "Contrast":1.3
                            })
        
    array = picam2.switch_mode_and_capture_array(config_capture, "main")
    return array

def cam_capture_file(peeled, wait_time):
    picam2.options["quality"] = 95

    if peeled:
        picam2.set_controls({"AfMode": controls.AfModeEnum.Manual,
                            #"AfMode":controls.AfModeEnum.Continuous,
                            "LensPosition":6.5,
                            "Brightness":0.1,
                            "AnalogueGain":10,#disabled when not closeup
                            "Contrast":1.3
                            })
        print("Peeled settings applied")
    else:
        picam2.set_controls({"AfMode":controls.AfModeEnum.Continuous,
                            "Brightness":0.1,
                            "Contrast":1.3
                            })
        print("UnPeeled settings applied")
        
    image_path = dir_path + os.urandom(5).hex() +".jpg"
    time.sleep(wait_time)
    picam2.switch_mode_and_capture_file(config_capture,image_path)
    picam2.switch_mode(config_preview)

    return image_path

def cam_stop():
    picam2.stop_preview()
    picam2.stop()


#picam2.capture_file(dir_path + last +".jpg")



#2304,1296
#4608, 2592

""" 
#unpeeled
picam2.set_controls({"AfMode":controls.AfModeEnum.Continuous,
                     "Brightness":0.1,
                     "Contrast":1.3
                    })

#peeled
picam2.set_controls({"AfMode": controls.AfModeEnum.Manual,
                     "LensPosition":6.5,
                     "Brightness":0.1,
                     "AnalogueGain":10,#disabled when not closeup
                     "Contrast":1.3
                    })
"""