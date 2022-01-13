#tictactoe assignment 1
#Student: Aitana Toscano Cedeño.

def main():
    player1 = input('Player 1, please choose your nickname: ')
    player2= input('Player 2, please choose your nickname: ')
    board = draw_board()

    while not (end_game(board)):
        print()
        display_board(board)
        print()
        turn1(player1, board)
        print()
        display_board(board)
        print()
        turn2(player2, board)
        
    display_board(board)
    print('Congratulations to the winner.')

def draw_board():
    board =[]
    for spot in range(9):
        board.append(spot + 1)
    return board

def display_board(board):
    print(f'{board[0]}|{board[1]}|{board[2]}')
    print(f'{board[3]}|{board[4]}|{board[5]}')
    print(f'{board[6]}|{board[7]}|{board[8]}')

def turn1(player1, board):
    choose = input(f'{player1.upper()}, please choose a number available from 1 to 9: ')
    choose = int(choose)
    if choose <= 9:
        board[choose - 1] = "\033[2;31;40mX\033[2;37;40m"

def turn2(player2, board):
    choose = input(f'{player2.upper()}, please choose a number available from 1 to 9: ')
    choose = int(choose)
    if choose <= 9:
        board[choose - 1] = "\033[2;34;40mO\033[2;37;40m"

def end_game(board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
            
if __name__ == "__main__":
    main()