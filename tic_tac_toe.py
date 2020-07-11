from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
    '''
    function display_board prints out a board. Board is set as a list, where each index 1-9 corresponds with a number on a number pad,
    so we get a 3 by 3 board representation
    '''

def player_input():
    marker =''
    while marker != 'X' and marker != 'O':
        marker = input('Player 1,choose X or O: ').upper()
        
        if marker == 'X':
            return ('X','O')
        else:
            return ('O','X')
     '''
      function player_input takes in a player input and assigns their marker as 'X' or 'O'
     '''

def place_marker(board, marker, position):
    board[position] = marker
    '''
    function place_marker takes in the board list object, a marker ('X' or 'O'), and a desired position (number 1-9) and assigns it to the board
    '''

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    '''
    function win_check takes in a board and a marks (X or O) and then checks to see if that mark has won
    '''

import random
def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
    '''
    function choose_first uses the random module to randomly decide which player goes first and returns a string of which player went first
    '''

def space_check(board, position):
    
    return board[position] == ' '
    '''
    function space_check returns a boolean indicating whether a space on the board is freely available
    '''

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True
    '''
    function full_board_check checks if the board is full and returns a boolean value. True if full, False otherwise
    '''

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position
    '''
    function player_choice asks for a player's next position (as a number 1-9) and then uses the space_check function to check if it's a free position.
    If it is, then return the position for later use
    '''

def replay():
    choice = input("Do you want to play again?[Y/N]: ").upper()
    return choice == 'Y'
    '''
    Function replay asks the player if they want to play again and returns a boolean True if they do want to play again
    '''

print('Welcome to Tic Tac Toe!')

# while loop to keep running the game
while True:
    # Reset the board
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play?[Y/N]:').upper()
    
    if play_game == 'Y':
        game_on = True
    else:
        game_on = False
    
    # game play
    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print('Congrats!Player 1 has won')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Congrats!Player 2 has won!')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    # break out of the while loop on replay()
    if not replay():
        break   
