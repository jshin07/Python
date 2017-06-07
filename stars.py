
x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(x):
    for i in range(0, len(x)):
        print "*" * x[i]
draw_stars(x)





x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
def draw_stars(x):
    for i in range(0, len(x)):
        if type(x[i])== int:
            print "*" * x[i]
        else:
            count = len(x[i])
            letter = x[i][0]
            print letter.lower() *count
draw_stars(x)
