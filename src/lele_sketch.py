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