# %%
import matplotlib.pyplot as plt
import numpy as np
import math
import random

class Maze:
    def __init__(self, num_rows, num_cols, use_dfs=True) -> None:
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__num_nodes = num_rows * num_cols
        self.__adjmat = np.zeros((self.__num_nodes, self.__num_nodes), dtype=bool)
        if use_dfs:
            self.__root = random.randint(0, self.__num_nodes - 1)            
            self.__create_dfs_maze()
        else:
            self.__root = 0            
            self.__create_perfect_maze()
    
    def __get_neighbors_of_index(self, index) -> list[int]:
        neighbors = []
        if index % self.__num_cols != 0:
            neighbors.append(index - 1)
        if (index + 1) % self.__num_cols != 0:
            neighbors.append(index + 1)
        if index >= self.__num_cols:
            neighbors.append(index - self.__num_cols)
        if index < self.__num_nodes - self.__num_cols:
            neighbors.append(index + self.__num_cols)
        
        return neighbors        
        
    def __dfs_helper(self, parent_index, discovered) -> None:
        neighbors = self.__get_neighbors_of_index(parent_index)
        random.shuffle(neighbors)
        # you can adjust this however you want to make more-less average connections per node
        num_to_connect = random.randint(1, 4)
        for node in neighbors:
            if num_to_connect == 0 or discovered[node]:
                continue
            
            num_to_connect -= 1
            discovered[node] = True
            self.__adjmat[node][parent_index] = True
            self.__dfs_helper(node, discovered)
                            
    # creates a root-directed maze
    def __create_dfs_maze(self) -> None:
        discovered = [False for _ in range(self.__num_nodes)]
        discovered[self.__root] = True
        self.__dfs_helper(self.__root, discovered)
    
    
    # applies origin shift and changes the root
    def __origin_shift(self) -> None:
        neighbors = self.__get_neighbors_of_index(self.__root)
        new_root = neighbors[random.randint(0, len(neighbors) - 1)]
        self.__adjmat[self.__root][new_root] = True
        self.__adjmat[new_root] = np.zeros((1, self.__num_nodes), dtype=bool)
        self.__root = new_root
        
            
    # creates a simple perfect maze to origin shift on
    def __create_perfect_maze(self) -> None:
        for i in range(1, self.__num_nodes):
            if i % self.__num_cols == 0:
                self.__adjmat[i][i - self.__num_cols] = True
            else:
                self.__adjmat[i][i - 1] = True
        
    def origin_shift_n_times(self, n=1) -> None:
        if n < 0:
            raise Exception(f"Invalid n value. N must be >= 0. n = {n}")

        for _ in range(n):
            self.__origin_shift()    
    
    def print_maze(self) -> None:
        _, p = plt.subplots(figsize=(math.sqrt(self.__num_cols), math.sqrt(self.__num_rows)))
        p.plot([0, self.__num_cols], [0, 0], color='blue', linewidth=1)
        p.plot([self.__num_cols, self.__num_cols], [0, self.__num_rows], color='blue', linewidth=1)
        for i in range(0, self.__num_nodes):
            # creating vertical lines to the left of the index
            if i % self.__num_cols == 0:
                starting_y = math.floor(i / self.__num_cols)
                p.plot([0, 0], [starting_y, starting_y + 1], color='blue', linewidth=1)
            elif not self.__adjmat[i][i - 1] and not self.__adjmat[i - 1][i]:
                starting_x = i % self.__num_cols
                starting_y = math.floor(i / self.__num_cols)
                p.plot([starting_x, starting_x], [starting_y, starting_y + 1], color='blue', linewidth=1)
            
            # creating horizontal lines above the index
            if i >= self.__num_nodes - self.__num_cols:
                starting_x = i % self.__num_cols
                p.plot([starting_x, starting_x + 1], [self.__num_rows, self.__num_rows], color='blue', linewidth=1)
            elif not self.__adjmat[i][i + self.__num_cols] and not self.__adjmat[i + self.__num_cols][i]:
                starting_x = i % self.__num_cols
                starting_y = math.floor(i / self.__num_cols) + 1
                p.plot([starting_x, starting_x + 1], [starting_y, starting_y], color='blue', linewidth=1)
        p.set_xticks([])
        p.set_yticks([])
        plt.show()
        
    def write_adjmat_to_file(self, filename) -> None:
        np.savetxt(filename, self.__adjmat, fmt="%i")
        with open(filename, "a+") as f:
            f.write(f"Root node: {self.__root}")        
        
        
# %%
m = Maze(num_rows=10, num_cols=10, use_dfs=False)
print("Original maze:")
m.print_maze()
n = 1000
m.origin_shift_n_times(n)
print(f"New maze after {n} origin shifts:")
m.print_maze()
m.write_adjmat_to_file("out.txt")
# %%
