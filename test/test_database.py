import database


def test_users():
    database.add_user(1, 'a', 1)
    assert False
