import sys
import msvcrt

def clear_list(items):
    for _ in items:
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')

def clear_list_plus_one_line(items):
    for _ in items:
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')
    sys.stdout.write('\033[F')
    sys.stdout.write('\033[K')

def clear_previous_lines(items):
    for _ in range(items):
        sys.stdout.write('\033[F')
        sys.stdout.write('\033[K')
    return items

def delete_last_character():
    sys.stdout.write('\033[D')
    sys.stdout.write('\033[K')
    sys.stdout.flush()


# def get_limited_input(prompt, max_length=23):
#     print(prompt, end='', flush=True)
#     user_input = []
#     while True:
#         char = msvcrt.getch
#         if char in (b'\n',b'\r'):
#             break
#         if char == b'\x08':
#             if user_input:
#                 delete_last_character()
#                 user_input.pop()
#         elif len(user_input) < max_length:
#             user_input.append(char.decode())
#             sys.stdout.write(char.decode())
#             sys.stdout.flush()
#         else:
#             delete_last_character()
#     print()
#     return ''.join(user_input)
