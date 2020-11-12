import argparse
from snake.game import Game, setup, GameMode

dict_solver = {
    "hamilton": "HamiltonSolver",
}

dict_mode = {
    "normal": GameMode.n,
}

parser = argparse.ArgumentParser(description="Run snake game agent.")
parser.add_argument("-s", default="hamilton", choices=dict_solver.keys(),
                    help="name of the solving to direct the snake (default: hamilton)")
parser.add_argument("-m", default="normal", choices=dict_mode.keys(),
                    help="game mode (default: normal)")
args = parser.parse_args()


conf = setup()
conf.solver_name = dict_solver[args.s]
conf.mode = dict_mode[args.m]
print("Opening window....")

Game(conf).run()
