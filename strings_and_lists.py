# #Find and replace
words ="It's thanksgiving day. It's my birthday, too!"
newWord =words.replace("day","month")
print newWord

# #Min and Max
x=[2,54,-2,7,12,98]
print min(x)
print max(x)

# #First and Last
x =["hello", 2,54, -2, 7, 12, 98, "world"]
print [x[0], x[len(x)-1]]

#New List
x=[19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
y=x[0:5]
print y
z= x[5:10]
print z
z.insert(0,y)
print z
