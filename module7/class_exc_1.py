

from random import randrange
from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_blobs
def create_babies(amount):
    lst = list()
    for x in range(amount):
        height = randrange(45, 60)
        weight = randrange(3300, 4200)
        age_in_month = randrange(2, 24)
        lst.append((height, weight, age_in_month))
    return lst

