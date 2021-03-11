# %%
import numpy as np


# %%
def read(filename):
    with open(filename, "r", encoding="ascii") as f:
        grid_size = list(map(int, f.readline().split(" ")))
        bar = list(map(int, f.readline().split(" ")))
        buildings = []
        antennas = []
        for i in range(0, bar[0]):
            buildings.append(list(map(int, f.readline().split(" "))))
        for i in range(0, bar[1]):
            antennas.append(list(map(int, f.readline().split(" "))))
        return grid_size, bar, buildings, antennas


grid_size, bar, buildings, antennas = read("../input/data_scenarios_a_example.in")

# %%
buildings = sorted(buildings, key=lambda element: element[3], reverse=True)
antennas = sorted(antennas, key=lambda element: element[1], reverse=True)

# %%
grid = np.chararray((grid_size[0], grid_size[1]))
grid[:] = '-'
for building in buildings:
    grid[building[0]][building[1]] = 'B'
print(grid)


# %%
def cost(buildings, antennas, reward):
    total_reward = 0
    total_coverage = True
    for building in buildings:  # building = (x, y, lat, vel)
        temp_reward = 0
        for antenna in antennas:  # antenna = (x, y, dist, vel)
            if (abs(building[0] - antenna[0]) + (abs(building[1] - antenna[1]))) <= antenna[2]:
                rewardino = building[3] * antenna[3] - building[2] * antenna[2]
                if rewardino > temp_reward or temp_reward == 0:
                    temp_reward = rewardino
        if temp_reward == 0:
            total_coverage = False
        else:
            total_reward += temp_reward
    if total_coverage:
        total_reward += reward
    return total_reward


# %%
for index, ant in enumerate(antennas):
    ant = [buildings[index][0], buildings[index][1], ant[0], ant[1]]
    antennas[index] = ant

reward = cost(buildings, antennas, bar[2])

#%%
def save(filename, antennas):
    with open(filename, "w", encoding="ascii") as f:
        f.write(f"{len(antennas)}")
        for antenna in antennas:
            f.write(f"\n{antenna[0]} {antenna[1]} {antenna[2]}")


save("../output/out1.out", antennas)
