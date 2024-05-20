from tkinter import *
from tkinter import messagebox
import random

# while tkinter will help in making whole board 
# random will help in getting random number of 2 that is needed in 2048 game

# making 2 classes 1.board 
class Board:
    bg_color={

        '2': '#eee4da',
        '4': '#ede0c8',
        '8': '#edc850',
        '16': '#edc53f',
        '32': '#f67c5f',
        '64': '#f65e3b',
        '128': '#edcf72',
        '256': '#edcc61',
        '512': '#f2b179',
        '1024': '#f59563',
        '2048': '#edc22e',
    }
    # colours taken from game source source
    # giving each grid number different background colour
    color={
        #giving colour to number 
        '2': '#776e65',
        '4': '#f9f6f2',
        '8': '#f9f6f2',
        '16': '#f9f6f2',
        '32': '#f9f6f2',
        '64': '#f9f6f2',
        '128': '#f9f6f2',
        '256': '#f9f6f2',
        '512': '#776e65',
        '1024': '#f9f6f2',
        '2048': '#f9f6f2',
    }
# init method is used as object of a class in python
    def __init__(self):
        self.n=4
    # creating window using tkinter
        self.window=Tk()
        # self.window.iconbitmap('images.ico')
    # giving title using tkinter 
        self.window.title('OSP project : 2048 game')
    
    # makinng a frame and giving it brown colour
        self.gameArea=Frame(self.window,bg= '#BBADA0')
   
    # making a list named board    
        self.board=[]
    
    #initialize a 4*4 grid with 0 
    # [0]*4 uses the multiplication operator to create a list with four 
    # elements, all of which are 0. The result is [0, 0, 0, 0].
    # The outer list comprehension collects these inner lists into a new
    # list, effectively creating a list of lists (a 2D list).
        self.gridCell=[[0]*4 for i in range(4)]
        
        self.compress=False
        self.merge=False
        self.moved=False
        self.score=0

        for i in range(4):
            rows=[]
            for j in range(4):
            
            #instead of l we can write any thing its just naming of label 
            #label follow master option syntax,here master is gamearea
            #option are there to just modify your given label
            #label can use (pack,grid,and place respectyively )
                l=Label(self.gameArea,text='',bg='azure4',
                font=('Helvetica',32,'bold'),width=6,height=3)
                l.grid(row=i,column=j,padx=7,pady=7)

            
            # adding label l to each row using append
                rows.append(l);
            
            #adding rows to self board
            self.board.append(rows)
        self.gameArea.grid()
