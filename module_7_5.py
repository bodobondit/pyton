import os
import time
print(os.path.abspath(__file__))
for root, dirs, files in os.walk('/Users/vadim/PycharmProjects/TestBot/Bot'):
  for file in files:
    filepath = os.path.join(root,file)
    filetime = os.path.getmtime(filepath)
    formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
    filesize = os.path.getsize(filepath)
    parent_dir = os.path.dirname(filepath)
    print(f'Обнаружен файл: {file}, Путь: {filepath}, '
          f'Размер: {filesize} байт, Время изменения: {formatted_time}, '
          f'Родительская директория: {parent_dir}')
    print('path', os.path.dirname(file))

