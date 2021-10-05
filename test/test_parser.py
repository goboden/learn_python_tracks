import url_parser
import pytest


def test_hobbygames():
    url = 'https://hobbygames1.ru/codex-deathwatch-hardback'
    assert pytest.raises(url_parser.ParserNotFound, url_parser.get_parser, url)

    url = 'https://hobbygames.ru/codex-deathwatch-hardback'
    current_parser = url_parser.get_parser(url)
    assert False, current_parser.validate()

