import os

def check_os():
    if os.name != 'nt':
        print("Please use this on a windows device!")
        exit(1)

def cls():
    os.system("cls")