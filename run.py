import argparse
from snake.game import Game, setup, GameMode
import time


dict_solver = {
    "hamilton": "HamiltonSolver",
    "greedy": "GreedySolver"
}

dict_mode = {
    "normal": GameMode.n,
}
solverChoice = input("Which solver would you like? Enter 'hamilton' for Hamilton or 'greedy' for Greedy. ")
parser = argparse.ArgumentParser(description="Run snake game agent.")
parser.add_argument("-s", default=solverChoice, choices=dict_solver.keys())
parser.add_argument("-m", default="normal", choices=dict_mode.keys())
args = parser.parse_args()


conf = setup()
conf.solver_name = dict_solver[args.s]
conf.mode = dict_mode[args.m]
print("Opening window....")

Game(conf).run()

