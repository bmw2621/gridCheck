def test(i, j, grid):
    diag = test_diag(i, j, grid)
    down = test_down(i, j, grid)
    right = test_right(i, j, grid)

    if max([diag, down, right]) == diag:
        direc = 'Diaganol'
    if max([diag, down, right]) == down:
        direc = 'Down'
    if max([diag, down, right]) == right:
        direc = 'Right'

    return max([diag, down, right]), [i,j], direc

def test_diag(i, j, grid):
    try:
        if grid[i + 1][j + 1] == 1:
            return 1 + test_up((i + 1), (j + 1), grid)
        else:
            return 1
    except:
        return 1


def test_down(i, j, grid):
    try:
        if grid[i + 1][j] == 1:
            return 1 + test_down((i + 1), j, grid)
        else:
            return 1
    except:
        return 1


def test_right(i, j, grid):
    try:
        if grid[i][j + 1] == 1:
            return 1 + test_right(i, (j + 1), grid)
        else:
            return 1
    except:
        return 1
