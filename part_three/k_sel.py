import random
from operator import itemgetter
links = {
    'l1' : 10,
    'l2' : 15,
    'l3' : 10,
    'l4' : 20,
    'l5' : 15,
    'l6' : 20,
    'l7' : 15,
    'l8' : 15,
    'l9' : 20
}

paths = {
    1:sum(itemgetter('l2','l8','l9')(links)),
    2:sum(itemgetter('l4','l6')(links)),
    3:sum(itemgetter('l4','l6','l7')(links)),
    4:sum(itemgetter('l1','l4')(links)),
    5:sum(itemgetter('l4','l1','l2')(links)),
    6:sum(itemgetter('l3','l7')(links)),
    7:sum(itemgetter('l5','l9')(links)),
    8:sum(itemgetter('l8','l9','l5')(links)),
    9:links['l3'],
    10:sum(itemgetter('l1','l2')(links))
}

print(paths[random.randint(1, 10)])

