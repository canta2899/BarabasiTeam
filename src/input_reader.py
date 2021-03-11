def read(filename):
    with open(filename, "r") as f:
        grid = list(map(int, f.readline().split(" ")))
        bar = list(map(int, f.readline().split(" ")))
        buildings = []
        antennas = []
        for i in range(0, bar[0]):
            buildings.append(list(map(int, f.readline().split(" "))))
        for i in range(0, bar[1]):
            antennas.append(list(map(int, f.readline().split(" "))))
        return grid, bar, buildings, antennas