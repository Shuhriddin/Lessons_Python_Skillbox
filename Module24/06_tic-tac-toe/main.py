# TODO здесь писать код
class Cell:
    def __init__(self, number):
        self.number = number
        self.symbol = ' '
        self.occupied = False

class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def display(self):
        for i in range(0, 9, 3):
            print(f"{self.cells[i].symbol}|{self.cells[i+1].symbol}|{self.cells[i+2].symbol}")
            if i < 6:
                print("-----")

    def change_cell_state(self, cell_number, symbol):
        cell = self.cells[cell_number - 1]
        if not cell.occupied:
            cell.symbol = symbol
            cell.occupied = True
            return True
        else:
            return False

    def check_game_end(self):
        winning_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        for combo in winning_combinations:
            if self.cells[combo[0]].symbol == self.cells[combo[1]].symbol == self.cells[combo[2]].symbol != ' ':
                return True
        return False


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self):
        while True:
            try:
                move = int(input(f"{self.name}, введите номер клетки для вашего символа '{self.symbol}': "))
                if 1 <= move <= 9:
                    return move
                else:
                    print("Некорректный ввод. Введите число от 1 до 9.")
            except ValueError:
                print("Некорректный ввод. Введите число от 1 до 9.")

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]

    def play_turn(self, player):
        self.board.display()
        move = player.make_move()
        if self.board.change_cell_state(move, player.symbol):
            if self.board.check_game_end():
                self.board.display()
                print(f"{player.name} победил!")
                return True
        else:
            print("Эта клетка уже занята. Попробуйте другую.")
        return False

    def play_game(self):
        for _ in range(9):
            for player in self.players:
                if self.play_turn(player):
                    return
        self.board.display()
        print("Ничья!")

    def start(self):
        while True:
            self.board = Board()
            self.play_game()
            play_again = input("Хотите сыграть еще раз? (да/нет): ")
            if play_again.lower() != 'да':
                break

player1 = Player("Игрок 1", "X")
player2 = Player("Игрок 2", "O")
game = Game(player1, player2)
game.start()