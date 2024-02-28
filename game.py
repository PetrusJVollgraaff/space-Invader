import pygame
from ShipClasses import SpaceShip, EnemyShip
from shapeBoard import Enemylist

pygame.font.init()

#Global vars
screen_width = 800
screen_height = 700
play_width = 300 #meaning 300 // 10 = 30 width per block
play_height = 600 #meaning 600 // 10 = 60 width per block
block_size = 30
rows = 20  # y
columns = 10  # x

top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height

def draw_text(win, text, color, top, left, font ):
    label = font.render(text, 1, color)

    win.blit(label, (top - (label.get_width()/2), left - (label.get_height()/2)) )

def end_screen(win, text):
    pygame.font.init()
    font = pygame.font.SysFont("comicsans", 80)
    txt = font.render(text,1, (255,0,0))
    win.blit(txt, (screen_width / 2 - txt.get_width() / 2, 300))
    pygame.display.update()

    pygame.time.set_timer(pygame.USEREVENT+1, 3000)

    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                run = False
            elif event.type == pygame.KEYDOWN:
                run = False
            elif event.type == pygame.USEREVENT+1:
                run = False

def score_board(win, score, color, top, left, font ):
    label = font.render("Score: " + str(score), 1, color)

    win.blit(label, (top, left))
def main(win):
    run = True
    ship = SpaceShip(screen_width//2, play_height - 70)
    font = pygame.font.SysFont('comicsans', 12)
    enemyships = Enemylist()
    clock = pygame.time.Clock()
    fly_time = 0
    fly_speed = 0.001
    enemyshoot_time = 0
    enemyshoot_speed = 1.9
    enemymove_time = 0
    enemymove_speed = 0.09
    enemyships.buildArr()
    score = 0

    while run:
        win.fill((0, 0, 0))
        score_board(win, score, (255,255,255), 0, 0, font)
        keys = pygame.key.get_pressed()
        fly_time += clock.get_rawtime()
        enemyshoot_time += clock.get_rawtime()
        enemymove_time  += clock.get_rawtime()
        clock.tick()

        if not ship.isHit:
            ship.drawShip(win)

        ship.drawbullets(win)

        enemyships.drawbullets(win)
        score = enemyships.isEneniesHit(ship, score)
        enemyships.drawEnenies(win)


        if enemymove_time / 1000 >= enemymove_speed:
            enemyships.EneniesMove(screen_width)
            enemymove_time = 0

        if enemyshoot_time / 1000 >= enemyshoot_speed:
            enemyships.EnimiesShoot(win)
            enemyshoot_time = 0

        if fly_time / 1000 >= fly_speed:
            ship.bulletmove("up", screen_height)
            enemyships.EnimiesBulletMove(screen_height)

            fly_time = 0

            if keys[pygame.K_LEFT] and ship.inSideScreen("left", screen_width):
                ship.moveShip("left")

            elif keys[pygame.K_RIGHT] and ship.inSideScreen("right", screen_width):
                ship.moveShip("right")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ship.shoot(win)

        if enemyships.isAllEneniesHit():
            end_screen(win, "You wins")
            run = False
        elif enemyships.EneniesWon(ship):
            end_screen(win, "You Lose")
            run = False

        pygame.display.update()