#include "Maze.hpp"
#include <stdexcept>

Maze::Maze() = default;

void Maze::generateMazeFromOriginShift() { initiallyGenerated = true; }

void Maze::originShiftNTimes(int n) {
    if (n <= 0) {
        return;
    }
    int i = 0;
    if (!initiallyGenerated) {
        generateMazeFromOriginShift();
        printMaze();
        ++i;
    }
    for (; i < n; ++i) {
        applyOriginShift();
        printMaze();
    }
}

void Maze::printMaze() const {}

void Maze::applyOriginShift() {}

int Maze::getIndexFromRowCol(const int row, const int col) const {
    if (row < 0 || col < 0 || row >= ROW_SIZE || col >= COL_SIZE) {
        throw std::invalid_argument("Invalid row or column value");
    }
    return row * ROW_SIZE + col;
}