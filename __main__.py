# __main__.py
import sys, os, pygame
from pygame.locals import *
from colours import *
from game import TicTacToe, playerNumToToken, flatList
SIZE = WIDTH, HEIGHT = 1000, 1000
FPS = 30
TITLE =  "Tic Tac Toe"
os.chdir(os.path.dirname(__file__))
AVG = lambda a, b : int(((a+b)/2))
class Game:
    def __init__(self):
        self._running = False
        self._display_surface = None
        self.size = self.width, self.height = SIZE
        self.spritesList = None
        self.ttt = TicTacToe()
        
    def initialise(self):
        try:
            pygame.init()
            self.font = pygame.font.Font('freesansbold.ttf', 35)
            self.topText = "Welcome, Player 1's Move"
            self._display_surface = pygame.display.set_mode(SIZE, pygame.DOUBLEBUF | pygame.HWSURFACE)
            pygame.display.set_caption(TITLE)
            self._fps = pygame.time.Clock()
            self.spritesList = pygame.sprite.Group()
            self.inGame = True
            # self.sprite = NewSPrite()
            # self.spritesList.add(self.sprite)
        except Exception as e:
            print("Error Occured")
            self._running = False
            raise(e)
        else:
            self._running = True
        return self._running
    def getSquare(self,pos):
        x, y = pos
        print(x,y)
        col = 0
        if x >= 50 and x < self.width//3:
            col = 1
        elif x >= self.width//3 and x < 2*self.width//3:
            col = 2
        elif x>= 2*self.width//3 and x < self.width-50:
            col = 3

        row = 0
        if y >= 150 and y < 100+(self.height-100)//3:
            row = 1
        elif y>= 100+(self.height-100)//3 and y < 100+(2*(self.height-100)//3):
            row = 2
        elif y>= 100+(2*(self.height-100)//3) and y < self.height-50:
            row = 3
        return (col, row)
    
    def eventHandler(self, event):
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_ESCAPE):
            self._running = False

        
            
        if self.inGame:
            if event.type == pygame.MOUSEBUTTONUP:
                x,y = square_clicked = self.getSquare(pygame.mouse.get_pos())
                if x != 0 and y != 0 and self.ttt.board[y-1][x-1] == 0:
                    self.ttt.board[y-1][x-1] = playerNumToToken(self.ttt.playerNum)
                    self.ttt.playerNum = 2 if self.ttt.playerNum == 1 else 1

                    self.ttt.display()
                    winner = self.ttt.check()
                  
                    if winner is not None:
                        self.win(winner)
                    else:

                        self.topText = f'Player {self.ttt.playerNum}\'s Move ({"red" if self.ttt.playerNum == 1 else "green"})'

    def win(self, winner):
        self.topText = f"Player {winner} won the game! " if winner != 3 else "Game Ended. Draw."
        print(self.topText)
        self.inGame = False
    def loop(self):
        self.spritesList.update()
        self._display_surface.fill(WHITE)
        self.drawBoardLines()
        self.drawTokens()
        # write whos go it is
                                                        # txt Color, Background Highlight
        
        text = self.font.render(self.topText, True, BLACK, WHITE)
        textRect = text.get_rect()
        textRect.center = (WIDTH // 2, 50)
        self._display_surface.blit(text, textRect)
        
        self.spritesList.draw(self._display_surface)
    
    def drawBoardLines(self):
        #vert
        pygame.draw.line(self._display_surface, BLACK, (self.width//3, 150), (self.width//3, self.height-50), 10)
        pygame.draw.line(self._display_surface, BLACK, (2*self.width//3, 150), (2*self.width//3, self.height-50), 10)


        # hor
        pygame.draw.line(self._display_surface, BLACK, (50, 100+((self.height-100)//3)), (self.width-50, 100+((self.height-100)//3)), 10) 
        pygame.draw.line(self._display_surface, BLACK, (50, 100+(2*(self.height-100)//3)), (self.width-50, 100+(2*(self.height-100)//3)), 10)
    def getCoords(self, pos):
        
        d = {
        0 : (AVG(50, self.width//3),
             AVG(150,  100+(self.height-100)//3)),
        1 : (AVG(self.width//3, 2*self.width//3),
              AVG(150,  100+(self.height-100)//3)),
        2: (AVG(2*self.width//3, self.width -50),
             AVG(150,  100+(self.height-100)//3)),
        3 : (AVG(50, self.width//3),
             AVG(100+(self.height-100)//3, 100+(2*(self.height-100)//3))),
        4: (AVG(self.width//3, 2*self.width//3),
             AVG(100+(self.height-100)//3, 100+(2*(self.height-100)//3))),
        5: (AVG(2*self.width//3, self.width -50),
            AVG(100+(self.height-100)//3, 100+(2*(self.height-100)//3))),
        6: (AVG(50, self.width//3),
            AVG(100+(2*(self.height-100)//3), self.height-50)),
        7:  (AVG(self.width//3, 2*self.width//3),
             AVG(100+(2*(self.height-100)//3), self.height-50)),
        8: (AVG(2*self.width//3, self.width -50),
             AVG(100+(2*(self.height-100)//3), self.height-50)),
            }
        print(d[pos])
        return d[pos]
    def drawTokens(self):
        # draw 
        for i, token in enumerate(flatList(self.ttt.board)):
            if token == 1:
                pygame.draw.circle(self._display_surface, RED, self.getCoords(i), 100, width=10)
            if token == 2:
                pygame.draw.circle(self._display_surface, GREEN, self.getCoords(i), 100, width=10)
    def render(self):
        pygame.display.flip()
        self._fps.tick(FPS)

    def start(self):
        if self.initialise() == False:
            self._running = False
        while self._running:
            self.render()
            for event in pygame.event.get():
                self.eventHandler(event)
            self.loop()
            
        
if __name__ == "__main__":
    game = Game()
    game.start()
