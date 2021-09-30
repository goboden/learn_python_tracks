from typing import Tuple
from urllib.parse import urlparse
from pathlib import Path
import yandex


parsers = {'market.yandex.ru': yandex, }


class ParserNotFound(Exception):
    def __init__(self, domain):
        self.text = f'Не найден модуль парсера для {domain}'


def get_page_filename(url: str, prefix=''):
    parse_result = urlparse(url)
    filename = f'{parse_result.netloc}{parse_result.path}'
    filename = filename.translate(str.maketrans('./', '__'))
    return prefix + filename + '.html'


def get_html_from_cache(url: str) -> str:
    filename = get_page_filename(url, prefix='g_')
    full_filename = Path(__file__).parent.joinpath('cache').joinpath(filename)
    if full_filename.exists():
        with open(full_filename, 'r', encoding='utf-8') as f:
            return f.read()
    return ''


def get_current_parser(url: str) -> Tuple:
    result = urlparse(url)
    domain = result.netloc
    current_parser = parsers.get(domain, False)
    return (domain, current_parser)


def get_price(url):
    domain, current_parser = get_current_parser(url)
    if not current_parser:
        raise ParserNotFound(domain)
    html = get_html_from_cache(url)
    if not html:
        html = current_parser.get_html(url)
    return current_parser.get_price(html)


if __name__ == '__main__':
    # url = 'https://market.yandex.ru/product--mysh-logitech-m90/6197603'
    url = 'https://market.yandex.ru/product--mysh-logitech-m90/6197603?cpa=1'
    print(get_price(url))
