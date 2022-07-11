#!/usr/local/bin/python3
import subprocess


def ping_ip(ip_address):
    reply = subprocess.run(['ping', '-c', '3', ip_address],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        t = tuple(reply.stdout.split('\n'))
        for t_i in t:
            print(t_i)
        return True

    else:
        e = tuple(reply.stderr.split('\n'))
        for e_i in e:
            print(e_i)
        return False


print(ping_ip(input('Введите ip: ')))
print(ping_ip('a'))#это для теста если к примеру айпи не отвечает
