from PIL import ImageGrab, ImageOps 
import pyautogui 
import time 
import numpy as np   
   
class coordinates(): 
    # Coordinates of the reset game button
    replaybutton = (515, 405)
    # Coordinates of the top-right corner of the dinosaur
    dinasaur = (300, 420) 
       
# Restart the game, by clicking the replay button
def restartGame():  
    pyautogui.click(coordinates.replaybutton)
    pyautogui.keyDown('down') 

# Make Dino jump 
def press_space(): 
    pyautogui.keyUp('down')  
    pyautogui.keyDown('space')
    # Press the key for a time so the dino jump for a while longer
    time.sleep(0.15) 
    pyautogui.keyUp('space') 
    pyautogui.keyDown('down') 
  
def imageGrab():
    # Defining the coordinates of hitbox in front of dinosaur  
    box = (
        coordinates.dinasaur[0]+30, coordinates.dinasaur[1], 
        coordinates.dinasaur[0]+120, coordinates.dinasaur[1]+2
    ) 
  
    # Grabbing all the pixels values in form of RGB tupples 
    image = ImageGrab.grab(box) 
  
    # Converting RGB to Grayscale to make processing easy and result faster
    grayImage = ImageOps.grayscale(image) 
  
    # Using numpy to get sum of all grayscale pixels
    pixels = np.array(grayImage.getcolors()) 
   
    print(pixels.sum())  
    return pixels.sum() 

# Restart the game on dinosaur die
restartGame()
while True:  
    # 427 is the sum of white pixels values of box. Represents that there are no obstacles
    if(imageGrab() != 427):    
        press_space()
        # Time to recognize the operation performed by above function  
        time.sleep(0.1)  
