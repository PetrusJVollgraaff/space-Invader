import pygame

class ShipBullet:

    def __init__(self, x_axis, y_axis, color):
        self.x = x_axis
        self.y = y_axis
        self.didHit = False
        self.color = color

    def drawbullet(self, win):
        return pygame.draw.line(win, self.color, (self.x, self.y),
                         (self.x, self.y + 5))

class Ship:
    def __init__(self, x_axis, y_axis):
        self.x = x_axis
        self.y = y_axis
        self.isHit = False
        self.player = "enemy"
        self.bullet_list = []
        self.color = (255, 255, 255)

    def drawShip(self, win):
        pygame.draw.rect(win, self.color, (self.x - 2, self.y - 2, 64, 64))

    def moveShip(self, dir):
        if dir == "up":
            self.y -= 1

        if dir == "left":
            self.x -= 1

        if dir == "down":
            self.y += 1

        if dir == "right":
            self.x += 1

    def shoot(self, win):
        bulletcolor = (125,125,125)

        if self.player == "player":
            bulletcolor = (0, 255, 0)

        bullet = ShipBullet(self.x, self.y, bulletcolor)
        self.bullet_list.append( bullet )
        bullet.drawbullet(win)

    def drawbullets(self, win):
        for bullet in self.bullet_list:
            bullet.drawbullet( win )

    def bulletmove(self, dir):
        for bullet in self.bullet_list:
            if dir == 'up':
                bullet.y -= 1
            else:
                bullet.y += 1


class SpaceShip(Ship):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (255, 255, 255)
        self.player = "player"


class EnemyShip(Ship):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (255, 0, 0)
        self.player = "enemy"