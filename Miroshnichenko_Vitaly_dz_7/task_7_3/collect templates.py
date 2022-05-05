import os
import shutil

root = 'my_project'

for r, d, f in os.walk(root):
    for folder in d:
        if folder == 'templates':
            cur_path = os.path.join(r, folder)
            if cur_path != os.path.join(root, 'templates'):
                try:
                    shutil.move(cur_path, root)
                except shutil.Error:
                    for elem in os.listdir(cur_path):
                        sub_cur_path = os.path.join(cur_path, elem)
                        shutil.move(sub_cur_path, os.path.join(root, folder))
                    os.rmdir(cur_path)
