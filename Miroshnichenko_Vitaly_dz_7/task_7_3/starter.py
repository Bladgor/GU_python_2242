import os
import shutil

starter_dict = {'my_project': [
    {'settings': [
        '__init__.py', 'dev.py', 'prod.py'
    ],
    },
    {'mainapp': [
        '__init__.py', 'models.py', 'views.py',
        {'templates': [
            {'mainapp': [
                'base.html', 'index.html'
            ]
            }]}
    ]
    },
    {'authapp': [
        '__init__.py', 'models.py', 'views.py',
        {'templates': [
            {'authapp': [
                'base.html', 'index.html'
            ]
            }]}
    ]
    }]}


def starter(data, path):
    if isinstance(data, dict):
        for key, value in data.items():
            cur_path = os.path.join(path, key)
            starter(value, cur_path)
    else:
        for elem in data:
            if isinstance(elem, dict):
                for key, value in elem.items():
                    cur_path = os.path.join(path, key)
                    starter(value, cur_path)
            else:
                cur_path = os.path.join(path, elem)
                if not os.path.exists(path):
                    os.makedirs(path)
                with open(cur_path, 'w') as f:
                    f.write('')


try:
    shutil.rmtree('my_project')
except FileNotFoundError:
    pass

my_path = os.getcwd()
starter(starter_dict, my_path)
