#!/usr/bin/python
import subprocess
from datetime import datetime
from calendar import monthrange


def days_amount():
    current_year = datetime.now().year
    current_month = datetime.now().month
    days_in_month = monthrange(current_year, current_month)[1]
    return days_in_month


def files_generate(file):
    days = days_amount()
    for i_day in range(days):
        if i_day == 0:
            continue
        elif i_day <= 8:
            cnt_s = '0' + str(i_day)
            i_day += 1
        else:
            i_day += 1
            cnt_s = i_day
        files_list.append(str(cnt_s) + file)
    return files_list


def remove_files(files, dir):
    import random
    original_lst = files.copy()
    for _ in range(5):
        r_file = files.pop(random.randrange(len(files)))
        subprocess.call('sudo rm -f ' + r_file, shell=True, cwd=dir)
        print(f'Файл {r_file} был удален')


cnt = 1
cnt_s = ''
files_list = []
folder = str(subprocess.getoutput('pwd')) + '/dz1'
file_name = datetime.today().strftime('-%m-%Y') + '.log'
print('Текущий пользователь:')
print(subprocess.getoutput('whoami'))
print()
print('Полный путь где вы находитесь: ')
print(subprocess.getoutput('pwd'))

subprocess.call("mkdir dz1", shell=True)
print()
lst_logs = files_generate(file_name)

for gen_f in lst_logs:
    subprocess.call('touch ' + gen_f, shell=True, cwd=folder)

subprocess.call('sudo chown -R root ' + folder, shell=True)
print('Овнер папки dz1 был изменен на root')
print()

remove_files(files_list, folder)
