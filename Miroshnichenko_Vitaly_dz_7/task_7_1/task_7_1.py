import os

starter = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}

for dir in starter:
    if os.path.exists(dir):
        print('Папка', dir, 'уже существует.\n'
                            'Будет выполнена проверка вложенных папок. '
                            'Если какая-то отсутствует, то она будет создана.')
        for folder in starter[dir]:
            cur_path = os.path.join(dir, folder)
            if not os.path.exists(cur_path):
                os.mkdir(cur_path)
    else:
        for folder in starter[dir]:
            cur_path = os.path.join(dir, folder)
            os.makedirs(cur_path)
