#!/usr/bin/env python
# coding: utf-8

class Piece:
    
    def __init__(self, piece, side, a=None, b=None):
        self._cpi = piece
        self._csi = side
        self._ca = a
        self._cb = b
        
    def files(self): return self._ca
    def ranks(self): return self._cb
    def pieces(self): return self._cpi
    def side(self): return self._csi
        
    def onboard(self, a, b):
        self._ca = a
        self._cb = b
    
    def transform(self, piece):
        self._cpi = piece
    
    def __str__(self):
        result = str(self._csi) + ' ' + str(self._cpi)
        return result

#====================================================================
#====================================================================

class ChPiece(Piece):
    
    #Игровая доска в виде списка (сhboard)
    board1 = ['A','B','C','D','E','F','G','H']
    board2 = ['8','7','6','5','4','3','2','1']
    chboard = [[],[],[],[],[],[],[],[]]
    for i in range(8):
        for j in range(8):
            chboard[j] += [board1[i]+board2[j]]
    
    dboard = {}
    for i in range(len(chboard)):
        for j in range(len(chboard)):
            dboard[str(chboard[i][j])] = (j, i)

    def __init__(self, piece, side, cage=None):
        Piece.__init__(self, piece, side)
        self._cage = cage

    #Превратить фигуру на шахматной доске в абстрактную фигуру
    def transition(self):
        x = dboard.get(self._cage)
        return Piece(self._cpi, self._csi, x[0], x[1])
    
    def chmove(self, x):
        self._cage = x
    
    def __str__(self):
        result = str(self._csi) + ' ' + str(self._cpi) + ' ' + str(self._cage)
        return result
    
#====================================================================
#====================================================================

def detransition(x):
        if isinstance(x, Piece):
            a = (x.files(), x.ranks())
            b = (list(dboard.keys())[list(dboard.values()).index(a)])
            return ChPiece(x.pieces(), x.side(), b)

if __name__ == '__main__':
    x = ChPiece('pawn', 'white', 'A1')
    print(x)
    x.chmove('A2')
    print(x)
    x.chmove(None)
    print(x)


