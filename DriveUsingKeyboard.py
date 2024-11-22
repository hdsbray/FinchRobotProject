'''See PyGame Events documentation for a list of the events built into pygame: https://www.pygame.org/docs/ref/event.html '''
from BirdBrain import Finch
import time
import pygame
myFinch = Finch('A')


myFinch.resetEncoders()


def main():
    #-----------------------------Setup------------------------------------------------------#
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surfaceSize = 480   # Desired physical surface size, in pixels.


    # Create surface of (width, height), and its window.
    mainSurface = pygame.display.set_mode((surfaceSize, surfaceSize))
   
   
    #-----------------------------Program Variable Initialization----------------------------#
    # Set up some data to describe a small circle and its color
    # Set up some data to describe a small circle and its color
    circlePos = [50,100]  #X and Y Values
    circleSize = 30  
    circleColor = (255, 0, 0)        # A color is a mix of (Red, Green, Blue)
    myFinch.setMotors(0,0)
    myFinch.setBeak(100, 100, 100)


    #-----------------------------Main Program Loop---------------------------------------------#
    while True:
        #-----------------------------Event Handling-----------------------------------------#


        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop
        elif ev.type == pygame.KEYDOWN:  #KEYDOWN has the attributes: key, mod, unicode, scancode
            if ev.key == pygame.K_UP:
                myFinch.setMotors(100,100)
                # myFinch.setMove('F', 10, 100)
            if ev.key == pygame.K_DOWN:
                myFinch.setMotors(-100,-100)
                # myFinch.setMove('B', 10, 100)
            if ev.key == pygame.K_RIGHT:
                myFinch.setMotors(100, 0)# myFinch.setTurn('R', 90, 100)
            if ev.key == pygame.K_LEFT:
                # myFinch.setTurn('L', 90, 100)
                myFinch.setMotors(0, 100)
        elif ev.type == pygame.KEYUP:
            myFinch.setMotors(0, 0)
       
        # myFinch.setDisplay([1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1])
        # myFinch.setMove('F', 100, 100)
        # time.sleep(2)
        # myFinch.setBeak(0, 0, 0)
        # myFinch.stop()
        # time.sleep(1)
        #-----------------------------Program Logic---------------------------------------------#
        # Update your game objects and data structures here...


        #-----------------------------Drawing Everything-------------------------------------#
        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        mainSurface.fill((0, 200, 255))


               
        # Draw a circle on the surface
        pygame.draw.circle(mainSurface, circleColor, circlePos, 20)


        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()


    pygame.quit()     # Once we leave the loop, close the window.


main()