import time

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.current_state = [['_' for _ in range(3)] for _ in range(3)]
        self.player_turn = input("Choose your symbol (X/O): ").upper()

    def draw_board(self):
        for i in range(0, 3):
            for j in range(0, 3):
                print('{}|'.format(self.current_state[i][j]), end=" ")
            print()
        print()

    def is_valid(self, px, py):
        if px < 0 or px > 2 or py < 0 or py > 2:
            return False
        elif self.current_state[px][py] != '_':
            return False
        else:
            return True

    def is_end(self):
        for i in range(0, 3):
            if (self.current_state[0][i] != '_' and
                self.current_state[0][i] == self.current_state[1][i] and
                self.current_state[1][i] == self.current_state[2][i]):
                return self.current_state[0][i]

        for i in range(0, 3):
            if (self.current_state[i][0] != '_' and
                self.current_state[i][0] == self.current_state[i][1] and
                self.current_state[i][1] == self.current_state[i][2]):
                return self.current_state[i][0]

        if (self.current_state[0][0] != '_' and
            self.current_state[0][0] == self.current_state[1][1] and
            self.current_state[0][0] == self.current_state[2][2]):
            return self.current_state[0][0]

        if (self.current_state[0][2] != '_' and
            self.current_state[0][2] == self.current_state[1][1] and
            self.current_state[0][2] == self.current_state[2][0]):
            return self.current_state[0][2]

        for i in range(0, 3):
            for j in range(0, 3):
                if (self.current_state[i][j] == '_'):
                    return None

        return '_'

    def max_alpha_beta(self, alpha, beta):
        maxv = -2
        px = None
        py = None

        result = self.is_end()

        if result == self.player_turn:
            return (-1, 0, 0)
        elif result == 'O' and self.player_turn == 'X' or result == 'X' and self.player_turn == 'O':
            return (1, 0, 0)
        elif result == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '_':
                    if self.player_turn == 'X':
                        self.current_state[i][j] = 'O'
                    else:
                        self.current_state[i][j] = 'X'
                    (m, min_i, min_j) = self.min_alpha_beta(alpha, beta)
                    if m > maxv:
                        maxv = m
                        px = i
                        py = j
                    self.current_state[i][j] = '_'

                    if maxv >= beta:
                        return (maxv, px, py)

                    if maxv > alpha:
                        alpha = maxv

        return (maxv, px, py)

    def min_alpha_beta(self, alpha, beta):
        minv = 2

        qx = None
        qy = None

        result = self.is_end()

        if result == self.player_turn:
            return (-1, 0, 0)
        elif result == 'O' and self.player_turn == 'X' or result == 'X' and self.player_turn == 'O':
            return (1, 0, 0)
        elif result == '_':
            return (0, 0, 0)

        for i in range(0, 3):
            for j in range(0, 3):
                if self.current_state[i][j] == '_':
                    if self.player_turn == 'X':
                        self.current_state[i][j] = 'X'
                    else:
                        self.current_state[i][j] = 'O'
                    (m, max_i, max_j) = self.max_alpha_beta(alpha, beta)
                    if m < minv:
                        minv = m
                        qx = i
                        qy = j
                    self.current_state[i][j] = '_'

                    if minv <= alpha:
                        return (minv, qx, qy)

                    if minv < beta:
                        beta = minv

        return (minv, qx, qy)

    def play(self):
        while True:
            self.draw_board()
            self.result = self.is_end()

            if self.result != None:
                if self.result == 'X':
                    print('The winner is X!')
                elif self.result == 'O':
                    print('The winner is O!')
                elif self.result == '_':
                    print("It's a tie!")

                self.initialize_game()
                return

            if self.player_turn == 'X':
                while True:
                    start = time.time()
                    (m, qx, qy) = self.min_alpha_beta(-2, 2)
                    end = time.time()
                    print('Evaluation time: {}s'.format(round(end - start, 7)))
                    print('Recommended move: X = {}, Y = {}'.format(qx, qy))

                    px = int(input('Insert the X coordinate: '))
                    py = int(input('Insert the Y coordinate: '))

                    qx = px
                    qy = py

                    if self.is_valid(px, py):
                        self.current_state[px][py] = 'X'
                        self.player_turn = 'O'
                        break
                    else:
                        print('The move is not valid! Try again.')

            else:
                (m, px, py) = self.max_alpha_beta(-2, 2)
                self.current_state[px][py] = 'O'
                self.player_turn = 'X'


def main():
    g = Game()
    g.play()


if __name__ == "__main__":
    main()




