from picamera2 import Picamera2 , Preview
import os
import pygame
import sys
import time

pygame.init()
res = (640, 480)
#if you want a separate pygame window
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Black Garlic Quality Classification System")

#if you want a full screen pygame window 
#screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)



picam2 = Picamera2()

preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
picam2.configure(preview_config)
picam2.start_preview(Preview.QTGL)

picam2.start()
time.sleep(10)

#picam2.close()

while True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()