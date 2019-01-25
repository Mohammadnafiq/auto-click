import pyautogui as pag
import time
import PIL.ImageGrab
import cv2 as cv

print("running click script . . . \n")


'''the below commented code describes how to move mouse pointer on the 768x1366 screen''' 

'''
pag.moveTo(100,150)
time.sleep(2)
pag.moveTo(1000,500)
'''

'''using the Python Image Library
we are taking a screengrab/screenshot
and storing it in im
NOTE: 'im' does not get stored as a matrix format'''

im = PIL.ImageGrab.grab()

'''the non matrix form 'im' gets stored on the drive'''

im.save("C:\\Users\\mukhe\\Desktop\\clicking the buttons python\\1.jpg")


'''the saved 'im' is now read off the disk into an image matrix
using the opencv library'''
'''NOTE: this does not seem like the most efficient way to
convert a screengrab/screenshot into an image matrix but will
have to figure that out at a later time'''

image = cv.imread("C:\\Users\\mukhe\\Desktop\\clicking the buttons python\\1.jpg")

'''finding the rows and coloumns for future image
processing/manipulation'''

row = len(image)
col = len(image[0])


'''writing the image matrix back onto the drive'''

cv.imwrite("C:\\Users\\mukhe\\Desktop\\clicking the buttons python\\3.jpg",image)

print("row: ",row," col: ",col);



print("script run ended . . .\n")

