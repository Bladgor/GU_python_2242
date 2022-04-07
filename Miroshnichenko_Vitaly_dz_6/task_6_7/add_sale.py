import json


def writing_value(argv):
    _, *args = argv

    with open('my_txt.txt', 'a', encoding='utf-8') as f, \
            open('bakery.csv', encoding='utf-8') as dict_index:
        if f.tell() == 0:
            price_dict = {'1': args[0]}
            f.write(f'_')
        else:
            price_dict = json.load(dict_index)
            price_dict[max(map(int, price_dict.keys())) + 1] = args[0]

    with open('bakery.csv', 'w', encoding='utf-8') as dict_index:
        json.dump(price_dict, dict_index)


if __name__ == '__main__':
    import sys

    exit(writing_value(sys.argv))
