name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(arr1, arr2):
    new_list= zip(name,favorite_animal)
    new_dict= dict(new_list)
    print new_dict

make_dict(name,favorite_animal)
