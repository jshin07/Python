import random

def coinTosses (repeat):
    print "Starting the program..."
    head_count = 0
    tail_count = 0
    for i in range(1, repeat+1):
        toss = random.randint(0,1)
        if toss ==1:
            head_count += 1
            print "Attempt #",i, ": Throwing a coin... It's a head!... Got", head_count, "head(s) so far and ", tail_count, "tail(s) so far"
        else:
            tail_count += 1
            print "Attempt #",i, ": Throwing a coin... It's a tail!... Got", head_count, "head(s) so far and ", tail_count, "tail(s) so far"
    print "Ending the program, thank you!"


coinTosses(5000)
