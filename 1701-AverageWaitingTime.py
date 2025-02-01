def averagetime(customers):
    finishedtime = customers[0][0] + customers[0][1]
    times = [finishedtime-customers[0][0]]
    for i in range(1, len(customers)):
        if finishedtime > customers[i][0]:
            finishedtime = finishedtime + customers[i][1]
            times.append(finishedtime - customers[i][0])
        else:
            finishedtime = sum(customers[i])
            times.append(sum(customers[i])-customers[i][0])
        
    return sum(times)/len(times)

averagetime([[1,2],[2,5],[4,3]])
