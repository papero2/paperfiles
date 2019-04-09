# -*- coding: utf-8 -*-
from Tkinter import *
from itertools import count
import Tkinter
import tkMessageBox
import math


size = 35
color1='royal blue'
color2='bisque3'

##board = ('.rnbqkbnr.'
##         '.pppppppp.'
##         '..........'
##         '..........'
##         '..........'
##         '..........'
##         '.PPPPPPPP.'
##         '.RNBQKBNR.')
board=('......K.r.'
         '.k......p.'
         '........P.'
         '....R..P..'
         '..........'
         '..........'
         '..........'
         '..........')

A = ['.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']    


directions = {
    'P': (-10, -20, -11, -9),
    'N': (21, 19, 12, 8, -21, -19, -12, -8),
    'B': (11, 9, -11, -9),
    'R': (10, 1, -1, -10),
    'Q': (10, 1, -1, -10, 11, 9, -11, -9),
    'K': (10, 1, -1, -10, 11, 9, -11, -9),
    'p': (10, 20, 11, 9),
    'n': (-21, -19, -12, -8, 21, 19, 12, 8),
    'b': (-11, -9, 11, 9),
    'r': (-10, -1, 1, 10),
    'q': (-10, -1, 1, 10, -11, -9, 11, 9),
    'k': (-10, -1, 1, 10, -11, -9, 11, 9)}


pst = {
    'P': (
        0, 198, 198, 198, 198, 198, 198, 198, 198, 0,
        0, 178, 198, 198, 198, 198, 198, 198, 178, 0,
        0, 178, 198, 198, 198, 198, 198, 198, 178, 0,
        0, 178, 198, 208, 218, 218, 208, 198, 178, 0,
        0, 178, 198, 218, 238, 238, 218, 198, 178, 0,
        0, 178, 198, 208, 218, 218, 208, 198, 178, 0,
        0, 178, 198, 198, 198, 198, 198, 198, 178, 0,
        0, 198, 198, 198, 198, 198, 198, 198, 198, 0),
    'B': (0, 797, 824, 817, 808, 808, 817, 824, 797, 0,
        0, 814, 841, 834, 825, 825, 834, 841, 814, 0,
        0, 818, 845, 838, 829, 829, 838, 845, 818, 0,
        0, 824, 851, 844, 835, 835, 844, 851, 824, 0,
        0, 827, 854, 847, 838, 838, 847, 854, 827, 0,
        0, 826, 853, 846, 837, 837, 846, 853, 826, 0,
        0, 817, 844, 837, 828, 828, 837, 844, 817, 0,
        0, 792, 819, 812, 803, 803, 812, 819, 792, 0),
    'N': (
        0, 627, 762, 786, 798, 798, 786, 762, 627, 0,
        0, 763, 798, 822, 834, 834, 822, 798, 763, 0,
        0, 817, 852, 876, 888, 888, 876, 852, 817, 0,
        0, 797, 832, 856, 868, 868, 856, 832, 797, 0,
        0, 799, 834, 858, 870, 870, 858, 834, 799, 0,
        0, 758, 793, 817, 829, 829, 817, 793, 758, 0,
        0, 739, 774, 798, 810, 810, 798, 774, 739, 0,
        0, 683, 718, 742, 754, 754, 742, 718, 683, 0),
    'R': (0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0,
        0, 1258, 1263, 1268, 1272, 1272, 1268, 1263, 1258, 0),
    'Q': (0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0,
        0, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 2529, 0),
    'K': (0, 60098, 60132, 60073, 60025, 60025, 60073, 60132, 60098, 0,
        0, 60119, 60153, 60094, 60046, 60025, 60094, 60153, 60119, 0,
        0, 60146, 60180, 60121, 60073, 60073, 60121, 60180, 60146, 0,
        0, 60173, 60207, 60148, 60100, 60100, 60148, 60207, 60173, 0,
        0, 60196, 60230, 60171, 60123, 60123, 60171, 60230, 60196, 0,
        0, 60224, 60258, 60199, 60151, 60151, 60199, 60258, 60224, 0,
        0, 60287, 60321, 60262, 60214, 60214, 60262, 60321, 60287, 0,
        0, 60298, 60332, 60273, 60225, 60225, 60273, 60332, 60298, 0)}

pst['p']=pst['P']
pst['n']=pst['N']
pst['b']=pst['B']
pst['r']=pst['R']
pst['q']=pst['Q']
pst['k']=pst['K']


top = Tkinter.Tk()
top.geometry('650x450')
f=Frame(top)
#f.columnconfigure(2, minsize=60)
c = Canvas(f)
c.configure(height=300, width=8*size)
queen = PhotoImage(file = "wqueen.gif")
t1 = Text(f, height=1, width=5)
t2 = Text(f, height=15, width=15)
images = [0]*80 

class Board:
    
    def __init__(self, board, score, turn, wc, bc):
      self.board = board
      self.score = score
      self.turn = turn
      self.wc = wc
      self.bc = bc
      self.attsq1 = [0]*80
      self.attsq2 = [0]*80
      self.images = images
      self.movenr = 0
      self.check = 0
      self.gameover = 0
      self.y1 = 0
      self.y2 = 0
      self.updateatt()
      self.wkingpos = 0
      self.bkingpos = 0
      
    def updateatt(self):
        self.attsq1=[[] for i in range(80)]
        self.attsq2=[[] for i in range (80)]
        for i, p in enumerate(self.board):
            if not p in 'pnkrbBRPNK': continue
            if p in 'pnbrqk':
                mypieces='pnbrqk'
                yourpieces='PNBRQK'
                pawn='p'
            elif p in 'PNBRQK':
                mypieces='PNBRQK'
                yourpieces='pnbrqk'
                pawn='P'
            self.score+=pst[p][i]
            for d in directions[p]:
                for j in count (i+d, d):
                    q = j
                    if q>78 or q<1 or (q)%10==0 or (q)%10==9:
                        break
                    if self.board[i]==pawn and d in (-10, -20, 10, 20): break
                    if p in 'PNBRQK':
                        self.attsq1[j].append(p)
                    if p in 'pnbrqk':
                        self.attsq2[j].append(p)
                    if p in 'PNKpnk' or self.board[q] in yourpieces: break
                    if self.board[q] in mypieces:
                        break      

        
    def move(self):
        score = 0
        bestscore = -60000
        x, y = 0, 0
        if self.turn==0:
            mypieces = 'PRNBQK'
            yourpieces = 'prnbqk'
        elif self.turn==1:
            mypieces = 'prnbqk'
            yourpieces = 'PRNBQK'
        for i, p in enumerate(self.board):
            if not p in mypieces: continue
            if p == 'K':
                self.wkingpos = i
                
            if p == 'k':
                self.bkingpos = i
            for d in directions[p]:
                for j in count (i+d, d):
                    q = j
                    if q>78 or q<1 or (q)%10==0 or (q)%10==9:
                        break
                    if self.board[q] in mypieces:
                        break
#                   pawn moves:
                    if self.board[i] in ('p', 'P') and d in (-10, -20, 10, 20) and self.board[q]!= '.': break
                    if self.board[i] in ('p', 'P') and d == -20 and (i>61 or self.board[i+d/2]!= '.'): break
                    if self.board[i] in ('p', 'P') and d == 20 and (i<28 or self.board[i+d/2]!= '.'): break
                    if self.board[i] in ('p', 'P') and d in (-11, -9, 11, 9) and self.board[q]== '.': break
                    
                    score = self.evaluate(i, q)
                    if (score > bestscore):
                        bestscore = score
                        x=i
                        y=j
                    if p in 'PNKpnk' or self.board[q] in yourpieces: break
# castle:
                    if (i == 78 and self.board[j+d] == 'K' and self.wc%10 == 0):
                        score = self.evaluate(i, q)+50
                        if (score > bestscore):
                            bestscore = score
                            x=i
                            y=j+d
                    if (i == 8 and self.board[j+d] == 'k' and self.bc%10 == 0):
                        score = self.evaluate(i, q)+50
                        if (score > bestscore):
                            bestscore = score
                            x=i
                            y=j+d

        if bestscore <= -50000:
            tkMessageBox.showinfo("Message:", "Checkmate!")
        self.play(x, y)
        print bestscore
        t1.delete(1.0, END)
        t1.insert(INSERT, ' %d' %self.score)
        

    def play (self, x, y):
        if self.gameover==0: 
# pawn promotion
            if self.board[x] in ('p', 'P'):
                if 1 <= y <= 8:
                    self.board[x]='Q'
                    c.delete(self.images[x])
                    self.images[x]=c.create_image((x%10)*size-17,size*(1+x//10)-17, image=queen, anchor="c")    
#              self.images[x]=c.createimage((i%10)*size-17,size*(1+i//10)-17, image=piece, anchor="c")   
# castle
            if self.board[x] == 'R' and self.board[y] == 'K':
                if x == 78:
                    c.move(self.images[x], -2*size, 0)
                    c.move(self.images[y], 2*size, 0)
                    self.board = self.board[:y] + '0' + self.board[x] + self.board[y] + '0'
                    self.wc=11
                    self.images[x-2]= self.images[x]
                    self.images[y+2]= self.images[y]
                    self.images[x]=0
                    self.images[y]=0
                elif x == 71:
                    c.move(self.images[x], 3*size, 0)
                    c.move(self.images[y], -2*size, 0)
                    self.board = self.board[:x] + '00' + self.board[y] + self.board[x] + '0' + self.board[y+1:]
                    self.wc=11
                    self.images[x+3]= self.images[x]
                    self.images[y-2]= self.images[y]
                    self.images[x]=0
                    self.images[y]=0
            if self.board[x] == 'r' and self.board[y] == 'k':
                if x == 8:
                    c.move(self.images[x], -2*size, 0)
                    c.move(self.images[y], 2*size, 0)
                    self.board = self.board[:y] + '0' + self.board[x] + self.board[y] + '0' + self.board[x+1:]
                    self.bc=11
                    self.images[x-2]= self.images[x]
                    self.images[y+2]= self.images[y]
                    self.images[x]=0
                    self.images[y]=0
                elif x == 1:
                    c.move(self.images[x], 3*size, 0)
                    c.move(self.images[y], -2*size, 0)
                    self.board = self.board[:x] + '00' + self.board[y] + self.board[x] + '0' + self.board[y+1:]
                    self.bc=11
                    self.images[x+3]= self.images[x]
                    self.images[y-2]= self.images[y]
                    self.images[x]=0
                    self.images[y]=0
            else:
                c.delete(self.images[y])
                c.move(self.images[x], ((y)%10-x%10)*size, ((y)//10-x//10)*size)
                self.images[y] = self.images[x]
                self.images[x]=0
                a = A[x%10]
                b = 8-x/10
                c1 = A[y%10]
                d = 8-y/10
                if x == 71: self.wc += 10
                if x == 78: self.wc += 1
                if x == 1: self.bc += 10
                if x == 8: self.bc += 1
                if self.board[x] == 'K': self.wc+=11
                if self.board[x] == 'k': self.bc+=11
                if self.board[y] in ('k', 'K'):
                    self.gameover=1
                    tkMessageBox.showinfo("Message:", "Game over!")

                self.board = self.board[:y] + self.board[x] + self.board[y+1:]
                self.board = self.board[:x] + '.' + self.board[x+1:]
                if self.turn==0:
                    self.movenr+=1
                self.updateatt()

                writemove(self.movenr, a, b, c1, d)

            self.turn = (self.turn+1)%2
            
        
    def evaluate(self, i, q):
        score = 0
        p = self.board[i]

# VANTAGGI:
# 1. aggiungi il valore del pezzo mangiato 
        if self.board[q] in 'pnbqkPNBQK':
            score+= pst[self.board[q]][q]
            
# 2. vai a donna
        if p in ('p', 'P'):
            if 1 <= q <= 8 or 71 <= q <= 78:
                score += 2350

# 3. migliora la posizione dei pezzi
        score += pst[p][q] - pst[p][i]

# SVANTAGGI:

# 1. non mettere il pezzo in presa
        board2 = self.board
        self.board = self.board[:q] + self.board[i] + self.board[q+1:]
        self.board = self.board[:i] + '.' + self.board[i+1:]
        self.updateatt()
        if self.turn==0 and self.attsq2[q]!=[]:
            score -= pst[p][q]
        if self.turn==1 and self.attsq1[q]!=[]:
            score -= pst[p][q]

# 2. soprattutto: non lasciare il re in presa
        if self.turn==0:
            print 'piff'
            if self.attsq2[self.wkingpos]!=[]:
                score-=60000
        if self.turn==1:
            print 'puff'
            print self.bkingpos
            if self.attsq1[self.bkingpos]!=[]:
                score-=60000

        self.board = board2
        return score


#########################################################################
# GUI
#########################################################################

def GUI():
    top.title("The Duck")

    rows = 8
    columns = 8


    for i in range(rows):
        for j in range(columns):
            if ((i+j)%2):
                c.create_rectangle(size*i, size*j, size*(i+1), size*(j+1), outline="black", fill="%s" %color1)
            else:
                c.create_rectangle(size*i, size*j, size*(i+1), size*(j+1), outline="black", fill="%s" %color2)

    pawn = PhotoImage(file = "GIF\pawn.gif")
    knight = PhotoImage(file = "wknight.gif")
    bishop = PhotoImage(file = "wbishop.gif")
    rook = PhotoImage(file = "wrook.gif")

    king = PhotoImage(file = "wking.gif")

    bpawn = PhotoImage(file = "bpawn.gif")
    bknight = PhotoImage(file = "bknight.gif")
    bbishop = PhotoImage(file = "bbishop.gif")
    brook = PhotoImage(file = "brook.gif")
    bqueen = PhotoImage(file = "bqueen.gif")
    bking = PhotoImage(file = "bking.gif")


    for i in range(len(board)):
        if (board[i]== '.'): continue
        if (board[i]== 'P'):
            piece = pawn
        elif (board[i]== 'p'):
            piece = bpawn
        elif (board[i]== 'R'):
            piece = rook
        elif (board[i]== 'N'):
            piece = knight
        elif (board[i]== 'B'):
            piece = bishop
        elif (board[i]== 'Q'):
            piece = queen
        elif (board[i]== 'K'):
            piece = king
        elif (board[i]== 'r'):
            piece = brook
        elif (board[i]== 'n'):
            piece = bknight
        elif (board[i]== 'b'):
            piece = bbishop
        elif (board[i]== 'q'):
            piece = bqueen
        elif (board[i]== 'k'):
            piece = bking
        pos.images[i]=c.create_image((i%10)*size-17,size*(1+i//10)-17, image=piece, tags="cip" , anchor="c")    
        c.tag_bind(pos.images[i], "<Button-1>", cip)  
        c.tag_bind(pos.images[i], "<ButtonRelease-1>", ciop)

    c.grid(row=0, column=0, rowspan=2, columnspan=2)

    l1 = Label(f, text="Game Notation")
    l1.grid(row=0, column=2, sticky=N, padx=20)
    
    t2.grid(row=1, column=2, sticky=N, padx=20)

    b1 = Button(f, text="MOVE", command = pos.move)
    b1.grid(row=3, column=1, sticky=N)

    l2 = Label(f, text="Computer evaluation")
    l2.grid(row=2, column=0, sticky=N)

    t1.grid(row=3, column=0, pady=3, sticky=N)
##    
##
    f.pack(pady=30)
    top.mainloop()


def cip(event):
        pos.y1 = event.x/35+1 + 10*(event.y/35)
def ciop(event):
        pos.y2 = event.x/35+1 + 10*(event.y/35)
        pos.play(pos.y1, pos.y2)
        pos.move()

def writemove(nr, a, b, c1, d):
    if pos.turn==0:
        t2.insert(INSERT, "  %d" %nr)
    t2.insert(INSERT, " %s%d%s%d" %(a, b, c1, d))
    if pos.turn==1:
        t2.insert(INSERT, "\n")

#########################################################################
# MAIN
#########################################################################


   
pos = Board(board, 0, 0, 0, 0)
GUI()

# problemi:
##1. board =
##        ('........K.'
##         '....p.....'
##         '..........'
##         '.....P....'
##         '..........'
##         '..........'
##         '.......pp.'
##         '..R....nk.')
##2. board = ('..........'
##         '...pp.ppp.'
##         '..........'
##         '...PP.P...'
##         '..p.....k.'
##         '..........'
##         '.PP....p..'
##         '.......K..')
##3. board = ('........K.'
##         '..........'
##         '.k.P......'
##         '........p.'
##         '..........'
##         '..........'
##         '..........'
##         '..........')
##4. board = ('..........'
##         '..........'
##         '.p.k......'
##         '.p..p.....'
##         '.P..P.....'
##         '......K...'
##         '..........'
##         '..........')
##4. board=('....B.....'
##         '.pP.....p.'
##         '.k......P.'
##         '..........'
##         '..........'
##         '..........'
##         '..........'
##         '.K........')
##5. board=('....k.K...'
##         '..P.......'
##         '.......PP.'
##         '...R......'
##         '..........'
##         '..........'
##         '..........'
##         '..........')

