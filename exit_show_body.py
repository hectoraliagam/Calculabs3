from animation import *
from print_body import *

def exit_title():
    title = [
        "----------------------------------",
        "|      Gracias por utilizar      |",
        "|           CALCULABS            |",
        "|       Vuelva pronto! :D        |",
        "----------------------------------"
    ]
    return print_text(title)

def exit_menu_opt():
    while True:
        options = [
            "----------------------------------",
            "|    Salir --------------- s     |",
            "|    Menú Principal ------ p     |",
            "----------------------------------"
        ]
        print_text(options)
        exit_opt = input('| ins == ')
        if exit_opt == "s":
            clear_list_plus_one_line(options)
            exit_title()
            return -1
        elif exit_opt == "p":
            clear_list_plus_one_line(options)
            return 0
        else:
            clear_list_plus_one_line(options)

def exit_version_opt():
    while True:
        options = [
            "----------------------------------",
            "|    Regresar ------------ r     |",
            "----------------------------------"
        ]
        print_text(options)
        exit_opt = input('| ins == ')
        if exit_opt == "r":
            clear_list_plus_one_line(options)
            clear_previous_lines(2)
            return 0
        else:
            clear_list(options)
            clear_previous_lines(1)

def exit_calculator_menu_opt():
    while True:
        options = [
            "----------------------------------",
            "|    Volver -------------- v     |",
            "|    Calculadora --------- c     |",
            "----------------------------------"
        ]
        print_text(options)
        exit_opt = input('| ins == ')
        if exit_opt == "v":
            clear_list_plus_one_line(options)
            return -1
        elif exit_opt == "c":
            clear_list_plus_one_line(options)
            return 0
        else:
            clear_list(options)

def exit_key_panel_menu_opt():
    while True:
        options = [
            "----------------------------------",
            "|    Volver -------------- v     |",
            "|    Panel de Teclas ----- t     |",
            "----------------------------------"
        ]
        print_text(options)
        exit_opt = input('| ins == ')
        if exit_opt == "v":
            clear_list_plus_one_line(options)
            return -1
        elif exit_opt == "t":
            clear_list_plus_one_line(options)
            return 0
        else:
            clear_list_plus_one_line(options)

def exit_calculate_menu_opt():
    while True:
        options = [
            "----------------------------------",
            "|    Volver -------------- v     |",
            "|    Calcular ------------ c     |",
            "----------------------------------"
        ]
        print_text(options)
        exit_opt = input('| ins == ')
        if exit_opt == "v":
            clear_list_plus_one_line(options)
            clear_previous_lines(5)
            return -1
        elif exit_opt == "c":
            clear_list_plus_one_line(options)
            clear_previous_lines(5)
            return 0
        else:
            clear_list_plus_one_line(options)
