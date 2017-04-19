from random import randint

class Player:
    def __init__(self, name):
        self.Name = name
        self.Activity = []
        self.Capacity = []
        self.ContractAmount = 3.5
        self.difference = []
        self.preformance = []
        self.rollOver = 0

    def getCapacity(self, roundNum):
        capacity = randint(1, 6)
        if self.Activity[roundNum] == 0:
            self.Activity[roundNum] = capacity
        return capacity

    def completeActivity(self,capacity,work):
        if capacity > work:
            self.rollOver = 0
            return work
        elif capacity < work:
            self.rollOver = work - capacity
            return capacity
        elif capacity == work:
            self.rollOver = 0
            return capacity

    def playGame(self,passed,roundNum):
        self.Activity.append(self.rollOver + passed)
        self.Capacity.append(self.getCapacity(roundNum))
        self.Activity[roundNum] = self.completeActivity(self.Capacity[roundNum], self.Activity[roundNum])
        self.difference.append(self.Activity[roundNum] - self.ContractAmount)
        try:
            self.preformance.append((self.difference[roundNum]) - (self.preformance[roundNum - 1]))
        except IndexError:
            self.preformance.append(self.difference[roundNum] - 0)
        return self.Activity[roundNum]

class Game:
    def __init__(self, rounds, playerAmount, totlaWork):
        self.player = []
        self.rounds = rounds
        self.playerAmount = playerAmount
        self.totalWork = totalWork
        self.completedWork = 0

    def __init__(self):
        self.player = []
        self.rounds = 10
        self.playerAmount = 5
        self.totalWork = 35
        self.completedWork = 0

    def CreatePlayers(self):
        for x in range(0, self.playerAmount):
            self.player.append(Player(x+1))

    def playGame(self):
        passAmount = 0
        for x in range(0, self.rounds):
            passAmount = 0
            for y in range(0, self.playerAmount):
                passAmount = self.player[y].playGame(passAmount ,x)
            self.completedWork += passAmount

    def printResults(self, filename):
        file = open(filename + ".csv","w+")
        for x in range(0,5):
            file.write("Player: " + str(self.player[x].Name) + "\n")
            file.write("Round,1,2,3,4,5,6,7,8,9,10" + "\n")
            file.write("Capacity," + str(self.player[x].Capacity[0]) + "," + str(self.player[x].Capacity[1]) + "," + str(self.player[x].Capacity[2]) + "," + str(self.player[x].Capacity[3]) + "," + str(self.player[x].Capacity[4]) + "," + str(self.player[x].Capacity[5]) + "," + str(self.player[x].Capacity[6]) + "," + str(self.player[x].Capacity[7]) + "," + str(self.player[x].Capacity[8]) + "," + str(self.player[x].Capacity[9]) + "\n")
            file.write("Activity," + str(self.player[x].Activity[0]) + "," + str(self.player[x].Activity[1]) + "," + str(self.player[x].Activity[2]) + "," + str(self.player[x].Activity[3]) + "," + str(self.player[x].Activity[4]) + "," + str(self.player[x].Activity[5]) + "," + str(self.player[x].Activity[6]) + "," + str(self.player[x].Activity[7]) + "," + str(self.player[x].Activity[8]) + "," + str(self.player[x].Activity[9]) + "\n")
            file.write("Contract," + str(self.player[x].ContractAmount) + "," + str(self.player[x].ContractAmount) + "," + str(self.player[x].ContractAmount) + ","  + str(self.player[x].ContractAmount) + "," + str(self.player[x].ContractAmount) + "," + str(self.player[x].ContractAmount) + "," + str(self.player[x].ContractAmount) + "," + str(self.player[x].ContractAmount) + "," + str(self.player[x].ContractAmount) + "," + str(self.player[x].ContractAmount) + "\n")
            file.write("difference," + str(self.player[x].difference[0]) + "," + str(self.player[x].difference[1]) + "," + str(self.player[x].difference[2]) + "," + str(self.player[x].difference[3]) + "," + str(self.player[x].difference[4]) + "," + str(self.player[x].difference[5]) + "," + str(self.player[x].difference[6]) + "," + str(self.player[x].difference[7]) + "," + str(self.player[x].difference[8]) + "," + str(self.player[x].difference[9]) + "\n")
            file.write("preformance," + str(self.player[x].preformance[0]) + "," + str(self.player[x].preformance[1]) + "," + str(self.player[x].preformance[2]) + "," + str(self.player[x].preformance[3]) + "," + str(self.player[x].preformance[4]) + "," + str(self.player[x].preformance[5]) + "," + str(self.player[x].preformance[6]) + "," + str(self.player[x].preformance[7]) + "," + str(self.player[x].preformance[8]) + "," + str(self.player[x].preformance[9]) + "\n")
        file.close()

for x in range(0,10):
    game = Game()
    game.CreatePlayers()
    game.playGame()
    game.printResults("game"+str(x)) 
