import random


def gen_token(length, special_chars=False, upper_case_only=True):
    """
        Generates random token for various use cases
    """
    chars = "abcdefghijkmnpqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ0123456789"

    if special_chars:
        chars += "~!@#$%^&*()?+_-[]{};><"

    token = "".join(random.choice(chars) for x in range(length))

    if upper_case_only:
        token = token.upper()

    return token


def slugify(name):
    """
    creates a shortened form of school name
    """
    split = name.split(' ')
    if len(split) > 1:
        return split[0].lower() + '_' + split[1].lower()[0]
    return split[0].lower()
