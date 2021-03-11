def cost(buildings, antennas, reward):
    total_reward = 0
    total_coverage = True
    for building in buildings: #building = (x, y, lat, vel)
        temp_reward = 0
        for antenna in antennas: # antenna = (x, y, dist, vel)
            if ((abs(building[0]-antenna[0]) + (abs(building[1]-antenna[1]))) <= antenna[2]):
                rewardino = buildings[3] * antenna[3] - buildings[2] * antenna[2]
                if rewardino > temp_reward or temp_reward == 0:
                    temp_reward = rewardino
        if temp_reward == 0:
            total_coverage = False
        else:
            total_reward += temp_reward
    if total_coverage:
        total_reward += reward
    return total_reward


def move_antenna(grid, x, y, d):
    if x - 2*d < 0:
        x1 = 0
    else:
        x1 = x -2 * d
    if x + 2 * d >= grid.shape[0]:
        x2 = grid.shape[0]
    else:
        x2 = x + 2 * d
    if y - 2*d < 0:
        y1 = 0
    else:
        y1 = y -2 * d
    if y + 2 * d >= grid.shape[0]:
        y2 = grid.shape[0]
    else:
        y2 = y + 2 * d
    cord = []
    for indexr, r in enumerate(grid[x1:x2]):
        for indexc, c in enumerate(r[y1:y2]):
            if c[0] != -1 and c[1] == -1:
                cord.append((indexr, indexc))
    finalx = 0
    finaly = 0
    for build in cord:
        finalx += build[0] - x
        finaly += build[1] - y
    finalx = x + finalx / len(cord)
    finaly = y + finaly / len(cord)

    return finalx, finaly