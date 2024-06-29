# CALCULABS
# by Hector Aliaga

from show_body import *

while True:
    menu_title()
    opt = menu_opt()
    if opt == 0:
        if exit_menu_opt() == -1:
            break
    elif opt == 9:
        version_title()
        if exit_version_opt() == -1:
            break
    elif opt == 8:
        while True:
            calculator_opt = calculator_menu_opt()
            if calculator_opt == 0:
                if exit_calculator_menu_opt() == -1:
                    break
            elif calculator_opt == -1:
                break
            elif calculator_opt == 9:
                while True:
                    key_panel_opt = key_panel_menu_opt()
                    if key_panel_opt == 0:
                        if exit_key_panel_menu_opt() == -1:
                            break
                    elif key_panel_opt == -1:
                        break
                    elif key_panel_opt == 9:
                        basic_operator_title()
                        if exit_key_panel_menu_opt() == -1:
                            break
                    elif key_panel_opt == 8:
                        basic_math_function_title()
                        if exit_key_panel_menu_opt() == -1:
                            break
                    elif key_panel_opt == 7:
                        trigonometric_function_title()
                        if exit_key_panel_menu_opt() == -1:
                            break
                    elif key_panel_opt == 6:
                        math_constant_title()
                        if exit_key_panel_menu_opt() == -1:
                            break
                    elif key_panel_opt == 5:
                        additional_function_title()
                        if exit_key_panel_menu_opt() == -1:
                            break
            elif calculator_opt == 8:
                while True:
                    calculate_title()
                    print(perform_operation())
                    if exit_calculate_menu_opt() == -1:
                        break
                    