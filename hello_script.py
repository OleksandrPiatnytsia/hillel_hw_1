import datetime


def hello():
    user_name = input("Input your name >> ")

    now = datetime.datetime.now()

    current_date = now.strftime("%A %d.%m.%Y")

    print(f"Hello, {user_name}.")
    print(f"Today is {current_date}")


if __name__ == "__main__":
    hello()
