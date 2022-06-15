#!/usr/bin/python
import subprocess

subprocess.call('cp dz1_1.py dz1_run.py', shell=True)
print('Файл dz_1.py скопирован в dz1_run.py')
print()
subprocess.call('chmod ugo-rwx dz1_run.py', shell=True)
print('Доступ к dz1_run.py полностью запрещен для всех кроме овнера')
print()
subprocess.call('chmod u+rx dz1_run.py', shell=True)
print('Овнер может читать и запускать файл dz1_run.py')
print()
print('Запуск файла dz1_run.py')
print()
subprocess.call('./dz1_run.py', )


