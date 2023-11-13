import numpy as np

class Map:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.zeros((self.row, self.col))
        self.world_len = len(self.map)


    def canyon(self, param, *argv):
        if (len(argv == 4)):
            self.map[argv[0] : argv[1], argv[2] : argv [3]] = param
        else:
            raise Exception("Too much or less arguments")
    

    def bridge(self, param, *argv):
        if (len(argv == 4)):
            self.map[argv[0] : argv[1], argv[2] : argv [3]] = param
        else:
            raise Exception("Too much or less arguments")


    def river(self, dir, param, *argv):
        if (len(argv == 2)):
            if (dir == 0):
                if ( 0 <= argv[0] < self.world_len) and (0 <= argv[1] < self.world_len):
                    self.map[argv[0] : argv[0] + 1, argv[1] : argv [1] + 1] = param
                elif (argv[0] <= self.world_len) and (argv[1] <= self.world_len):
                    self.map[argv[0] : argv[0] - 1, argv[1] : argv [1] - 1] = param
                else:
                    raise Exception("Range error in map")
            elif (dir == 1):
                pass
        else:
            raise Exception("Too much or less arguments")



