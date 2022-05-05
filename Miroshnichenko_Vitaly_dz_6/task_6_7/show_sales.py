import json


def print_value(my_list, my_dict):
    for elem in my_list:
        print(my_dict[elem])


def show_value(argv):
    _, *args = argv
    with open('bakery.csv', encoding='utf-8') as f:
        data = json.load(f)
        keys_list = sorted(list(data.keys()))
        if len(args) == 0:
            pass
        elif len(args) == 1:
            start_idx = keys_list.index(args[0])
            keys_list = keys_list[start_idx:]
        else:
            start_idx = keys_list.index(args[0])
            end_idx = keys_list.index(args[1]) + 1
            keys_list = keys_list[start_idx:end_idx]
        print_value(keys_list, data)


if __name__ == '__main__':
    import sys

    exit(show_value(sys.argv))
