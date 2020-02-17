from random import randint
import requests
import json

CURRENCY_URL = "http://www.floatrates.com/daily/usd.json"
MAX_NUMBER = 100
difficulty = -1
ils_usd_rate = -1
usd_amount = -1

def load_currency_rate():
    global ils_usd_rate, CURRENCY_URL
    response = requests.get(CURRENCY_URL)
    ils_usd_rate = float(json.loads(response.content)["ils"]["rate"])

def get_money_interval(ils_amount):
    global difficulty
    return (round(ils_amount - (5 - difficulty)),round(ils_amount + (5 - difficulty)))

def get_guess_from_user():
    global MAX_NUMBER, usd_amount
    usd_amount = randint(1, MAX_NUMBER)
    return float(input('How much {} dollars are in shekels?: '.format(usd_amount)))

def play(diff):
    global difficulty,usd_amount
    difficulty = diff
    load_currency_rate()
    user_answer = get_guess_from_user()
    money_interval = get_money_interval(usd_amount * ils_usd_rate)
    return user_answer >= money_interval[0] and user_answer <= money_interval[1]