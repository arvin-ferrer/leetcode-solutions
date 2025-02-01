def relativeRanks(score):
    sortedScores = sorted(score, reverse = True)
    hashmap = {}
    index = 1
    for i in sortedScores:
        hashmap[i] = score.index(i)
    for value in hashmap.values():
        if index == 1:
            score[value] = "Gold Medal"
        elif index == 2:
            score[value] = "Silver Medal"
        elif index == 3:
            score[value] = "Bronze Medal"
        else:
            score[value] = str(index)
        index +=1 
    return score
relativeRanks([10,3,8,9,4])
