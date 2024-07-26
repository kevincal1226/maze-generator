from maze import Maze

m = Maze(num_rows=10, num_cols=10, use_dfs=False)
m.save_maze("original")
n = 1000
m.origin_shift_n_times(n)
m.save_maze("after-origin-shift")
m.save_adjmat_to_file("out.txt")