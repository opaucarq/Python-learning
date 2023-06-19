board = {'7': ' ', '8': ' ', '9': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '1': ' ', '2': ' ', '3': ' '}

keys = board.keys()

def printBoard(board):
    print(f"{board['7']}|{board['8']}|{board['9']}")
    print("-+-+-")
    print(f"{board['4']}|{board['5']}|{board['6']}")
    print("-+-+-")
    print(f"{board['1']}|{board['2']}|{board['3']}")


def game():
    turn = 'x'
    count = 0
    played_once = False

    while True:
        printBoard(board)

        move = input(f"It is {turn}'s turn. Specify the place you want to go: ")

        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("Sorry, this cell location is filled. Please choose another one.")
            continue

        if (
            (board['7'] == board['8'] == board['9'] != ' ') or
            (board['4'] == board['5'] == board['6'] != ' ') or
            (board['1'] == board['2'] == board['3'] != ' ') or
            (board['1'] == board['4'] == board['7'] != ' ') or
            (board['2'] == board['5'] == board['8'] != ' ') or
            (board['3'] == board['6'] == board['9'] != ' ') or
            (board['1'] == board['5'] == board['9'] != ' ') or
            (board['3'] == board['5'] == board['7'] != ' ')
        ):
            printBoard(board)
            print("...Game Over...")
            print(f"Player {turn} won the game")
            break

        if count == 9:
            printBoard(board)
            print("...Game Over...")
            print("It's a tie!")
            break

        if turn == 'x':
            turn = 'o'
        else:
            turn = 'x'
    
    restart = input("Do you want to try again? (y/n): ")

    if restart.lower() == 'y':
        for i in keys:
            board[i] = ' '
        game()
    elif not played_once:
        played_once = True
        print("Thanks for playing...")
    else:
        print("Thanks for playing...")

if __name__ == "__main__":
    game()
