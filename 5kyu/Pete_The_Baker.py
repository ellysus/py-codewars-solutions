import math
def cakes(recipe, available):
    array = []
    for key in recipe.keys():
        if key in available.keys():
            array.append(math.floor(available[key]/recipe[key]))
        else:
            array.append(0)
    return min(array)