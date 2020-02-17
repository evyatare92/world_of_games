from random import randint

difficulty = -1
secret_number = -1

def read_number_from_user(minimum, maximum = None):
    is_valid = False
    num = -1

    if maximum != None and maximum < minimum:
        raise ValueError("wrong borders")
    while not is_valid:
        try:
            num = int(input("please enter a number: "))
            if num < minimum:
                print("the number must be greater than or equal to {}".format(minimum))
            elif maximum != None and num > maximum:
                print("the number must be less than {}".format(maximum))
            else:
                is_valid = True
        except ValueError as e:
            print("must be numeric")
    return num

def generate_number():
    global difficulty, secret_number
    secret_number = randint(1, difficulty)

def get_guess_from_user():
    global difficulty
    min = 1
    max = difficulty
    return read_number_from_user(min, max)

def compare_results():
    global secret_number
    user_num = get_guess_from_user()
    return user_num == secret_number

def play(diff):
    global difficulty, secret_number
    difficulty = diff
    generate_number()
    return compare_results()
