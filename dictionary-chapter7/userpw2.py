# !/usr/bin/env python
# coding=utf-8

from time import time, ctime # 导入时间模块
db = {}


def new_user():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if name in db:
            prompt = 'name taken, try another:'
            continue
        else:
            break

    pwd = raw_input('passwd: ')
    db[name] = pwd


def old_user():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name
    else:
        print 'login incorrect'


def show_menu():
    prompt = """
    (N)ew User Login
    (E)xisting User Login
    (Q)uit
    Enter choice:"""
    operate_str = "neq"
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except(EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\n You picked [%s]' % choice

            if choice not in operate_str:
                print 'invalid option,try again'
            else:
                chosen = True
        if choice == 'q':
            break
        elif choice == 'n':
            new_user()
        else:
            old_user()

if __name__ == "__main__":
    show_menu()
