from models.user import User


def test_can_instanciate_user():
    user = User(1, "Charles", "TI", "charles@test.com", 1)

    assert isinstance(user, User)
