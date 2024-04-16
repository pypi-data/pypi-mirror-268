import random
import re


def all_required(model: dict, required_args: list):
    for _req_arg in required_args:
        if model.get(_req_arg) is None:
            return False, _req_arg
    return True, None


def detect_browser(user_agent: str):
    browsers = {
        'brave': r'Brave',
        'firefox': r'Firefox',
        'edge': r'Edg',
        'safari': r'Safari',
        'opera': r'Opera|OPR',
        'internet_explorer': r'MSIE|Trident',
        'chrome': r'Chrome',
    }

    for browser, pattern in browsers.items():
        if re.search(pattern, user_agent):
            if browser == 'chrome':
                if 'Edg' not in user_agent and 'Brave' not in user_agent:
                    return browser
            elif browser == 'safari':
                if 'Chrome' not in user_agent and 'Brave' not in user_agent:
                    return browser
            else:
                return browser
    return 'unknown'


def format_user_agent(user_agent: str):
    _browser = detect_browser(user_agent).capitalize()
    return " - ".join(user_agent.split('(')[1].split(')')[0].split('; '))


def create_string(length: int = 32, lowercase: bool = True, uppercase: bool = True,
                  numbers: bool = True, symbols: bool = True):
    if not any([lowercase, uppercase, numbers, symbols]) or length <= 0:
        return None

    lowercase_set = "abcdefghijklmnopqrstuvwxyz"
    uppercase_set = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers_set = "0123456789"
    symbols_set = "!@#$%^&*()_-+=<>?"

    first_char_query = ""
    if lowercase:
        first_char_query += lowercase_set
    if uppercase:
        first_char_query += uppercase_set
    if numbers:
        first_char_query += numbers_set

    if length == 1:
        return random.choice(first_char_query)

    rest_query = first_char_query
    if symbols:
        rest_query += symbols_set

    result = random.choice(first_char_query)
    result += ''.join(random.choice(rest_query) for _ in range(length - 1))
    return result
