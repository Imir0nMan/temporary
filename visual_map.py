import tkinter as tk

class ColorfulMatrixGame:
    def __init__(self, root, matrix, piece_size, obstacle_numbers):
        self.root = root
        self.root.title("Map")

        self.matrix = matrix
        self.matrix_size = len(matrix)
        self.piece_size = piece_size
        self.person_position = (self.matrix_size // 2, self.matrix_size // 2)  # Start in the middle of the matrix

        self.obstacle_numbers = obstacle_numbers
        self.colors = {}  # Dictionary to store the colors of each number
        self.revealed = set()  # Set to keep track of revealed numbers

        self.canvas = tk.Canvas(root, width=piece_size * 50, height=piece_size * 50)
        self.canvas.pack()

        self.init_color_map()
        self.draw_matrix()

        # Bind arrow key events to move the person
        root.bind("<Left>", self.move_left)
        root.bind("<Right>", self.move_right)
        root.bind("<Up>", self.move_up)
        root.bind("<Down>", self.move_down)


    def colors_mapping(self):
        color_map = {
            0: "lawngreen",
            1: "coral",
            2: "olive",
            3: "royalblue",
            4: "grey",
            5: "lime",
            6: "teal",
            7: "aqua",
            8: "sienna",
            9: "firebrick",
            10: "blue",
            11: "forestgreen",
            12: "darkgrey",
            13: "bisque",
            14: "chocolate"
        }
        return color_map
    def init_color_map(self):
        color_mapping = self.colors_mapping()
        for number, color in color_mapping.items():
            self.colors[number] = color
        """    
        unique_numbers = set(num for row in self.matrix for num in row)
        for number in unique_numbers:
            self.colors[number] = generate_random_color()
        """
    def draw_matrix(self):
        self.canvas.delete("all")  # Clear the canvas
        temp = 50
        current_piece_x, current_piece_y = self.person_position[0] // temp, self.person_position[1] // temp

        for i in range(current_piece_x * temp, min((current_piece_x + 1) * temp, self.matrix_size)):
            for j in range(current_piece_y * temp, min((current_piece_y + 1) * temp, self.matrix_size)):
                x1 = (i - current_piece_x * temp) * self.piece_size
                y1 = (j - current_piece_y * temp) * self.piece_size
                x2 = x1 + self.piece_size
                y2 = y1 + self.piece_size

                number = self.matrix[i][j]

                if (i, j) == self.person_position:
                    color = "white"  # Color for the person
                #elif number in self.obstacle_numbers:
                #    color = "red"  # Color for obstacles
                elif (i, j) in self.revealed:
                    color = self.colors[number]  # Use the revealed color
                else:
                    color = "black"  # Hide the color

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def move_person(self, dx, dy):
        x, y = self.person_position
        new_x, new_y = x + dx, y + dy

        # Check if the new position is within the matrix boundaries and not an obstacle
        if (
            0 <= new_x < self.matrix_size
            and 0 <= new_y < self.matrix_size
            and self.matrix[new_x][new_y] not in self.obstacle_numbers
        ):
            self.person_position = (new_x, new_y)
            #self.reveal_nearby_numbers(dx, dy)
            self.reveal_nearby_numbers()
            self.draw_matrix()

    def move_left(self, event):
        self.move_person(-1, 0)

    def move_right(self, event):
        self.move_person(1, 0)

    def move_up(self, event):
        self.move_person(0, -1)

    def move_down(self, event):
        self.move_person(0, 1)


    def reveal_nearby_numbers(self):
        x, y = self.person_position

        for i in range(x - 4, x + 5):
            for j in range(y - 4, y + 5):
                if 0 <= i < self.matrix_size and 0 <= j < self.matrix_size:
                    self.revealed.add((i, j))

