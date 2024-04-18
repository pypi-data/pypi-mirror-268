from toolboxv2.mods.CloudM import User


def get_user(user_token: str):
    if user_token.startswith("0"):
        return None
    if user_token.startswith("1"):
        return User(name="boot", email="root@example.com", level=100)

    return User(name="root", email="root@example.com", level=100)
