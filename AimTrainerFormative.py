###########################################
# Kelton Figurski
# Pygame Formative
# Aim Trainer
###########################################


# Imports modules
import random,pygame
from pygame.locals import *
import time


# Class for the target
class target:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        
    def position(self):
        xpos = random.randint(50, width - 50)
        ypos = random.randint(50, height - 50)
        
        return xpos,ypos
        

# ------------------ Variables ------------------- #

width = 960
height = 540

pygame.init()

backround = (238,223,204)
circle_color = (0,205,205)

win = pygame.display
display = win.set_mode((width, height))

shape = target(circle_color, 50)


# Function that draws and moves the circle
def circle():
    starttime = time.time()
    p = 20
    while p > 0:# Starts  a loop that completes 20 times
        p = p - 1
        q = False
        
        x,y = shape.position()


        pygame.draw.circle(display, shape.color, (x, y), shape.size ,0) # Draws a circle at a random spot
        win.update()
        
        #Loop that repeats until the user clicks  on the circle
        while True:
            for event in pygame.event.get():
            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = pygame.mouse.get_pos()
                    xmax = x + 50
                    xmin = x - 50
                    ymax = y + 50
                    ymin = y - 50
                    
                    if mx < xmax and mx > xmin and my < ymax and my > ymin:
                        display.fill(backround)
                        win.update()
                        q = True
                        break
                    

                    else:
                        continue
                    
                # Exits if the  user clicks the x
                if event.type == QUIT:
                    pygame.quit()
                    quit()
            
            if q == True:
                break
            
    #Finds the total time and average time
    endtime = time.time()
    totaltime = endtime - starttime
    timeper = totaltime/20
    
    endtime = time.time()
    totaltime = endtime - starttime
    timeper = totaltime/20
    
    totaltime = round(totaltime, 1)
    timeper = round(timeper, 3)
    
    print_time(totaltime, timeper)
    
    end()
    
 
# Function that ends the code
def end():
    time.sleep(5)
    quit()


# Function that prints the time on the screen
def print_time(totaltime, timeper):
    font = pygame.font.Font('freesansbold.ttf', 50)
    text = font.render(f"Total Time: {totaltime}s", True, circle_color, backround)
    text2 = font.render(f"Time Per Target: {timeper}s", True, circle_color, backround)
    textRect = text.get_rect()
    textRect2 = text2.get_rect()
    textRect.center = (960 // 2, 300)
    textRect2.center = (960 // 2, 200)
    
    display.blit(text, textRect)
    display.blit(text2, textRect2)
    win.update()


# Main Function
def main():
    win.set_caption("Aim Trainer")
    display.fill(backround)
    win.update()
    circle()


# ----------------Main Code ---------------- #

if __name__ == "__main__":
    main()
