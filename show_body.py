from animation import *
from print_body import *
from exit_show_body import *

def menu_title():
    title = [
        "----------------------------------",
        "|     BIENVENIDO A CALCULABS     |"
    ]
    return print_text(title)

def menu_opt():
    title = [
        "|--------------------------------|",
        "|    MENÚ PRINCIPAL:             |"
    ]
    options = [
        "|    Salir --------------- 0     |",
        "|    Versión ------------- 9     |",
        "|    Calculadora --------- 8     |",
        "|    Álgebra ------------- 7     |",
        "|    Geometría ----------- 6     |",
        "|    Conversor de                |",
        "|    Unidades     -------- 5     |",
        "|    Finanzas ------------ 4     |",
        "|    Salud --------------- 3     |",
        "|    Otros --------------- 2     |",
        "|    Configuración ------- 1     |",
        "----------------------------------"
    ]
    opt_choise = print_menu_choise(title,options)
    if opt_choise == 0:
        clear_list_plus_one_line(title + options)
        clear_previous_lines(2)
    elif opt_choise == 9:
        clear_list_plus_one_line(title + options)
        clear_previous_lines(2)
    else:
        clear_list(title + options)
        clear_previous_lines(3)
    return opt_choise

def version_title():
    title = [
        "----------------------------------",
        "|         Versión: 3.0.0         |"
    ]
    return print_text(title)

def calculator_menu_opt():
    title = [
        "----------------------------------",
        "|    CALCULADORA:                |"
    ]
    options = [
        "|    Volver -------------- 0     |",
        "|    Panel de Teclas ----- 9     |",
        "|    Calcular ------------ 8     |",
        "----------------------------------"
    ]
    opt_choise = print_menu_choise(title,options)
    if opt_choise == 0:
        clear_list_plus_one_line(title + options)
    else:
        clear_list_plus_one_line(title + options)
    return opt_choise

def key_panel_menu_opt():
    title = [
        "----------------------------------",
        "|    PANEL DE TECLAS:            |"
    ]
    options = [
        "|    Volver -------------- 0     |",
        "|    Operadores básicos -- 9     |",
        "|    Funciones                   |",
        "|    matemáticas                 |",
        "|    básicas ------------- 8     |",
        "|    Funciones                   |",
        "|    trigonométricas ----- 7     |",
        "|    Constantes                  |",
        "|    matemáticas --------- 6     |",
        "|    Funciones                   |",
        "|    adicionales --------- 5     |",
        "----------------------------------"
    ]
    opt_choise = print_menu_choise(title,options)
    if opt_choise == 0:
        clear_list_plus_one_line(title + options)
    else:
        clear_list_plus_one_line(title + options)
    return opt_choise

def basic_operator_title():
    title = [
        "----------------------------------",
        "|    OPERADORES BÁSICOS:         |"
    ]
    options = [
        '|    Adición ----------- (+)     |',
        '|    Sustracción ------- (-)     |',
        '|    Multiplicación ---- (*)     |',
        '|    División ---------- (/)     |',
        "----------------------------------"
    ]
    print_menu_choise(title,options)

def basic_math_function_title():
    title = [
        "----------------------------------",
        "|    FUNCIONES MATEMÁTICAS       |",
        "|    BÁSICAS:                    |"
    ]
    options = [
        '|    Potencia ---------- (^)     |',
        '|    Raíz cuadrada -- (sqrt)     |',
        '|    Logaritmo en                |',
        '|    base 10 --------- (log)     |',
        '|    Logaritmo                   |',
        '|    natural ---------- (ln)     |',
        '|    Exponencial ----- (exp)     |',
        "----------------------------------"
    ]
    print_menu_choise(title,options)

def trigonometric_function_title():
    title = [
        "----------------------------------",
        "|    FUNCIONES                   |",
        "|    TRIGONOMÉTRICAS:            |"
    ]
    options = [
        '|    Seno ------------ (sin)     |',
        '|    Coseno ---------- (cos)     |',
        '|    Tangente -------- (tan)     |',
        '|    Sen inverso ---- (asin)     |',
        '|    Cos inverso ---- (acos)     |',
        '|    Tan inverso ---- (atan)     |',
        "----------------------------------"
    ]
    print_menu_choise(title,options)

def math_constant_title():
    title = [
        "----------------------------------",
        "|    CONSTANTES MATEMÁTICAS:     |"        
    ]
    options = [
        '|    Pi --------------- (pi)     |',
        '|    Euler ------------- (e)     |',
        "----------------------------------"        
    ]
    print_menu_choise(title,options)

def additional_function_title():
    title = [
        "----------------------------------",
        "|    FUNCIONES ADICIONALES:      |"
    ]
    options = [
        '|    Valor absoluto -- (abs)     |',
        '|    Factorial ------ (fact)     |',
        "----------------------------------"   
    ]
    print_menu_choise(title,options)

def calculate_title():
    title = [
        "----------------------------------",
        "|    CALCULAR:                   |",
        "|    Terminar ---------- '='     |",
        "|--------------------------------|"
    ]
    return print_text(title)

def get_number(prompt="| num == "):
    while True:
        num = input(prompt)
        try:
            return float(num)
        except ValueError:
            clear_previous_lines(1)
            continue

def perform_operation():
    result = get_number()
    clear_list([result])
    division_by_zero = 0
    while True:
        operation = input("| op  == ")
        if division_by_zero == 1:
            clear_list([operation])
            division_by_zero = 0

        clear_list([operation])
        if operation == '=':
            clear_list([operation])
            break
        elif operation in ['+', '-', '*', '/', '^', '*/']:
            num = get_number()
            if (operation == '/' and num == 0):
                clear_list([operation])
                print("|        División por cero       |")
                division_by_zero = 1
                continue
            elif operation == '+':
                result += num
                clear_list([result])
            elif operation == '-':
                result -= num
                clear_list([result])
            elif operation == '*':
                result *= num
                clear_list([result])
            elif operation == '/':
                result /= num
                clear_list([result])
            elif operation == '**':
                result **= num
                clear_list([result])
            elif operation == '*/':
                result **= (1 / num)
                clear_list([result])
    print("|--------------------------------|")
    if result.is_integer():
        return f"| res == {int(result)}"
    return f"| res == {result}"
