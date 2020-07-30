COOKIE_MAIN_ACCOUNT = ''
COOKIE_MAKER = ''

CAPTCHA_MAIN_ACCOUNT = ''
CAPTCHA_MAKER = ''

ACCOUNT_MAIN = ''
ACCOUNT_MAKER = ''

PASSWORD_MAIN_ACCOUNT = ''
PASSWORD_MAKER = ''

BOT_TOKEN = ''

MAIN_ACCOUNT_CHAR_ONE = ''
MAIN_ACCOUNT_CHAR_TWO = ''

MAKER_ACCOUNT_CHAR_ONE = ''


base_header = {
            'authority': 'www.demolidores.com.br',
            'cache-control': 'max-age=0',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
            'origin': 'https://www.demolidores.com.br',
            'content-type': 'application/x-www-form-urlencoded',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-user': '?1',
            'sec-fetch-dest': 'document',
            'referer': 'https://www.demolidores.com.br/?subtopic=accountmanagement',
            'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '',
}

base_data = {
    'account_login': '',
    'password_login': '',
    'g-recaptcha-response': '',
    'page': 'overview',
    'Login.x': '29',
    'Login.y': '9'
}

params = (
    ('subtopic', 'accountmanagement'),
)