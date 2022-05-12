'''
Tic-Tac-Toe Game Assignment:
Simon Mule
'''


def main():

    player = switch_player("")
    playing_board = make_playing_board()

    while not (there_is_winner(playing_board) or is_a_draw(playing_board)):

        display_board(playing_board)
        make_move(player, playing_board)
        player = switch_player(player)

    display_board(playing_board)
    print("Great Game!")


def make_playing_board():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def display_board(playing_board):
    print(f"\n{playing_board[0]} | {playing_board[1]} | {playing_board[2]}")
    print('--+--+---')
    print(f"{playing_board[3]} | {playing_board[4]} | {playing_board[5]}")
    print('--+--+---')
    print(f"{playing_board[6]} | {playing_board[7]} | {playing_board[8]}\n")


def is_a_draw(board):
    for square in range(9):
        if board[square] != "X" and board[square] != "O":
            return False
    return True


def there_is_winner(playing_board):
    return (
        playing_board[0] == playing_board[1] == playing_board[2] or
        playing_board[3] == playing_board[4] == playing_board[5] or
        playing_board[6] == playing_board[7] == playing_board[8] or
        playing_board[0] == playing_board[3] == playing_board[6] or
        playing_board[1] == playing_board[4] == playing_board[7] or
        playing_board[2] == playing_board[5] == playing_board[8] or
        playing_board[0] == playing_board[4] == playing_board[8] or
        playing_board[2] == playing_board[4] == playing_board[6]
    )


def make_move(player, playing_board):

    box = int(
        input(f"{player}'s turn to play.Choose number between 1 - 9 for a square: "))
    playing_board[box - 1] = player


def switch_player(active_player):
    if active_player == "X" or active_player == "":
        return "O"
    elif active_player == "O":
        return "X"


if __name__ == "__main__":
    main()
