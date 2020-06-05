import json


def get_sorted_username():
    """如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_sorted_username()
    if username:
        result = input(username + " is right?")
        if result == 'y':
            print("Welcom back,", username, "!")
        else:
            username = get_new_username()
            print("Welcom back,", username, "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back,", username, "!")


if __name__ == "__main__":
    greet_user()
