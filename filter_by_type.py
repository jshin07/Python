def filter (val):
    if type(val) is int:
        if val >=100:
            print "That's a big number!"
        else:
            print "That's a small number"
    elif type(val) is str:
        if len(val)>=50:
            print "Long sentence"
        else:
            print "Short sentence"
    else:
        if len(val)>=10:
            print "Big list!"
        else:
            print "Short list"
filter ()
