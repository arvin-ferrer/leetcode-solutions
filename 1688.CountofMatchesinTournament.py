def matches(n):
    #my thought process 
    # n = 7
    # if team is odd number of matches is (n - 1) / 2 and (n - 1)/2 +1 teams advances to the next round
    # if team is even number of matches is n/2 and n/2 teams advances to the second round
    # while n != 2 perform matches: (n-1)/2 append to the array and n = (n-1)/2 +1 if n = odd
    # if even matches: n/2 append to array and n = n/2
    matches = []
    while n >= 2:
        if n % 2 == 0:
            matches.append(n/2)
            n = n/2
        else:
            matches.append((n-1)/2)
            n = ((n-1)/2)+1
    print(int(sum(matches)))




matches(14)
