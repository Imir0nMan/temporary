import numpy as np


def filler(arr, param, *argv):
	if len(argv) == 4:
            row_a, row_z, col_a, col_z = argv
            arr[row_a : row_z, col_a : col_z] = param
        else:
            raise Exception("Too much or less arguments")


class Map:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.map = np.zeros((self.row, self.col))
        self.w_len = len(self.map)

	#ATTENTION
    #one side of the canyon have to be touch in one side of "walls" of array
    def canyon(self, param, *argv):
   		filler(self.map, param, *argv)


	#ATTENTION
	#one side of the river have to be touch in one side of "walls" of array
    def river(self, drct, param, *argv):
        if len(argv == 2) and drct == 0:
			row, col = argv
        	if 0 <= row < self.w_len and 0 <= col < self.w_len:
            	self.map[row : row=1, col: col+1] = param
            elif row <= self.w_len and col <= self.w_len:
            	self.map[row : row-1, col : col-1] = param
            else:
            	raise Exception("Range error in map")

        elif len(argv) == 4 and drct == 1:
			row_a, row_z, col_a, col_z = argv		 
			np.fill_diagonal(self.map[row_a : row_z, col_a : col_z], param)
			np.fill_diagonal(self.map[row_a+1 : row_z, col_a : col_z], param)
        else:
            raise Exception("Too much or less arguments")


	def quicksand(self, param, *argv):
		filler(self.map, param, *argv)


	def KKK(self, param, *argv):
		filler(self.map, param, *argv)
   	
	#ATTENTION
    #one side of the ocean have to be touch in one side of "walls" of array
    def ocean(self, param, *argv):
		filler(self.map, param, *argv)


	def trees(self, param):
		rows = self.row
		cols = self.col
		# Function to check if adding a param violates the condition
    	def is_valid_position(row, col):
        	neighbors =[(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        	for r, c in neighbors:
            	if 0 <= r < rows and 0 <= c < cols and self.map[r, c] == param:
                	return False
        	return True

    	# Place param in the matrix
    	for _ in range(rows * cols // 2):
        	while True:
            	row, col = np.random.randint(0,rows), np.random.randint(0,cols)
            	if self.map[row, col] == 0 and is_valid_position(row, col):
                	self.map[row, col] = param
                	break

	
    def highway(self, param, *argv):
		filler(self.map, param, *argv)


	def hill(self, param, *argv):
		filler(self.map, param, *argv)
