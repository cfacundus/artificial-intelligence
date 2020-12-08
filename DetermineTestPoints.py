winScalar = 15
secondPoints = 10
losePoints = 0
TWins = 0
RWins = 0
AWins = 0

def assignRanking(index, resultsList):
    copyList = resultsList.copy()
    if(resultsList[index] == max(copyList)):
        return 1
    copyList.remove(max(copyList))
    if(resultsList[index] == max(copyList)):
        return 2
    copyList.remove(max(copyList))
    if(resultsList[index] == max(copyList)):
        return 3
    print("ERROR IN RANK ASSIGN")
    return -1

def assignPoints(ranking, index, rankingList, resultsList):
    count = rankingList.count(ranking)
    ranking = ranking + count - 1
    if(ranking == 1):
        second = rankingList.index(2)
        dif = abs(resultsList[index] - resultsList[second])
        ave = (resultsList[index] + resultsList[second])/2.0
        percDif = dif/ave
        return 2*secondPoints + winScalar * percDif
    if(ranking == 2):
        return secondPoints
    if(ranking == 3):
        return losePoints
    print("ERROR IN POINTS ASSIGN")
    return -1
    
possibleFiles = ["outputNormal.txt", "outputMoreRounds.txt", "outputHalfSimulations.txt", "outputHalfMaxRaise.txt"]
results = possibleFiles[3]
file = open(results, "r")
line = file.readline()
count = 0
TScore = 0
RScore = 0
AScore = 0
while line:
    if(line[0].isdigit()):
        count = count + 1
        resultsList = line.rsplit(" ")
        resultsList = [int(i) for i in resultsList]
        TChips = assignRanking(0, resultsList)
        RChips = assignRanking(1, resultsList)
        AChips = assignRanking(2, resultsList)
        rankingList = [TChips, RChips, AChips]
        if TChips == 1: TWins = TWins+1
        if RChips == 1: RWins = RWins+1
        if AChips == 1: AWins = AWins+1
        TTScore = assignPoints(TChips, 0, rankingList, resultsList)
        TRScore = assignPoints(RChips, 1, rankingList, resultsList)
        TAScore = assignPoints(AChips, 2, rankingList, resultsList)
        print("Truther score: {0} Randy score: {1} AI score: {2}".format(TTScore, TRScore, TAScore))
        TScore = TScore + TTScore
        RScore = RScore + TRScore
        AScore = AScore + TAScore
    line = file.readline()
print("\nResults of {0} games...\n".format(count))
print("Truther:  Score: {0}    Winrate: {1}%".format(round((TScore/count), 2), round(100*TWins/float(count), 1)))
print("Randy:    Score: {0}    Winrate: {1}%".format(round((RScore/count), 2), round(100*RWins/float(count), 1)))
print("AI:       Score: {0}    Winrate: {1}%".format(round((AScore/count), 2), round(100*AWins/float(count), 1)))