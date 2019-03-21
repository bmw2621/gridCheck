def grid_gen(grid_rows, grid_cols):
    from random import randint
    grid = []
    for row in range(grid_rows):
        row_data = []
        for _ in range(grid_cols):
            i = randint(0, 1)
            row_data.append(i)
        grid.append(row_data)

    return grid