# tic tac toe
x = 2
O = 1
_ = 0
INIT_BOARD = [
[_,_,_],
[_,_,_],
[_,_,_],
    ]

tokenToString = lambda col : "x" if col == x else "o" if col == O else "-"
playerNumToToken = lambda player_num  : O if player_num == 1 else x if player_num == 2 else _
listSameValues = lambda inList : True if len(set(inList)) == 1 else False
getColumn = lambda matrix, colNum : [row[colNum] for row in matrix]
flatList = lambda t : [item for sublist in t for item in sublist]
class TicTacToe:
    def __init__(self):
        self.playerNum = 1
        self.board = INIT_BOARD

        self.running = True
    def display(self):
     
        for i, [c1,c2,c3] in enumerate(self.board):
            
            print(f"{i+1} : {tokenToString(c1)}|{tokenToString(c2)}|{tokenToString(c3)}")

    def check(self):
        
        
    # horizontal
        for row in self.board:
            if row[0] != _ and listSameValues(row):
                return row[0]

    # vertical
        for col in [getColumn(self.board, x) for x, token in enumerate(self.board[0])]:
            if col[0] != _ and listSameValues(col):
                return col[0]
            
    # diagonal
        if (self.board[1][1] != _) and ((self.board[0][0] == self.board[1][1] == self.board[2][2]) or (self.board[0][2] == self.board[1][1] == self.board[2][0])):
            return self.board[1][1]

        if _ not in flatList(self.board):

            return 3
    

   


