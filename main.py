import pygame
import game

def main_menu(win):
    run     = True
    font    = pygame.font.SysFont('comicsans', 60, bold=True)
    top     = game.top_left_x + game.play_width / 2
    left    = game.top_left_y + game.play_height / 2

    while run:
        win.fill((0, 0, 0))
        game.draw_text(win,"Press Any Key To Play", (255, 255, 255),  top, left, font)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                print("hello world")
                game.main(win)

    pygame.display.quit()


win = pygame.display.set_mode((game.screen_width, game.screen_height))
pygame.display.set_caption('Space Invader')

main_menu(win)  # start game