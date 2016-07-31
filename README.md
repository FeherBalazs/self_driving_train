## Synopsis

This project is about building a proof of concept solution that uses a blackberry pi and its camera module to recognise images (signals along the train track), and to use it to control the behaviour of a toy train set.

## Installation

Requirements:

* Python 2.7
* Keras 1.0.4

For collecting training images for classification camera_non_stop_image_collect.py and camera_stop_image_collect.py should be installed to the raspberry pi. 

* copy to raspberry: e.g.: scp camera_stop_image_collect.py pi@192.168.0.27:Documents/Train
* copy from raspberry: e.g.: scp pi@192.168.0.27:Documents/Train/data/image* .data
* run the program for image collection on the pi: python camera_non_stop_image_collect.py

## License

MIT