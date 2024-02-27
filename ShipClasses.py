import pygame

class ShipBullet:

    def __init__(self, x_axis, y_axis):
        self.x = x_axis
        self.y = y_axis
        self.didHit = False

    def drawbullet(self, win):
        return pygame.draw.line(win, (128, 128, 128), (self.x, self.y),
                         (self.x, self.y + 5))

class Ship:
    def __init__(self, x_axis, y_axis, ):
        self.x = x_axis
        self.y = y_axis
        self.isHit = False
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
        bullet = ShipBullet(self.x, self.y)
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


class EnemyShip(Ship):

    def __init__(self, x_axis, y_axis):
        super().__init__(x_axis, y_axis)
        self.color = (255, 0, 0)