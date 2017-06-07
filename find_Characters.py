def findChar(list, letter):
    newList =[]
    for i in list:
        if i.find(letter) >=0:
            newList.append(i)
    print newList

findChar (['hello','world','my','name','is','Anna'],"o")


#
#word_list = ['hello','world','my','name','is','Anna']
#char = 'o'
## output
#new_list = ['hello','world']
