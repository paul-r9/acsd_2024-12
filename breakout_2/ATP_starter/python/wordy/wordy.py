import re


def answer(question):
    pattern = r"^What is (-?\d+)(.*)\?$"
    match = re.search(pattern, question)

    if not match:
        return None

    number = match.group(1)
    rest = match.group(2)

    if not rest:
        return int(number)

    match = re.search(pattern, expression)
    if match:
        return int(match.group(1))

    pattern = r"^ plus (-?\d+)$"
    match = re.search(pattern, expression)
    if match:
        return int(match.group(1)) + int(match.group(2))

    pattern = r"^(-?\d+) minus (-?\d+)$"  # should we support 'subtract'?
    match = re.search(pattern, expression)
    if match:
        return int(match.group(1)) - int(match.group(2))

    pattern = r"^(-?\d+) multiplied by (-?\d+)$"  # times?
    match = re.search(pattern, expression)
    if match:
        return int(match.group(1)) * int(match.group(2))

    pattern = r"^(-?\d+) divided by (-?\d+)$"
    match = re.search(pattern, expression)
    if match:
        return int(match.group(1)) / int(match.group(2))

    # questions like: what is the capital?
    return None
