import os
import shutil

dst = r'my_project\templates'
folder = r'my_project'
if not os.path.exists(dst):
    os.mkdir(dst)

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(".html"):
            try:
                src = str(root).split('\\')
                full_path = os.path.join(src[0], src[2], src[3])
                if not os.path.exists(full_path):
                    os.mkdir(full_path)
                file_path = os.path.join(root, file)
                full_path = os.path.join(full_path, file)
                if not os.path.exists(full_path):
                    with open(file_path, 'r') as fsrc, open(full_path, 'w') as fdst:
                        shutil.copyfile(file_path, full_path)
            except IndexError:
                print()
