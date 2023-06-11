import random

class Game:
    def __init__(self):
        self.board = [0 for _ in range(9)]

    def show_board(self) -> list[str]:
        tic_tac_toe_board = []
        for i in range(0, 9, 3):
            row = " ".join(map(str, self.board[i:i+3]))
            tic_tac_toe_board.append(row)
        return tic_tac_toe_board

    def restart_game(self):
        self.board = [0 for _ in range(9)]

    @property
    def possible_moves(self):
        return [i for i, cell in enumerate(self.board) if cell == 0]

    def player_move(self, field: int):
        if field in self.possible_moves:
            self.board[field] = "X"
            is_won = self.check_win()
            if is_won:
                return "GAME WON"
            return True
        return False

    def ai_move(self) -> int:
        while True:
            random_field = random.randint(1, 9)
            

    def check_win(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]  # Diagonals
        ]
        for combination in winning_combinations:
            a, b, c = combination
            if self.board[a] == self.board[b] == self.board[c] != 0:
                return True
        return False