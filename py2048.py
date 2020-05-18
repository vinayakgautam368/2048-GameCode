import random
import copy
import keyword

import keyboard
import pyautogui
import os
import argparse
import time
import sys

parser=argparse.ArgumentParser()
parser.add_argument('-n','--size', type=int ,help='size of board')
parser.add_argument('-w','--no',type=int,help='win')
args=parser.parse_args()

size=args.size
no=args.no

board=size
def display():
    largest=mat[0][0]
    for row in mat:
        for element in row:
            if element>largest:
                largest=element

    space=len(str(largest))
    for row in mat:
        curr="|"
        for element in row:
            if element==0:
                curr+=str(0)*space+"|"
            else:
                curr+=(str(0)*(space-len(str(element))))+str(element)+"|"
        print(curr)
    print()


def rowleft(row):
    for j in range(board-1):
        for i in range(board-1,0,-1):
            if row[i-1]==0:
                row[i-1]=row[i]
                row[i]=0
    for i in range(board-1):
        if row[i]==row[i+1]:
            row[i]=row[i]*2
            row[i+1]=0
    for i in range(board-1,0,-1):
        if row[i-1]==0:
            row[i-1]=row[i]
            row[i]=0

    return row

def merleft(cb):
    for i in range(board):
        cb[i]=rowleft(cb[i])

    return cb
def rev(row):
    new=[]
    for i in range(board-1,-1,-1):
        new.append(row[i])
    return new
def merright(cb):
    for i in range(board):
        cb[i]=rev(cb[i])
        cb[i]=rowleft(cb[i])
        cb[i]=rev(cb[i])

    return cb
def transpose(cb):
    for j in range(board):
        for i in range(j,board):
            if not i==j:
                temp=cb[j][i]
                cb[j][i]=cb[i][j]
                cb[i][j]=temp

    return cb
def merup(cb):
    cb=transpose(cb)
    cb=merleft(cb)
    cb=transpose(cb)

    return cb
def merdown(cb):
    cb=transpose(cb)
    cb=merright(cb)
    cb=transpose(cb)

    return cb

def pickvalue():
    if random.randint(1,8)==1:
       return 4
    else:
       return 2
def addvalue():
    r=random.randint(0,board-1)
    c=random.randint(0,board-1)
    while not mat[r][c]==0:
        r=random.randint(0,board-1)
        c=random.randint(0,board-1)

    mat[r][c]=pickvalue()

def won():
    for row in mat:
        if no in row:
            return True
    return False
def nomoves():
    t1=copy.deepcopy(mat)
    t2=copy.deepcopy(mat)
    t1=merdown(t1)
    if t1==t2:
        t1=merright(t1)
        if t1==t2:
            t1=merup(t1)
            if t1==t2:
                t1=merleft(t1)
                if t1==t2:
                    return True
    return False
mat=[]
for i in range(board):
    row=[]
    for j in range(board):
        row.append(0)
    mat.append(row)

num=1
while num>0:
    r=random.randint(0,board-1)
    c=random.randint(0,board-1)
    if mat[r][c]==0:
        mat[r][c]=pickvalue()
        num=num-1
print("::THIS IS 2048 GAME::")
os.system("cls")
display()
time.sleep(0.5)
gameover=False
if size==1:
    m=pickvalue()
    if m==no:
        print("YOU WON")
        gameover=True
    else:
        print("YOU LOSE")
        gameover=True
while not gameover:
    keyinp=keyboard.read_key()

   # move=input("enter the move")
    validinput=True
    tempmat=copy.deepcopy(mat)
    #if move=="w":

    if keyinp=="w":
    #if keyboard.is_pressed('w'):

        mat=merup(mat)
   # elif move=="a":
    elif keyinp=="a":
    #elif keyboard.is_pressed('a'):
        mat=merleft(mat)
   # elif move=="d":
    elif keyinp=="d":
    #elif keyboard.is_pressed('d'):
        mat=merright(mat)
   # elif move=="s":
    elif keyinp=="s":
    #elif keyboard.is_pressed('s'):
        mat=merdown(mat)
    else:
        validinput=False

    if not validinput:
        print("Please enter different move")
    else:
        if mat==tempmat:
            print("Try different move")
        else:
            if won():
                os.system("cls")
                display()
                time.sleep(0.5)
                print("YOU WON")
                gameover=True
            else:
                addvalue()
                #pyautogui.typewrite(["l"])
                os.system("cls")

                display()
                time.sleep(0.5)
                if nomoves():
                    print("YOU LOSE")
                    print("PLAY AGAIN")
                    gameover=True










