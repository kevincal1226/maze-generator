#include <vector>

constexpr int ROW_SIZE = 5;
constexpr int COL_SIZE = 5;
constexpr int NUM_NODES = ROW_SIZE * COL_SIZE;

class Graph {
  public:
    Graph();
    [[nodiscard]] int get(int i, int j) const;
    int &get(int i, int j);

  private:
    std::vector<std::vector<int>> graphMatrix;
};