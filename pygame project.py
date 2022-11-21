import pygame
import time
import random
pygame.init()

BLACK = (   0,  0,  0)
WHITE = (   255,    255,    255)

GREY = (    100,    100,   100)

RED =(     200,    0,  0)
GREEN = (   0,  200,    0)
BLUE = (    0,  0,  200)

BROWN = (   200,    200,    0)
CYAN = (    0,   200,   200)
PINK = (    200,   0,  200)

RANGE = 1
RANGE1 = 100
RANGE2 = 115
RANGE3 = 155
RANGE4 = 160

screen_size = (800, 600)
width = screen_size[0]
height = screen_size[1]                                             #sets up the canvas

screen = pygame.display.set_mode(screen_size)

my_icon = pygame.image.load('pygame_project_icon.png')
pygame.display.set_icon(my_icon)

pygame.display.set_caption("Hamzah's pygame project")

collision_message = False
running = True
first_time = True
start = False
collision_timer = 0
x_speed = 0
y_speed = 0
sx_speed = 35
sy_speed = 30
x = int(width/2)
y = int(height/2)
RANGE = random.randint(1,2)
sx = 20
if RANGE == 1:
    sy = random.randint(RANGE1, RANGE2)
else:
    sy = random.randint(RANGE3, RANGE4)
clock = pygame.time.Clock()
screen.fill(GREY)
game_over = False
timer = 0

user_w = False
user_a = False
user_s = False
user_d = False
user_quit = False
user_mouse = False
s_collision = False
e_collision = False
anti_repeat = True

font = pygame.font.Font('C:\Windows\Fonts\Lsans.ttf', 19)

line1 = font.render('Hi, this is my very basic game where all you can do is move a ball around.', True, CYAN,)
line1Rect = line1.get_rect()
line1Rect.center = (width/2, height/2)

line2 = font.render('Touch the edge or that square and it will reset back to the middle.', True, CYAN,)
line2Rect = line2.get_rect()
line2Rect.center = (width/2, height/2 + 40)

line3 = font.render("Try to last as long as you can.", True, CYAN,)
line3Rect = line3.get_rect()
line3Rect.center = (width/2, height/2 + 80)

line4 = font.render("To start the game click on the screen.", True, CYAN,)                             #creates text to be displayed later
line4Rect = line4.get_rect()
line4Rect.center = (width/2, height/2 + 160) 

edge_message = font.render("You're being reset because you touched the edge.", True, CYAN,)
edge_messageRect = edge_message.get_rect()
edge_messageRect.center = (width/2, height/2)

square_message = font.render("You're being reset because you touched the square.", True, CYAN,)
square_messageRect = square_message.get_rect()
square_messageRect.center = (width/2, height/2 + 25)

retry_message = font.render("If you want to retry just click anywhere on the screen.", True, CYAN)
retry_messageRect = retry_message.get_rect()
retry_messageRect.center = (width/2, height/2 + 100)


while running:
    pygame.draw.rect(screen, GREY, (0, 0, width, height))
    mouse = pygame.mouse.get_pos()
    mouse_x = mouse[0]
    mouse_y = mouse[1]

    #main event loop:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("User aksed to quit.")
            running = False
            user_quit = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button.")
            user_mouse = True
            if first_time:
                print("The user has started the game.")
            first_time = False
            
        if (event.type==pygame.KEYDOWN):
            
            if (event.key==pygame.K_w):      #moves square up if w pressed, same for the other WASD keys below
                print("User is pressing the 'w' key.")
                user_w = True
            elif (event.key==pygame.K_a):
                print("User is pressing the 'a' key.")
                user_a = True
            elif (event.key==pygame.K_d):
                print("User is pressing the 'd' key.")

                user_d = True
            elif (event.key==pygame.K_s):
                print("User is pressing the 's' key")
                user_s = True
            else:
                print("User is pressing down a non-'wasd' key.")
      
      
        if (event.type==pygame.KEYUP):
            
            if (event.key==pygame.K_w):
                print("User let go of the 'w' key.")                                    #the ball stops moving when keys are lifted
                user_w = False
            elif (event.key==pygame.K_a):
                print("User let go of the 'a' key.")
                user_a = False
            elif (event.key==pygame.K_d):
                print("User let go of the 'd' key.")
                user_d = False
            elif (event.key==pygame.K_s):
                print("User let go of the 's' key.")
                user_s = False
            else:
                print("User stopped presseing a non-'wasd' key.")

    if game_over == False :
        #game logic should go here
        if first_time:
            screen.blit(line1, line1Rect)
            screen.blit(line2, line2Rect)                                              #creates an intro page
            screen.blit(line3, line3Rect)
            screen.blit(line4, line4Rect)
            pygame.display.flip()

        
        else:
            if (x <= 20) or (x >= 780) or (y <= 20) or (y >= 580):
                x = 400
                y = 300
                RANGE = random.randint(1, 2)
                sx = 20
                if RANGE == 1:
                    sy = random.randint(RANGE1, RANGE2)
                else:
                    sy = random.randint(RANGE3, RANGE4)
                print("User's ball touched the edge and had to be reset.")            #game over if user touches the edge
                e_collision = True
                game_over = True
            
            if (sx <= 0) or (sx >= 760):
                sx_speed = -sx_speed 
            if (sy <= 0) or (sy >= 560):
                sy_speed = -sy_speed
            
            if user_w == True:
                y_speed = -5
            if user_s == True:
                y_speed = 5
            if user_a == True:                                       #allows user to hold down keys instead of having to tap each frame
                x_speed = -5
            if user_d == True:
                x_speed = 5
                
            if user_w == False and user_s == False:
                y_speed = 0
            if user_a == False and user_d == False:
                x_speed = 0
            
            x += x_speed
            y += y_speed
            sx += sx_speed           #moves user and square
            sy += sy_speed


            #drawing code:    
                        

            user = pygame.draw.circle(screen, CYAN,(x,y),20,0)                          #user ball
            rect = pygame.draw.rect(screen, RED,(sx,sy,20,20),7)                        #square to avoid
            pygame.display.flip()

            if user.colliderect(rect):
                collision_message = True
                collision_timer = 0

            if collision_message:
                print("User touched the square and had to be reset.")                     #game over if user collides with square
                s_collision = True
                x = 400
                y = 300
                RANGE = random.randint(1, 2)
                sx = 20
                if RANGE == 1:
                    sy = random.randint(RANGE1, RANGE2)
                else:
                    sy = random.randint(RANGE3, RANGE4)
                game_over = True
                collision_message = False
        timer += 1/60
        if first_time == True:
            timer = 0
                
    elif game_over == True:
        timer = round(timer,3)
        if e_collision == True:
            screen.blit(edge_message, edge_messageRect)
        if s_collision == True:
            screen.blit(square_message, square_messageRect)
        time_message = font.render("You lasted " + str(timer) + " seconds.", True, RED)                 #gamer over screen, also
        time_messageRect = time_message.get_rect()                                                       #shows score in seconds lasted
        time_messageRect.center = (width/2, height/2 + 50)
        screen.blit(retry_message, retry_messageRect)
        screen.blit(time_message, time_messageRect)
        if anti_repeat == True:
            print("User lasted " + str(timer) + " seconds.")
        anti_repeat = False
        pygame.display.flip()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button.")
            game_over = False
            e_collision = False
            s_collision = False                                          #resets game if user clicks on screen
            timer = 0
            anti_repeat = True

    pygame.display.flip()
    clock.tick(60)

print("The program has been terminated.")
pygame.quit()                                                         #terminates program if user exits
time.sleep(2)
quit()
