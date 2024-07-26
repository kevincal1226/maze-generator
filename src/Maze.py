# %%
import matplotlib.pyplot as plt
import numpy as np
import math
from icecream import ic
import random

NUM_ROWS = 7
NUM_COLS = 7
NUM_NODES = NUM_ROWS * NUM_COLS

def get_index_from_row_col(row, col) -> int:
    if row < 0 or col < 0 or row >= NUM_ROWS or col >= NUM_COLS:
        raise Exception(f"Invalid row or column index. row = {row}, col = {col}")
    return row * NUM_ROWS + col

class Maze:
    def __init__(self, use_dfs=True):
        self.__adjmat = np.zeros((NUM_NODES, NUM_NODES), np.int8)
        if use_dfs:
            self.root = random.randint(0, NUM_NODES - 1)            
            self.__create_dfs_maze()
        else:
            self.root = 0            
            self.__create_perfect_maze()
            
    # creates a root-directed maze
    def __create_dfs_maze(self):
        
        pass
    
    # applies origin shift and changes the root
    def __origin_shift(self):
        pass
    
    def origin_shift_n_times(self, n):
        if n < 0:
            raise Exception(f"Invalid n value. N must be >= 0. n = {n}")

        for _ in range(n):
            self.__origin_shift()
        
    # creates a simple perfect maze to origin shift on
    def __create_perfect_maze(self):
        for i in range(1, NUM_NODES):
            if i % NUM_COLS == 0:
                self.__adjmat[i][i - NUM_COLS] = 1
            else:
                self.__adjmat[i][i - 1] = 1
        
    def print_maze(self):
        _, p = plt.subplots(figsize=(NUM_COLS, NUM_ROWS))
        # for i in range(0, ROW_SIZE + 1):
        #     p.plot([i, i], [0, COL_SIZE], color='blue', linewidth=1)
        # for j in range(0, COL_SIZE + 1):
        #     p.plot([0, ROW_SIZE], [j, j], color='blue', linewidth=1)
        p.plot([0, NUM_COLS], [0, 0], color='purple', linewidth=1)
        p.plot([NUM_COLS, NUM_COLS], [0, NUM_ROWS], color='black', linewidth=1)
        for i in range(0, NUM_NODES):
            # creating vertical lines to the left of the index
            if i % NUM_COLS == 0:
                starting_y = math.floor(i / NUM_COLS)
                p.plot([0, 0], [starting_y, starting_y + 1], color='pink', linewidth=1)
            elif self.__adjmat[i][i - 1] == 0 and self.__adjmat[i - 1][i] == 0:
                starting_x = i % NUM_COLS
                starting_y = math.floor(i / NUM_COLS)
                p.plot([starting_x, starting_x], [starting_y, starting_y + 1], color='green', linewidth=1)
            
            # creating horizontal lines above the index
            if i >= NUM_NODES - NUM_COLS:
                starting_x = i % NUM_COLS
                p.plot([starting_x, starting_x + 1], [NUM_ROWS, NUM_ROWS], color='blue', linewidth=1)
            elif self.__adjmat[i][i + NUM_COLS] == 0 and self.__adjmat[i + NUM_COLS][i] == 0:
                starting_x = i % NUM_COLS
                starting_y = math.floor(i / NUM_COLS) + 1
                p.plot([starting_x, starting_x + 1], [starting_y, starting_y], color='red', linewidth=1)
        p.set_xticks([])
        p.set_yticks([])
        plt.show()
        
# %%
m = Maze(False)
m.print_maze()
# %%
