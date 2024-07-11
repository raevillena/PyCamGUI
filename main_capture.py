#!/usr/bin/python3
from picamera2 import Picamera2, Preview 
from libcamera import controls
import os
import time
import numpy as np

# folder path
dir_path = r'/home/admin/PyCamGUI/tmp/'


maxx = (4096, 2304)
max_half = (2048, 1152)
max_quarter = (1024,576)
full = (4608, 2592)
half = (2304, 1296)
quarter = (1152, 648)
picam2 = Picamera2()
config_capture = picam2.create_still_configuration(main={'size': full},
                                        buffer_count=3)


config_preview = picam2.create_preview_configuration({"size": maxx})


def cam_preview_show():
    picam2.configure(config_preview)
    picam2.start_preview(Preview.QTGL, x=0, y=0, width=800, height=400)
    picam2.start()
    picam2.set_controls({"AfMode":controls.AfModeEnum.Continuous,
                    "LensPosition":1.0,
                    "Brightness":0.1,
                    "AnalogueGain":1.0,
                    "Contrast":1.3
                    })
    overlay = np.zeros((300, 400, 4), dtype=np.uint8)
    overlay[:150, 200:] = (255, 0, 0, 64) # reddish
    overlay[150:, :200] = (0, 255, 0, 64) # greenish
    overlay[150:, 200:] = (0, 0, 255, 64) # blueish
    picam2.set_overlay(overlay)

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
                            "AnalogueGain":10,
                            "Contrast":1.3
                            })
    else:
        picam2.set_controls({"AfMode":controls.AfModeEnum.Continuous,
                            "LensPosition":1.0,
                            "Brightness":0.1,
                            "AnalogueGain":None,
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
                            "LensPosition":1.0,
                            "Brightness":0.1,
                            "AnalogueGain":1.0,
                            "Contrast":1.3
                            })
        print("UnPeeled settings applied")
        
    image_path = dir_path + os.urandom(5).hex() +".jpg"
    time.sleep(wait_time)
    picam2.switch_mode_and_capture_file(config_capture,image_path)

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