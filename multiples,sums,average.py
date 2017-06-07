def printOdds1To1000 ():
    for i in range (1,1001):
        if i % 2 == 1:
            print i
printOdds1To1000()

def printAllMultiples ():
    for i in range (5,1000001):
        if i % 5 ==0:
            print i
printAllMultiples()

def printSum (a):
    sum = 0
    for i in range (0,len(a)):
        sum+= a[i]
    print sum
printSum([1,2,5,10,255,3])

def printAvg (a):
    sum = 0
    for i in range(0, len(a)):
        sum+= a[i]
    avg = sum/len(a)
    print avg
printAvg([1,2,5,10,255,3])
