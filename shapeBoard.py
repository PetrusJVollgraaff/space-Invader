from ShipClasses import EnemyShip
class Enemylist:
    def __init__(self, lockedpos={}):
        self.EnemyArr =  [[0 for j in range(5)] for i in range(3)]
        print(self.EnemyArr)

    def buildArr(self):
        for i, line in enumerate(self.EnemyArr):
            y = (i+1) * 70
            for j, column in enumerate(line):
                x = (j + 1) * 70
                self.EnemyArr[i][j] = EnemyShip(x, y)

    def drawEnenies(self, win):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                if not enemyship.isHit:
                    enemyship.drawShip(win)

    def drawbullets(self, win):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                enemyship.drawbullets(win)

    def isEneniesHit(self, ship):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                if not enemyship.isHit:
                    ship.checkBulletHit(enemyship)