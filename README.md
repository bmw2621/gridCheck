# Code Challenge Solution

_**Initial code challenge:**_

Enter a random non-negative integers and a program spits out a "grid" of ones (1) and zeroes (0), it is the coder's goal to write a program that can then calculate the size of the largest straight chain of ones in the grid. The grid is output as a list with each row being a separate list.

Problem is solved by iterating over each point, checking for presence of "1", if so calling a series of direcctional tests, and if an adjacent "1" is found recursively runs the check in the appropriate driection.

_**Additional features not required by the challenge:**_

* Solution searches for horizontal, vertical, and diaganol chains.
* Solution allows user to enter custom grid size, rather than producing a square grid from input
* Solution returns index, direction, and length (to aid with very large grids)


### Adding something new to teach how GIT works
### Adding comment for GIT understanding