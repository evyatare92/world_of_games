from Utils import SCORES_FILE_NAME

def read_score_from_file():
    score = None
    try:
        with open(SCORES_FILE_NAME, "r") as file:
            score = int(file.readline())
    except:
        score = 0
    return score

def save_score_to_file(score):
    with open(SCORES_FILE_NAME, "w") as file:
        file.write(str(score))

def add_score(difficulty):
    score = read_score_from_file()
    new_score = score + (difficulty * 3) + 5
    save_score_to_file(new_score)



