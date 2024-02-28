import pygame

class ShipBullet:

    def __init__(self, x_axis, y_axis, color):
        self.x = x_axis
        self.y = y_axis
        self.color = color

    def drawbullet(self, win):
        return pygame.draw.line(win, self.color, (self.x, self.y),
                         (self.x, self.y + 5))

    def size(self):
        return ( (self.x, self.y), (1, 5))

class Ship:
    def __init__(self, x_axis, y_axis):
        self.x = x_axis
        self.y = y_axis
        self.isHit = False
        self.player = "enemy"
        self.bullet_list = []
        self.color = (255, 255, 255)
        self.shipsize = (40,40)

    def size(self):
        return ( (self.x, self.y), self.shipsize)
    def drawShip(self, win):
        pygame.draw.rect(win, self.color, (self.x - 2, self.y - 2, self.shipsize[0], self.shipsize[1]))

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

    def checkBulletHit(self, ship):
        for i, bullet in enumerate(self.bullet_list):
            if self.collides(ship.size(), bullet.size()):
                ship.isHit = True
                del self.bullet_list[i]

    def collides(self, rect1, rect2):
        r1x = rect1[0][0]
        r1y = rect1[0][1]

        r2x = rect2[0][0]
        r2y = rect2[0][1]

        r1w = rect1[1][0]
        r1h = rect1[1][1]

        r2w = rect2[1][0]
        r2h = rect2[1][1]

        if (r1x < (r2x + r2w) and (r1x + r1w) > r2x and r1y < (r2y + r2h) and (r1y + r1h) > r2y):
            return True
        else:
            return False

    def inSideScreen(self, dir, screen_width):
        if self.x >= 6 and dir == "left":
            return True
        elif (self.x + self.shipsize[0]) <= screen_width - 6 and dir == "right":
            return True

        return False

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
