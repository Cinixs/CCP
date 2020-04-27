#imports
import crayons
import getpass
import time
import os
import numpy as np
import cv2
from PIL import Image
import random

#welcome message
print(crayons.green("\n----------------------------------------\n"))
print(crayons.cyan(" Welcome to the Custom Command Prompt!"))
print(crayons.cyan(" Version 1.0.0. Update expected 26/04/20"))
print(crayons.yellow(" Please type your command or \"help\"\n"))
print(crayons.green("----------------------------------------\n"))


while True:
    user = getpass.getuser()
    cmd = input("C:/Users/" + user + ">")
    
    if cmd == "meme":
        print(crayons.green("\n The user is loading a meme...\n"))
        time.sleep(1)
        im_set = {"ignore\memes\LazarLazar.jpg", "ignore\memes\Yoda.jpg", "ignore\memes\Corona.jpg"}
        im = random.choice(tuple(im_set))
        imf = Image.open(im).show()
    elif cmd == "os " + cmd.strip("os "):
        os.system(cmd.strip("os "))

    elif cmd == "os":
        print(crayons.green("\n Please state an os command to be executed\n"))
    
    elif cmd == "say " + cmd.strip("say "):
        print(crayons.green(cmd.replace("say", "\n The user said")))
        print()
        

    elif cmd == "say":
        print(crayons.red("\nYou need to specify what should be said\n"))
        
    elif cmd == "exit":
        print(crayons.green("\n This Application will be terminated in 5 seconds..."))
        print(crayons.red(" If you have another command prompt open please EXIT THIS PROGRAM IMMEDIATELY"))
        print(crayons.green(" 5"))
        time.sleep(1)
        print(crayons.green(" 4"))
        time.sleep(1)
        print(crayons.green(" 3"))
        time.sleep(1)
        print(crayons.green(" 2"))
        time.sleep(1)
        print(crayons.green(" 1"))
        time.sleep(1)
        os.system("taskkill /im cmd.exe")
        
    elif cmd == "help":
        print(crayons.green("\n-----------------------------------------------------\n"))
        print(crayons.cyan("              Welcome to the Support Page!"))
        print(crayons.cyan(" Here is a list of all the commands currently avaliable"))
        print(crayons.green("\n-----------------------------------------------------\n"))

        print(" Command: capture\n\n Description: Records a clip\n Note: Press \"q\" when done\n\n")
        print(" Command: draw\n\n Description: Opens a photo editor\n Note: Double click to draw, press \"Ctrl\" + \"s\" to save, press \"esc\" to exit\n\n")
        print(" Command: exit\n\n Description: Exits this program\n Note: This command will terminate all applications with the name \"cmd.exe\"\n\n")
        print(" Command: help\n\n Description: Shows all the commands currently avaliable\n\n")
        print(" Command: meme\n\n Description: Shows a meme on the screen\n\n")
        print(" Command: os\n\n Description: Performs batch script to a certain extent\n\n")
        print(" Command: output\n\n Description: Plays the clip from the \"captures\" command\n Note: Press \"q\" when done\n\n")
        print(" Command: say\n\n Description: Says whatever the seccond argument is\n Note: Has to be 2 or more characters\n\n")
        
    elif cmd == "capture":
        cap = cv2.VideoCapture(0)

        print(crayons.green(" \n Starting Camera...\n Press \"q\" when done"))
        time.sleep(3)

        fourcc = cv2.VideoWriter_fourcc(*'DIVX')
        out = cv2.VideoWriter('ignore\output.mp4',fourcc, 20.0, (640,480))

        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret==True:
                out.write(frame)

                cv2.imshow('capture',frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        
    elif cmd == "output":

        def play_videoFile(filePath,mirror=False):
            out = "Output"
            cap = cv2.VideoCapture(filePath)
            cv2.namedWindow('Output',cv2.WINDOW_AUTOSIZE)
            while True:
                ret_val, frame = cap.read()
 
                if mirror:
                    frame = cv2.flip(frame, 1)
 
                cv2.imshow(out, frame)
 
                if cv2.waitKey(25) == 27:
                    break
 
            cv2.destroyAllWindows()
 
        def main():
            play_videoFile('ignore\output.mp4',mirror=False)
 
        if __name__ == '__main__':
            main()

    elif cmd == "draw":

        print(crayons.green(" \n Starting Photo Editor...\n Double click to draw, \"Ctrl\" + \"s\" to save \n Press \"esc\" when done\n"))
        time.sleep(3)

        def draw_circle(event,x,y,flags,param):
            if event == cv2.EVENT_LBUTTONDBLCLK:
                cv2.circle(img,(x,y),50,(255,0,0),-1)

        img = np.zeros((512,512,1), np.uint8)
        cv2.namedWindow('image')
        cv2.setMouseCallback('image',draw_circle)

        while(1):
            cv2.imshow('image',img)
            if cv2.waitKey(20) & 0xFF == 27:
                break
        cv2.destroyAllWindows()

    else:
        print(crayons.red("\n Invalid syntax\n"))
