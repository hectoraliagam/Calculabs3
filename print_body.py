from animation import *

def print_text(options):
    for text in options:
        print(text)
    return

def print_menu(title,options):
    for text in title:
        print(text)
    for option in options:
        print(option)
    return

def print_text_choise(options):
    for text in options:
        print(text)
    # choise = get_limited_input('| ins == ')
    choise = input('| ins == ')
    if choise.isdigit():
        return int(choise)
    return choise

def print_menu_choise(title,options):
    for text in title:
        print(text)
    for option in options:
        print(option)
    # choise = get_limited_input('| ins == ')
    choise = input('| ins == ')
    if choise.isdigit():
        return int(choise)
    return choise
