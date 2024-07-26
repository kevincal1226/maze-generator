# %%
import matplotlib.pyplot as plt
import numpy as np

ROW_SIZE = 5
COL_SIZE = 5
NUM_NODES = ROW_SIZE * COL_SIZE

def get_index_from_row_col(row, col) -> int:
    if row < 0 or col < 0 or row >= ROW_SIZE or col >= COL_SIZE:
        raise Exception(f"Invalid row or column index. row = {row}, col = {col}")
    return row * ROW_SIZE + col

class Maze:
    def __init__(self):
        self.adjmat = np.zeros((NUM_NODES, NUM_NODES), np.int8)
        print(len(self.adjmat), len(self.adjmat[0]))
        print(self.adjmat)
        
    def print_maze(self):
        _, ax = plt.subplots(figsize=(COL_SIZE * 2, ROW_SIZE * 2))
        for i in range(0, ROW_SIZE + 1):
            ax.plot([i, i], [0, COL_SIZE], color='blue', linewidth=1)
        for j in range(0, COL_SIZE + 1):
            ax.plot([0, ROW_SIZE], [j, j], color='blue', linewidth=1)
        ax.set_xticks([])
        ax.set_yticks([])
        plt.show()
        
# %%
m = Maze()
m.print_maze()
# %%
