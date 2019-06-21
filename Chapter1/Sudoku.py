import math

class sudoku:
    def __init__(self, a):
        self.size = a
        self.nsquares = int(math.sqrt(a))
        self.sudoku = [[None for x in range(0, self.size)] for y in range (0, self.size)]
        self.numbers = [x for x in range(1, self.size + 1)]

    def __str__(self):
        s = ""
        for x in range(0,self.size):
            s = s + str(self.sudoku[x]) + "\n"
        return s

    def setPos(self, x, y, val):
        self.sudoku[x][y] = val

    def inLine(self, n, row):
        return n in self.sudoku[row]

    def inCol(self, n, col):
        for x in range(0,self.size):
            if n == self.sudoku[x][col]:
                return True
        return False

    def inSquare(self, n, startx, starty):
        for x in range(0, self.nsquares):
            for y in range(0, self.nsquares):
                if self.sudoku[x + startx][y + starty] == n:
                    return True
        return False

    def isValid(self, n, row, col):
        return not self.inSquare(n, row - row % self.nsquares, col - col % self.nsquares) and not self.inLine(n, row) \
               and not self.inCol(n, col)

    def findEmptyPos(self, l):
        for x in range(self.size):
            for y in range(self.size):
                if self.sudoku[x][y] is None:
                    l[0] = x
                    l[1] = y
                    return True
        return False

    def solver(self):
        #l will be a pair with the row and col of a free position (None)
        l = [0,0]
        #if no more empty positions, sudoku is solved.
        if (not self.findEmptyPos(l)):
            return True
        #if we get here, the sudoku is not full, so we get the values of an empty pos.
        row = l[0]
        col = l[1]

        #try for every number.
        for num in self.numbers:
            #check if the number is valid
            if self.isValid(num,row,col):
                #if it's valid, put the number
                self.sudoku[row][col] = num
                #check recursevly if the sudoku can be solved with the previous assignment
                if (self.solver()):
                    return True
                #if we get here, it means it can be solved with the previous assumption, so we empty the position again
                self.sudoku[row][col] = None
        return False

testSudoku = sudoku(4)
testSudoku.setPos(0,1,3)
testSudoku.setPos(0,2,4)
testSudoku.setPos(1,0,4)
testSudoku.setPos(1,3,2)
testSudoku.setPos(2,0,1)
testSudoku.setPos(2,3,3)
testSudoku.setPos(3,1,2)
testSudoku.setPos(3,2,1)
print(testSudoku)
testSudoku.solver()
print(testSudoku)