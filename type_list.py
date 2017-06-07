
def printMessage (val):
    strOutput =" "
    count = 0

    for i in range(0, len(val)):
        if type(val[i]) is str:
            strOutput += val[i]+ " "
        elif type(val[i]) is int or type(val[i]) is float:
            count += val[i]
    if len(strOutput) < 1:
        print "The array you entered is of integer types"
        print "Sum: " , count

    elif count < 1:
        print "The array you entered is of string type"
        print "String: " , strOutput

    else:
        print "The array you entered is of mixed types"
        print "String: ",strOutput
        print "Sum: " ,count

printMessage(['magical unicorns',19,'hello',98.98,'world'])
