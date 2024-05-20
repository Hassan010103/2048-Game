import Structure_of_game
# ALL FUNCTIONS THAT WILL BE USED

#The method reverse is defined as a part of a class.
#It takes only one parameter, self, which refers to the instance of the class.
    def reverse(self):
        
# This loop iterates over the indices of the rows in the grid.
# ind takes values from 0 to 3, representing each row index.        
        for ind in range(4):
            i=0
            j=3
            while(i<j):
                self.gridCell[ind][i],self.gridCell[ind][j]=self.gridCell[ind][j],self.gridCell[ind][i]
                i+=1
                j-=1

    def transpose(self):
        self.gridCell = [[self.gridCell[j][i] for j in range(4)] for i in range(4)]






#function for compression
#the functionality of compress function is to bring all numbers to corner for merging
    def compressGrid(self):

#self.compress = False: This initializes a flag compress to False. This flag will be set to True if any tile is moved during compression. 
        self.compress=False

#temp = [[0] * 4 for i in range(4)]: This creates a temporary 4x4 grid temp filled with zeros. This grid will be used to build the compressed version of self.gridCell.
        temp=[[0] *4 for i in range(4)]

#The outer loop iterates through each row of the grid. i takes values from 0 to 3, representing row indices. 
        for i in range(4):

#cnt = 0: A counter cnt is initialized to keep track of the position in the temp grid where the next non-zero tile should be placed. 
            cnt=0
            
 # iterating through inner loop 
            for j in range(4):

# this particular condition chaeck if tile is non zero 
                if self.gridCell[i][j]!=0:

# (((((if tile is non zero))))temp[i][cnt] = self.gridCell[i][j]: The non-zero tile is copied to the next available position in the temp grid.
                    temp[i][cnt]=self.gridCell[i][j]
                    
#if cnt != j: This condition checks if the tile has moved (i.e., if the destination position cnt is different from the original position j).
                    if cnt!=j:
                        self.compress=True
#if cnt is moved it is incremented 
                    cnt+=1

# After all rows and columns have been processed, self.gridCell is updated to be the temp grid
        self.gridCell=temp



# functionality of merge function
# This initializes a flag merge to False. This flag will be set to True if any tiles are merged during the operation.
# The outer loop iterates through each row of the grid. i takes values from 0 to 3, representing row indices.
# The inner loop iterates through each column of the current row, except the last column. j takes values from 0 to 2, representing column indices. 
# The loop condition range(4 - 1) ensures that j + 1 is a valid index within the row.
# This condition checks if the current tile (self.gridCell[i][j]) is equal to the adjacent tile to the right (self.gridCell[i][j + 1]) and if the current tile is not zero.
# If both conditions are true, a merge operation is performed.
# self.gridCell[i][j] *= 2: The value of the current tile is doubled, effectively merging the two tiles.
# self.gridCell[i][j + 1] = 0: The adjacent tile to the right is set to zero, indicating that it has been merged into the current tile.
# self.score += self.gridCell[i][j]: The value of the merged tile is added to the score. Assuming self.score is a variable that keeps track of the player's score.
# self.merge = True: The merge flag is set to True to indicate that a merge has occurred.
    def mergeGrid(self):
        self.merge=False
        for i in range(4):
            for j in range(4 - 1):
                if self.gridCell[i][j] == self.gridCell[i][j + 1] and self.gridCell[i][j] != 0:
                    self.gridCell[i][j] *= 2
                    self.gridCell[i][j + 1] = 0
                    self.score += self.gridCell[i][j]
                    self.merge = True

   
   
#using random module to add random 2 each time we play
    def GenerateCell(self):
        cells=[]
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j] == 0:
                    cells.append((i, j))
        curr=random.choice(cells)
        i=curr[0]
        j=curr[1]
        self.gridCell[i][j]=2



    def can_merge(self):
    # checking row wise if two grid have same value(comparing rows) 
        for i in range(4):
            for j in range(3):
                if self.gridCell[i][j] == self.gridCell[i][j+1]:
                    return True
    # checking column wise if 2 grid have same value(comparing column)  
        for i in range(3):
            for j in range(4):
                if self.gridCell[i+1][j] == self.gridCell[i][j]:
                    return True
        return False


# calling colours
    def paintGrid(self):
        for i in range(4):
            for j in range(4):
                if self.gridCell[i][j]==0:
                    self.board[i][j].config(text='',bg='#CDC0B4')
                else:
                    self.board[i][j].config(text=str(self.gridCell[i][j]),
                    bg=self.bg_color.get(str(self.gridCell[i][j])),
                    fg=self.color.get(str(self.gridCell[i][j])))

class Game:
    def __init__(self,gamepanel):
        self.gamepanel=gamepanel
        self.end=False
        self.won=False

    def start(self):
        self.gamepanel.GenerateCell()
        self.gamepanel.GenerateCell()
        self.gamepanel.paintGrid()
        self.gamepanel.window.bind('<Key>', self.link_keys)
        self.gamepanel.window.mainloop()
    
    def link_keys(self,event):
        if self.end or self.won:
            return

        self.gamepanel.compress = False
        self.gamepanel.merge = False
        self.gamepanel.moved = False

        presed_key=event.keysym

        if presed_key=='Up':
            self.gamepanel.transpose()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.transpose()

        elif presed_key=='Down':
            self.gamepanel.transpose()
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
            self.gamepanel.transpose()

        elif presed_key=='Left':
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()

        elif presed_key=='Right':
            self.gamepanel.reverse()
            self.gamepanel.compressGrid()
            self.gamepanel.mergeGrid()
            self.gamepanel.moved = self.gamepanel.compress or self.gamepanel.merge
            self.gamepanel.compressGrid()
            self.gamepanel.reverse()
        else:
            pass

        self.gamepanel.paintGrid()
        print(self.gamepanel.score)

        flag=0
        for i in range(4):
            for j in range(4):
                if(self.gamepanel.gridCell[i][j]==2048):
                    flag=1
                    break

        if(flag==1): #found 2048
            self.won=True
            messagebox.showinfo('2048', message='You Wonnn!!')
            print("won")
            return

        for i in range(4):
            for j in range(4):
                if self.gamepanel.gridCell[i][j]==0:
                    flag=1
                    break

        if not (flag or self.gamepanel.can_merge()):
            self.end=True
            messagebox.showinfo('2048','Game Over!!!')
            print("Over")

        if self.gamepanel.moved:
            self.gamepanel.GenerateCell()
        
        self.gamepanel.paintGrid()
