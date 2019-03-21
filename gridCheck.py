import gridTests
import gridGen


grid_rows = int(input('How many Rows?      '))
grid_cols = int(input('How many Columns?   '))
grid = gridGen.grid_gen(grid_rows, grid_cols)

print('\n\n')

for i in grid:
    for j in i:
        print(str(j) + " ", end="")
    print()

print('\n\n\n')

longest = 1

for i in range(grid_rows):
    for j in range(grid_cols):
        if grid[i][j] == 1:
            block, loc, direc = gridTests.test(i,j, grid)
            if block > longest:
                longest = block
                coord = loc
                direction = direc
print('\n\nThe longest chain of 1s is {0} long at index {1} in the {2} direction'.format(longest, coord, direction))