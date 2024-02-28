import random
from ShipClasses import EnemyShip
class Enemylist:
    def __init__(self):
        self.row = 3
        self.column = 5
        self.EnemyArr = [[0 for j in range(self.column)] for i in range(self.row)]
        self.TotalShip = 15
        self.move = "left"
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

    def EneniesMove(self, screen_width):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                if enemyship.inSideScreen(self.move, screen_width):
                    enemyship.moveShip(self.move)
                else:
                    if self.move == "right":
                        self.move = "left"
                    else:
                        self.move = "right"

    def drawbullets(self, win):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                enemyship.drawbullets(win)


    def isEneniesHit(self, ship):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                if not enemyship.isHit:
                    ship.checkBulletHit(enemyship)
                    if enemyship.isHit:
                        self.TotalShip -= 1

    def isAllEneniesHit(self):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                if not enemyship.isHit:
                    return False
        return True

    def EnimiesShoot(self, win):
        shipsshoot = []
        totalship = random.randint(1, self.TotalShip)
        ships = [(row, col) for row in range(self.row) for col in range(self.column) if not self.EnemyArr[row][col].isHit]

        for i in range(totalship):
            shipsselect = random.choice(ships)
            if not shipsselect in shipsshoot:
                shipsshoot.append( shipsselect )

        for j in shipsshoot:
            if not self.EnemyArr[j[0]][j[1]].isHit:
                self.EnemyArr[j[0]][j[1]].shoot(win)

    def EnimiesBulletMove(self):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                enemyship.bulletmove("down")

    def EneniesWon(self, ship):
        for i, line in enumerate(self.EnemyArr):
            for j, enemyship in enumerate(line):
                if not ship.isHit:
                    enemyship.checkBulletHit(ship)
                    if ship.isHit:
                        return True

        return False