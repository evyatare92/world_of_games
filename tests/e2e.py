from selenium import webdriver

MIN_VALUE = 1
MAX_VALUE = 1000
EXIT_SUCCESS = 0
EXIT_FAIL = -1

def test_score_service(url):
    global MIN_VALUE,MAX_VALUE
    chrome_driver = webdriver.Chrome(executable_path='C:/Temp/chromedriver.exe')
    chrome_driver.get(url)
    elem = chrome_driver.find_element_by_id("score")

    try:
        score = int(elem.text)
        result = (MIN_VALUE <= score and score <= MAX_VALUE)
    except ValueError:
        result = false

    chrome_driver.close()
    return result

def main_function(url):
    global EXIT_SUCCESS,EXIT_FAIL

    if test_score_service(url):
        return EXIT_SUCCESS
    else:
        return EXIT_FAIL

main_function("http://192.168.95.5:8777/getscore")
