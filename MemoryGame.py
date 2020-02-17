from random import randint
from time import sleep

difficulty = 3
MAX_NUMBER = 101
TIME = 0.7

def generate_sequence():
    global difficulty, MAX_NUMBER, TIME
    list = []
    for i in range(difficulty):
        list.append(randint(1,MAX_NUMBER))
    print(list,end="")
    sleep(TIME)
    print("\r",end="\r")
    return list

def get_list_from_user():
    global difficulty
    user_list = []
    for i in range(difficulty):
        user_list.append(int(input('please enter the {} number: '.format(i + 1))))
    return user_list

def is_list_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    are_equal = True
    i = 0
    while i < len(list1) and are_equal:
        are_equal = list1[i] == list2[i]
        i+=1
    return are_equal

def play(diff):
    global difficulty
    difficulty = diff
    comp_list = generate_sequence()
    user_list = get_list_from_user()
    return is_list_equal(comp_list, user_list)