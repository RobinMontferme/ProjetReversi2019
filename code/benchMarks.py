from localGame import *
import myPlayer
import myPlayerBook
import RandomPlayer

players = []
data = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
n = 10

print("V1 vs Random")
for i in range(0,n):
    player1 = myPlayer.myPlayer()
    player2 = RandomPlayer.RandomPlayer()
    players.append(player1)
    players.append(player2)
    res = localGame(players)
    data[0][res] += 1
    players.clear()
    print("Game Done:",i)
print("Random vs V1 - Done")

print("V2 vs Random")
for i in range(0,n):
    player1 = myPlayerBook.myPlayerBook()
    player2 = RandomPlayer.RandomPlayer()
    players.append(player1)
    players.append(player2)
    res  = localGame(players)
    data[1][res] += 1
    players.clear()
print("Rand vs V2 - Done")

print("V1 vs V2")
for i in range(0,n):
    player1 = myPlayer.myPlayer()
    player2 = myPlayerBook.myPlayerBook()
    players.append(player1)
    players.append(player2)
    res  = localGame(players)
    data[2][res] += 1
    players.clear()
print("V1 vs V2 - Done")


print(data)
for i in range(0,len(data)):
    print("---------------------")
    blackRate = (data[i][2]/n)*100
    whiteRate = (data[i][1]/n)*100
    drawRate = (data[i][0]/n)*100
    print("Black won %d %% of the time" % blackRate)
    print("White won %d %% of the time" % whiteRate)
    print("Draw %d %% of the time" % drawRate)
print("Game played:",n)

