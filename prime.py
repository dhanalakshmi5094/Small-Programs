# -*- coding:
def num_frequency_grid(x, y, v) :
    '''    x = int(input("Please enter the width of the grid"))
    y = int(input("Please enter the width of the grid"))
    v = int(input("Please enter the value to be counted"))
    '''
    new_grid = []
    count = 0
    for i in range(0, x) :
        for j in range(0, y) :
            new_grid.append(i + (j * j))

    for i in range(0, len(new_grid)) :
            if new_grid[i] == v :
                count += 1
                continue
            else :
                continue
    return count


print(num_frequency_grid(1024, 1024, 83))

