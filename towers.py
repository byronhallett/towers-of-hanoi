class GameError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)

class State:
    def __init__(self, disc_count):
        # Stack all discs on the left column
        self.disc_count = disc_count
        self.left = [i for i in range(disc_count, 0, -1)]
        self.middle = []
        self.right = []
        self.complete = False
        self.turns = 0

    def __str__(self):
        '''
        Print self as a pretty picture
        '''
        string = ""
        all = [self.left, self.middle, self.right]
        string += "  |    |    |  \n"
        height = self.disc_count - 1
        for i in range(height, -1, -1):
            printables = {}
            for tower in all:
                if len(tower) > i:
                    string += "  {}  ".format(tower[i])
                else:
                    string += "  |  "
            string += "\n"
        # print a nice base
        string += "===============  turns: {}\n".format(self.turns)
        string += "= L == M == R =\n"
        return string

    def move_disc(self, stack_from, stack_to, quiet=False):
        # ensure move is legal
        if len(stack_to) > 0 and stack_from[-1] > stack_to[-1]:
            raise GameError(
                "Illegal move, larger disc would be placed on smaller one.")
        # try to move
        stack_to.append(stack_from.pop())
        # if succeed, incrmeent turns
        self.turns += 1
        # show new state if not quiet
        if not quiet:
            print(self)

class Game:
    def __init__(self, disc_count):
        self.state = State(disc_count)

    def complete(self):
        return (len(self.state.left) + len(self.state.middle)) == 0

    def symbol_to_tower(self, symbol):
        if (symbol == "L"):
            return self.state.left
        if (symbol == "M"):
            return self.state.middle
        if (symbol == "R"):
            return self.state.right
        raise GameError("Must be one of L, M, R")

    def get_move(self):
        while True:
            try:
                stack_from = self.symbol_to_tower(input("Move from (L M R): "))
                stack_to = self.symbol_to_tower(input("Move to (L M R): "))
                # play this move
                self.state.move_disc(stack_from, stack_to)
                break  # allow break if two good symbols parsed and played
            except GameError as e:
                print(e)
            except IndexError as e:
                print("That tower is empty!")

    def optimal_turns(self):
        return 2 ** self.state.disc_count - 1

    def game_over(self):
        if self.state.turns == self.optimal_turns():
            print("Omg, you win in only {} turns.".format(
                self.state.turns), end=' ')
            print("Thats the best possible score!")
        else:
            print("Nice job, you won in {} turns.".format(
                self.state.turns), end=' ')
            print("You can improve by {}, if you try your best :)".format(
                self.state.turns - self.optimal_turns()
            ))

if __name__ == '__main__':
    import sys
    try:
        game = Game(int(sys.argv[1]))
    except:
        print("must pass 1 arg, int")

    print(game.state)
    while not game.complete():
        game.get_move()
    # the game is finished
    game.game_over()
