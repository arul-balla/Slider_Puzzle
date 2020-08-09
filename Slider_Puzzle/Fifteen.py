import sys, threading, time
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QDialog, QInputDialog, QErrorMessage, QMessageBox
import random
from operator import itemgetter


ROWS = 4
SEATS = 4
CELL_SIZE = 90
GRID_ORIGINX = 50
GRID_ORIGINY = 50
SLIDE_NUM=0

my_list = []
blank_x=0
blank_y=0
counter=[]
recreate=[]
scores=[]
namelist=[]
data=[]
data2=[]
inversioncount=0
Moves=0
linecount=0
fn = 'leaderboard.txt'
#loc162d=0
#Rowloc=True

class Slider(QWidget):


    def __init__(self): #this is line 14
        super().__init__()
        self.__tiles = [[''] * SEATS for i in range(ROWS)]
        self.setWindowTitle('Slider Puzzle Grid')
        self.setGeometry(300, 300, (2 * GRID_ORIGINX + CELL_SIZE * SEATS) +300, \
            3 * GRID_ORIGINY + CELL_SIZE * ROWS)
        self.show()

    def gridpopulate(self):
        global blank_x, blank_y, counter

        #counter=[1,2,3,4,5,6,7,8,9,10,11,15,13,14,12,16]
        #counter= random.sample(range(1,17),16)#[14,15,13,5,11,2,10,9,16,7,4,6,12,8,3,1]
        counter_index=0
        print(counter)
        validtest=ex.gridcheck()
        print(validtest)
        if(validtest==True):
            for r in range(ROWS):
                for c in range(SEATS):
                    if(counter[counter_index]!=16):
                        self.__tiles[r][c]=str(counter[counter_index])
                        counter_index+=1
                        #print(counter[counter_index])
                    else:
                        self.__tiles[r][c]=''
                        blank_x=r
                        blank_y=c
                        #print(blank_x)
                        #print(blank_y)
                        counter_index +=1
        elif(validtest==False):
            ex.gridpopulate()
        self.update()

    def gridcheck(self):
        global counter #inversioncount
        counter= random.sample(range(1,17),16)
        #find 2d location of 16
        inversioncount=0
        for loc in range(len(counter)):
            if(counter[loc]==16):
                loc162d=loc
                rowcalc=(loc162d+1)//4
                if(rowcalc==0):
                    print("even")
                else:
                    print("odd")


        #count inversions
        testvar=0
        for x in counter:
            compareval= x
            testvar+=1
            for y in counter[testvar:]:
                if(compareval !=16 and y!=16):
                #print(y)
                    if(compareval> y):
                        inversioncount+=1
        print(inversioncount)
        print(rowcalc)
        #check valid
        if(inversioncount%2==0 and rowcalc!=0):
        #    print('true')
            return True
        elif(inversioncount%2!=0 and rowcalc==0):
        #    print('true')
            return True
        else:
        #    print('false')
            return False

    def wincheck(self):
        global recreate
        validate_sequence=1
        for r in range(ROWS):
            for c in range(SEATS):
                if(self.__tiles[r][c]=='' and validate_sequence==16):
                    #name,ok = QInputDialog.getText(self, 'Add a guest', 'Enter name:')
                    #if(len(name)>15):
                    #    QErrorMessage(self).showMessage('Name too long, please try again. Must be less than 15 letters.')
                    #file = open(fn, "a")
                    #file.writelines(name)
                    #file.close()
                    return True
                if(self.__tiles[r][c]!=str(validate_sequence)):
                    return False
                else:
                    validate_sequence+=1

        print(recreate)
        self.update()

    def paintEvent(self, event): #this is line 23
        global linecount, scores, data, data2

        qp = QPainter()
        blackPen = QPen(Qt.black)
        qp.begin(self)
        qp.setPen(blackPen)

        qp.setPen(blackPen)

#        #leaderboard grid
#        #handles scores
#        with open(fn,'r') as file:
#            for line in file:
#
#                #line.split(",")
#                #print(line.split(","))
#                scores.append(int(line.split(",")[1]))
#                #print(int(line.split(",")[1]))
#                print(scores)
#                linecount+=1
#        scores.sort()
#        print(scores)


        #print(data[0])
        #data2=sorted(data,key=itemgetter(0))
        n=1
        if(len(data2)<=5):
            for elem in range(len(data)):
                qp.drawText(660,50*n+80,str(data2[elem][0]))
                qp.drawText(570,50*n+80,data2[elem][1].strip('"'))
                n+=1
        if(len(data2)>5):
            for item in range(5):
                qp.drawText(660,50*n+80,str(data2[item][0]))
                qp.drawText(570,50*n+80,data2[item][1].strip('"'))
                n+=1




        #Row 1
        qp.drawRect(500,50,50,50)
        qp.drawRect(550,50,100,50)
        qp.drawRect(650,50,50,50)
        qp.drawText(510,80,'Rank')
        qp.drawText(580,80,'Name')
        qp.drawText(655,80,'Moves')

        #Row 2
        qp.drawRect(500,100,50,50)
        qp.drawRect(550,100,100,50)
        qp.drawRect(650,100,50,50)
        qp.drawText(520,130,'1')
        #Row 3
        qp.drawRect(500,150,50,50)
        qp.drawRect(550,150,100,50)
        qp.drawRect(650,150,50,50)
        qp.drawText(520,180,'2')
        #Row 4
        qp.drawRect(500,200,50,50)
        qp.drawRect(550,200,100,50)
        qp.drawRect(650,200,50,50)
        qp.drawText(520,230,'3')
        #Row 5
        qp.drawRect(500,250,50,50)
        qp.drawRect(550,250,100,50)
        qp.drawRect(650,250,50,50)
        qp.drawText(520,280,'4')
        #Row 6
        qp.drawRect(500,300,50,50)
        qp.drawRect(550,300,100,50)
        qp.drawRect(650,300,50,50)
        qp.drawText(520,330,'5')

        #Slider grid
        for r in range(ROWS):
            for c in range(SEATS):


                    qp.drawRect(GRID_ORIGINX + c * CELL_SIZE, GRID_ORIGINY + r * CELL_SIZE, CELL_SIZE,\
                    CELL_SIZE)
                    qp.setPen(Qt.blue)
                    qp.drawText(GRID_ORIGINX + c * CELL_SIZE + (CELL_SIZE/2), GRID_ORIGINY + r * CELL_SIZE + (CELL_SIZE/2),\
                    self.__tiles[r][c])
                    qp.drawText(50,450,"Moves: " + str(Moves))
                    qp.setPen(blackPen)
                    qp.drawText(550,30, "Leaderboard")
                    if(ex.wincheck()):
                    #if(Moves==2):
                        qp.setPen(Qt.red)
                        qp.drawText(220,30,"you win")

                        #data2=[]
                    #    name,ok = QInputDialog.getText(self, 'Add a guest', 'Enter name:')
                    #qp.setPen(blackPen)

                #print(self.__tiles[r][c])
                    qp.setPen(blackPen)
        #if(ex.wincheck()==True):
        #    qp.setPen(Qt.red)
        #    qp.drawText(220,30,"you win")
        #    name,ok = QInputDialog.getText(self, 'Add a guest', 'Enter name:')
        #    if ok:
        #        print('write file')


        qp.end()

    def mousePressEvent(self, event): #this is line 38
        global blank_x, blank_y,Moves, data, data2

        row = (event.y() - GRID_ORIGINY) // CELL_SIZE
        col = (event.x() - GRID_ORIGINX) // CELL_SIZE
        if(ex.wincheck()==False):
            if 0 <= row < ROWS and 0 <= col < SEATS:
                if(self.__tiles[row][col]!=''):
                    #handles ROW sections
                    if(row==blank_x):
                        diffRow=blank_y-col
                        #handles Left side
                        if(diffRow>0):
                            Moves+=1
                            for rep_horizL in range(diffRow):
                                temp_horizL=self.__tiles[blank_x][blank_y-1]
                                self.__tiles[blank_x][blank_y-1]=''
                                self.__tiles[blank_x][blank_y]=temp_horizL
                                blank_y=blank_y-1

                                print(Moves)
                                #if(ex.wincheck()):
                                #    print("you win!!")

                        #handles Right side
                        if(diffRow<0):
                            Moves+=1
                            for rep_horizR in range(abs(diffRow)):
                                temp_horizR=self.__tiles[blank_x][blank_y+1]
                                self.__tiles[blank_x][blank_y+1]=''
                                self.__tiles[blank_x][blank_y]=temp_horizR
                                blank_y=blank_y+1
                                print(Moves)
                                #if(ex.wincheck()):
                                #    print("you win!!")

                    #handles COLUMN sections
                    elif(col==blank_y):
                        diffCol=blank_x-row
                        #handles Up side
                        if(diffCol>0):
                            Moves+=1
                            for rep_VertU in range(diffCol):
                                temp_VertU=self.__tiles[blank_x-1][blank_y]
                                self.__tiles[blank_x-1][blank_y]=''
                                self.__tiles[blank_x][blank_y]=temp_VertU
                                blank_x=blank_x-1
                                print(Moves)
                                #if(ex.wincheck()):
                                #    print("you win!!")
                        #handles Down side
                        if(diffCol<0):
                            Moves+=1
                            for rep_VertD in range(abs(diffCol)):
                                temp_VertD=self.__tiles[blank_x+1][blank_y]
                                self.__tiles[blank_x+1][blank_y]=''
                                self.__tiles[blank_x][blank_y]=temp_VertD
                                blank_x=blank_x+1
                                print(Moves)
                                #if(ex.wincheck()):
                                #    print("you win!!")
        while(ex.wincheck()==True):
        #if(Moves==2):
            name = ""
            while(name is not None):
                name,ok = QInputDialog.getText(self, 'Add a guest', 'Enter name:')
                if ok:
                    if(len(name)>5 or len(name)==0):
                        #QErrorMessage(self).showMessage('Name too long, please try again. Must be less than 5 letters.')
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setInformativeText("Name too long, please try again. Must be less than 5 letters")
                        msg.setWindowTitle("Name too long")
                        msg.setStandardButtons(QMessageBox.Ok)
                        retval = msg.exec_()
                    else:
                        break
            if(len(name)<=5):
                if ok:
                    with open(fn,'a') as file:
                        file.write('"' + name + '",' + str(Moves) + '\n')
                        #file.flush()
                    file.close()
                    #with open(fn,'r') as file:
                    #    for line in file:
                    #        if line not in ['\n', '\r\n']:
                    #            namelist.append(line.split(",")[0])
                    #            scores.append(int(line.split(",")[1]))
                    #file.close()
                    readscore()
                    #data=list(zip(scores,namelist))
                    #data2=sorted(data,key=itemgetter(0))
                    #data.sort()
                    #namelist.append(name)
                    #scores.append(Moves)

                    #data.sort()
            break


#        else:
#            name,ok = QInputDialog.getText(self, 'Add a guest', 'Enter name:')
#            if(len(name)>5):
#                QErrorMessage(self).showMessage('Name too long, please try again. Must be less than 15 letters.')
#            file = open(fn, "a")
#            file.writelines(name)
#            file.close()
        self.update()


def readscore():
    global data, data2
    del data[:]
    del data2[:]
    del scores[:]
    del namelist[:]

    with open(fn, 'r') as file:
        for line in file:
            if line not in ['\n', '\r\n']:
                namelist.append(line.split(",")[0])
                scores.append(int(line.split(",")[1]))
    file.close()
    data = list(zip(scores, namelist))
    data2 = sorted(data, key=itemgetter(0))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    readscore()



    #print(data[0][1])

    try:
        file = open(fn, 'r')
    except IOError:
        file = open(fn, 'a')



    ex = Slider()
    #leaderboard grid
    #handles scores


    ex.gridpopulate()
    print(counter)

    #print("test",len(fn))
    #ex.wincheck()
    sys.exit(app.exec_())
