class TicTacToe:
    def __init__(self):
        # Initialize the board with empty space
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def print_board(self):
        """Print the current state of board."""
        for row in [[self.board[(i*3):(i+1)*3]] for i in range(3)]:
            print('| '+ ' | '.join(row)+' |')

    def available_move(self):
        """Reaturn a list of available move(indices of empty space)."""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, square):
        "Make a move on the board."
        if self.board[square] == ' ':
            self.board[square] = self.current_player
            return True
        else:
            return False

    def check_winner(self):
        "Check if there is a winner"
        pass

    def game_over(self):
        """Check if the game is over (either a winner or draw)"""
        pass

    def play(self):
        """Main game loop"""
        pass

if __name__ == '__main__':
    pass