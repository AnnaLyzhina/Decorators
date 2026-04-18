from logger import logger
from repository import get_random_word, add_user_word

LOG_PATH = 'tg_api.log'

@logger(LOG_PATH)
def start_command(user_id):
    return f'user {user_id} started bot'

@logger(LOG_PATH)
def next_word_command(user_id):
    return get_random_word(user_id)

@logger(LOG_PATH)
def add_word_command(user_id, english, russian):
    return add_user_word(user_id, english, russian)

if __name__ == '__main__':
    print(start_command(1))
    print(next_word_command(1))
    print(add_word_command(user_id=1, english='cat', russian='кот'))