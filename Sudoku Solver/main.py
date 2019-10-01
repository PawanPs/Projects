#main_file_import--------------------------
from Sudoko_solver import *
import ctypes
import os

os.system('mode 55,35')     
os.system('color 0C')
ctypes.windll.kernel32.SetConsoleTitleW("Sudoku Solver")

#input board-------------------------------
def enter_board():
    board = []
    i = 1
    print('\n**Enter 0 in case of empty box')
    while i != 10:
        temp = input("Enter "+str(i)+"th row elements: ")
        if not(temp.isnumeric()) or len(temp) != 9:
            print('Invalid Data!\n')
            continue
        
        temp = list(temp)    
        board.append([int(x) for x in temp])
        i += 1
    return board

#main_loop---------------------------------

running = True

while running:
    print('\nMenu\n\n1.Solve\n2.Exit\n')
    option = input('Enter option: ')
    if option == '1':
        board = enter_board()
        result = solve(board)
        if  result:
            print('\n')
            print_board(board)
        else:
            print('\n\nUnsolvable Board!')

        
    elif option == '2':
        running = False
    else:
        print('\nPlease enter \'option 1\' or \'option 2\'')
quit()
