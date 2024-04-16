import random

def dic_choice(a):
    dic_list = list(a)
    dic_random = random.choice(dic_list)
    return dic_random
def dic_shuffle(a):
    dic_list = list(a)
    random.shuffle(dic_list)
    return dic_list