#include "Graph.hpp"
#include <vector>

class Maze {
  public:
    Maze();
    void generateMazeFromOriginShift();
    void printMaze() const;
    void originShiftNTimes(int n);

  private:
    void applyOriginShift();
    [[nodiscard]] int getIndexFromRowCol(int row, int col) const;
    Graph graph;
    bool initiallyGenerated = false;
};