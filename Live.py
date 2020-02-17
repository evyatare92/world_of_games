import MemoryGame,GuessGame,CurrencyRouletteGame,Score

MEMORY_GAME = 1
GUESS_GAME = 2
CURRENCY_ROLLETE = 3

MIN_LEVEL = 1
MAX_LEVEL = 5

def welcome(name):
    return "Hello {} and welcome to the World of Games (WoG).\n".format(name) + \
           "Here you can find many cool games to play.\n"

def load_game():
    user_output_game = "Please choose a game to play:\n" + \
    "{}. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n" + \
    "{}. Guess Game - guess a number and see if you chose like the computer\n" + \
    "{}. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
    user_output_game = user_output_game.format(MEMORY_GAME, GUESS_GAME, CURRENCY_ROLLETE)
    user_output_level = "Please choose game difficulty from {} to {}: ".format(MIN_LEVEL, MAX_LEVEL)

    game_choise, level_choise = validate_input(user_output_game, user_output_level)
    user_won = None
    if game_choise == MEMORY_GAME:
        user_won = MemoryGame.play(level_choise)
    elif game_choise == GUESS_GAME:
        user_won = GuessGame.play(level_choise)
    else:
        user_won = CurrencyRouletteGame.play(level_choise)

    if user_won:
        Score.add_score(level_choise)


def validate_input(user_output_game, user_output_level):
    is_valid_choises = False
    game_choise = -1
    level_choise = -1
    while not is_valid_choises:
        try:
            #game_choise = int(input(user_output_game))
            #level_choise = int(input(user_output_level))
            game_choise = 1
            level_choise = 1
            if (game_choise > CURRENCY_ROLLETE or game_choise < MEMORY_GAME):
                print("invalid game. must be one in range of {}-{}\n".format(MEMORY_GAME, CURRENCY_ROLLETE))
            elif (level_choise > MAX_LEVEL or game_choise < MIN_LEVEL):
                print("invalid level. must be one in range of {}-{}\n".format(MIN_LEVEL, MAX_LEVEL))
            else:
                is_valid_choises = True
        except ValueError as e:
            print("invalid number entered. must be numeric.")

    return game_choise, level_choise
