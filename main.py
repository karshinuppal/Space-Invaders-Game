import pygame
import random
import math

# this is for pygame to work
pygame.init()

# this will create a display screen
screen = pygame.display.set_mode((650, 500))

# this is for adding background
bg = pygame.image.load('5512626.jpg')
bg1 = pygame.transform.scale(bg, (650, 500))

# this is for setting game name and icon associated with the game
pygame.display.set_caption("SPACE INVADERS")
icon = pygame.image.load('console.png')
pygame.display.set_icon(icon)

# used for adding image to the screen
spaceship = pygame.image.load('spaceship.png')
x = 290
y = 380
xchange = 0


# for adding spaceship to the screen
def spaceship1(x1, y1):
    screen.blit(spaceship, (x1, y1))


# this will be defining the enemies
enemy = []
xp = []
yp = []
xpchange = []
ypchange = []
no_of_enemy = 5

# for loading all the enemy onto the game screen
for j in range(no_of_enemy):
    enemy.append(pygame.image.load('alien (1).png'))
    xp.append(random.randint(0, 628))
    yp.append(random.randint(5, 90))
    xpchange.append(0.2)
    ypchange.append(20)


# for adding all the enemies to the game screen
def enemy1(x1, y1, j):
    screen.blit(enemy[j], (x1, y1))


# defining the bullets
bullet = pygame.image.load('bullets.png')
xbullet = 0
ybullet = 380
xwchange = 0
ywchange = 0.7
bullet_state = "pause"


# adding the bullets
def shoot_bullet(x, y):
    global bullet_state
    bullet_state = "shoot"
    screen.blit(bullet, (x + 16, y + 10))


# score value is set to zero in the begining
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 20)  # font is added which is already available with pycharm
# text size is defined
textx = 10
texty = 10


# shows the score
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 0))
    screen.blit(score, (x, y))


# game over
finish = pygame.font.Font('freesansbold.ttf', 65)


# game over text shows on the screen using this function
def game_over():
    finished = finish.render("GAME OVER", True, (255, 255, 0))
    screen.blit(finished, (135, 210))


# collision is definied between bullet and enemy
def collision(xp, yp, xbullet, ybullet):
    dist = math.sqrt((math.pow(xp - xbullet, 2)) + (math.pow(yp - ybullet, 2)))
    if dist < 27:
        return True
    else:
        return False


# while all of this is true the code will keep on running unless and until the game ends or we press the cross button
run = True
while run:

    screen.blit(bg1, (0, 0))

    # now for holding the screen as much longer as we want we'll run this part
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

        # all the required keys are defined
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                xchange = -0.7
            if i.key == pygame.K_RIGHT:
                xchange = 0.7
            if i.key == pygame.K_SPACE:
                if bullet_state is "pause":
                    xbullet = x
                    shoot_bullet(xbullet, ybullet)
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                xchange = 0

    # so that the spaceship is not going out of the screen(defined earlier)
    x += xchange
    if x <= 0:
        x = 0
    elif x >= 586:
        x = 586

    # enemy moment

    for j in range(no_of_enemy):

        # game over
        if yp[j] > 350:
            for k in range(no_of_enemy):
                yp[k] = 2000
            game_over()
            break
        # enemy moment:increase of speed etc
        xp[j] += xpchange[j]
        if xp[j] <= 0:
            xpchange[j] = 0.15
            yp[j] += ypchange[j]
        elif xp[j] >= 586:
            xpchange[j] = -0.15
            yp[j] += ypchange[j]

        # this will help in collision and resetting the value of bullet
        col = collision(xp[j], yp[j], xbullet, ybullet)
        if col:
            ybullet = 380
            bullet_state = "pause"
            score_value += 1
            xp[j] = random.randint(0, 628)
            yp[j] = random.randint(5, 150)

        enemy1(xp[j], yp[j], j)

    # this will help us with the bullet moment
    if ybullet <= 0:
        ybullet = 380
        bullet_state = "pause"

    if bullet_state is "shoot":
        shoot_bullet(xbullet, ybullet)
        ybullet -= ywchange

    spaceship1(x, y)
    show_score(textx, texty)
    pygame.display.update()
