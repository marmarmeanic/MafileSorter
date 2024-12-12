import time
import os


def validatemenu(user_input):
    try:
        user_input = int(user_input)
        if not ((user_input > 0) and (user_input < 5)):
            raise Exception()
    except:
        print('Your input not valid')
        time.sleep(1)
        os.system('cls')
        return False
    return True
