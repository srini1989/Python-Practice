import random


def generate_code(limit=5):
    start = 10 ** (limit - 1)
    end = (10 ** limit) - 1
    return random.randint(start, end)


def create_message(name, vc):
    return "{}, Your verification code is {}".format(name, vc)


def send_message(to_number, name, from_number="+12234"):
    code = generate_code(limit=4)
    # print(code)
    message = create_message(name, code)
    print(message)
