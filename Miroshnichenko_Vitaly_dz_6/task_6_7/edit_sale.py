import json


def edit_value(argv):
    _, *args = argv
    with open('bakery.csv', encoding='utf-8') as f:
        data = json.load(f)
        data[args[0]] = args[1]

    with open('bakery.csv', 'w', encoding='utf-8') as f:
        json.dump(data, f)


if __name__ == '__main__':
    import sys

    exit(edit_value(sys.argv))
