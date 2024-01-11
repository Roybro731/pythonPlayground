
def startHere():
    print("comprehensions lists")
    evens = [2,4,6,8,10]
    odds = [1,3,5,7,9,11, 13, 15, 17, 19]

    evenSquare = [ e ** 2 for e in evens]
    print(evenSquare)

    oddSquared = [ e**2 for e in odds if e >3 and e <17 ]
    print(oddSquared)

    print("comprehensions dictionary")
    ctemps = [0, 10, 42, 100]
    tempDict = {t: (t*9/5)+32 for t in ctemps}
    print(tempDict)




