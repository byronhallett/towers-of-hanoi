import towers
from time import sleep, time

def run_bot(game, delay=0):
    # solve here
    solution = recursive_solve(game.state.disc_count-1,
                               game.state.left,
                               game.state.right,
                               game.state.middle,
                               game.state,
                               delay)

def recursive_solve(disk, source, dest, spare, state, delay):
    if disk == 0:
        sleep(delay)
        state.move_disc(source, dest, quiet=(delay == 0))
    else:
        recursive_solve(disk - 1, source, spare, dest, state, delay)
        sleep(delay)
        state.move_disc(source, dest, quiet=(delay == 0))
        recursive_solve(disk - 1, spare, dest, source, state, delay)



if __name__ == '__main__':
    import sys
    try:
        disc_count = int(sys.argv[1])
        delay = float(sys.argv[2])
    except:
        sys.exit("must supply two args: disc_count (int), delay (float)")
    game = towers.Game(disc_count)
    print(game.state)
    pre = time()
    run_bot(game, delay)
    post = time()
    # game state is now solved
    if (delay == 0):
        print(game.state)
    print("Solved in {} moves".format(game.state.turns))
    print("theoretical optimum: {}".format(game.optimal_turns()))
    print("Time taken: {} seconds".format(post - pre))
