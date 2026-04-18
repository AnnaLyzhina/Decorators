from datetime import datetime
from functools import wraps

def logger(path):
    def __logger(old_function):
        @wraps(old_function)
        def new_function(*args, **kwargs):
            result = old_function(*args, **kwargs)

            with open(path, 'a', encoding='utf-8') as log_file:
                log_file.write(
                    f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | "
                    f"function: {old_function.__name__} | "
                    f"args: {args} | kwargs: {kwargs} | "
                    f"result: {result}\n"
                )

            return result

        return new_function

    return __logger