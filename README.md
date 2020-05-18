# py2048
## This is 2048 game code
## This is the updated game in which we give win number by own.
# About this game:-
in this we want to form a number given by ourself by moving the numbers in the board .We can move numbers up,down ,right,left and if there are same number present consecutively then they merges in one and turn into twice of this number .If user unable to create given number then he lose.
## We can use it for size 2 and size 1 also.
## In size 1 if the winning number is same as random number comes in one box then the user wins otherwise lose.
### There is a file named py2048.py is 2048 game code 
### os.system('cls') command is used to clear screen after move.
### Run this code on windows only as.system('cls')is used in code which runs in windows.
### Make every move after minimum(0.5s) because without time command time.sleep(0.5s) game running very fast and it takes input twice on    single key press.
### To run this game in command line we have to write command:-
![Capture](https://user-images.githubusercontent.com/64793363/82179818-d9b63900-98fc-11ea-8c1e-a898b69cdd0a.PNG)
### Modules imported for this code:-
![Capture1](https://user-images.githubusercontent.com/64793363/82179984-2ef24a80-98fd-11ea-8a20-84e09f98fbb7.PNG)
### Initializing of board
### There is appending of row according to the size given by user in the empty matrix named mat.
### Functions used in this code:-
#### a.  def rowleft()
##### This function shifts all the rows to the left.
#### b.  def rev()
##### This function used to reverse the row.
#### c.  def transpose()
##### This function is used to get transpose of the matrix.
#### d. def merleft()
##### This function merges matrix to the left.
#### e. def merright()
##### This function merges matrix to the right.
#### f. def merdown()
##### This function merges matrix to down.
#### g. def merup()
##### This function merges matrix in up direction.
#### h.def pickvalue()
##### This function randomly pickly value btwn 2 and 4.
#### i.def addvalue()
##### This function add this random value at random place in mat named matrix.
#### j.def won()
##### This function checks the win condition after every move.
#### k.def nomove()
##### This function checks that there is more move available or not after every move.
### Some screenshots of game:-
#![Capture3](https://user-images.githubusercontent.com/64793363/82181389-0ddf2900-9900-11ea-8c69-5e0888d674a9.PNG)
#![Capture2](https://user-images.githubusercontent.com/64793363/82181395-10418300-9900-11ea-8c23-c2f137ee9e56.PNG)
#![Capture4](https://user-images.githubusercontent.com/64793363/82181393-0fa8ec80-9900-11ea-89e9-2f5e62437047.PNG)
