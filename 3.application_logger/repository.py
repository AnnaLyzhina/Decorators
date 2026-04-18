from logger import logger

LOG_PATH = 'tg_api.log'

@logger(LOG_PATH)
def get_random_word(user_id):
    return f'word for user {user_id}'

@logger(LOG_PATH)
def add_user_word(user_id, english, russian):
    return f'added: {english} - {russian} for user {user_id}'

@logger(LOG_PATH)
def delete_user_word(user_id, word_id):
    return f'deleted word {word_id} for user {user_id}'