#include "Graph.hpp"

Graph::Graph() : graphMatrix(std::vector<std::vector<int>>(NUM_NODES, std::vector<int>(NUM_NODES, 0))) {}

int Graph::get(const int i, const int j) const { return graphMatrix[i][j]; }

int &Graph::get(const int i, const int j) { return graphMatrix[i][j]; }