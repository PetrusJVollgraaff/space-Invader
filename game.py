import pygame
from ShipClasses import SpaceShip, EnemyShip

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


def main(win):
    run             = True
    ship = SpaceShip(screen_width//2, play_height - 70)
    enemyship = EnemyShip(screen_width // 2, 70)
    clock = pygame.time.Clock()
    fly_time = 0
    fly_speed = 0.001

    while run:
        win.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        fly_time += clock.get_rawtime()
        clock.tick()

        if not ship.isHit:
            ship.drawShip(win)

        ship.drawbullets(win)
        ship.checkBulletHit(enemyship)

        if not enemyship.isHit:
            enemyship.drawShip(win)


        #enemyship.drawbullets(win)

        if fly_time / 1000 >= fly_speed:
            ship.bulletmove("up")
            fly_time = 0
            if keys[pygame.K_LEFT]:
                ship.moveShip("left")

            elif keys[pygame.K_RIGHT]:
                ship.moveShip("right")

            '''elif keys[pygame.K_UP]:
                ship.moveShip("up")

            elif keys[pygame.K_DOWN]:
                ship.moveShip("down")
            '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ship.shoot(win)

        pygame.display.update()