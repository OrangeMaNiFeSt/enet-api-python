from random import randrange

def generate_random(length):
    characters = "ABCDEF0123456789"
    token = ""
    for i in range(length):
        rand_num = randrange(0, len(characters))
        token += characters[rand_num:rand_num+1]
    return token