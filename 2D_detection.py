import cv2
import main_loop

# Initiate variables
imgdir = "/home/pi/Desktop/Captures/"
imgprefix = "CapF"

# Initiate main loop
loop = main_loop.main_loop()

def ImageDetection():
    #Esc to quit, Space to Capture Image
    fullscreen = False
    # Set detect XYZ to False when capturing pictures (press spacebar)
    detectXYZ = True
    # Set calculateXYZ to enable real-world XYZ calculation
    calculateXYZ = True
    move_arm = False  # Set move_arm to False to disable the robotic arm
    loop.capturefromPiCamera(imgdir, imgprefix, fullscreen, detectXYZ, calculateXYZ, move_arm)

ImageDetection()
