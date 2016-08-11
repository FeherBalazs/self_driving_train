from picamera import PiCamera
from time import sleep

camera = PiCamera()

# Rotation
camera.rotation = 180

# Test View
#camera.start_preview()
#sleep(10)
#camera.stop_preview()

# Capture test_image
for i in range(400):
	camera.start_preview()
	sleep(0.05)
	camera.resolution = (320, 240)
	camera.capture('/home/pi/Documents/Train/data/stop_'+str(i)+'.jpg')
	camera.stop_preview()