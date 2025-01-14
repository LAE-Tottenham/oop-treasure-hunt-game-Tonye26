from place import Place
from player import Player
from item import Item
from enemy import enemy
import random
class Game():
    def __init__(self, size=5):
        self.size = size
        self.grid = [['#' for _ in range(size)] for _ in range(size)]  # Initialize the grid with walls
        self.player_position = (0, 0)  # Start at the top-left corner
        self.treasure_position = None
        self.generate_maze()
        self.place_treasure()
        self.current_place = None

    def generate_maze(self):
        # Start carving paths from the top-left corner
        self.carve_path(0, 0)

    def carve_path(self, x, y):
        # Directions for moving in the maze (down, up, right, left)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        random.shuffle(directions)  # Randomize directions to create a maze

        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2  # Move two steps in the chosen direction
            if 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] == '#':
                self.grid[x + dx][y + dy] = ' '  # Carve a path
                self.grid[nx][ny] = ' '  # Carve a path
                self.carve_path(nx, ny)  # Recursively carve from the new position

    def place_treasure(self):
        # Find a random position for the treasure that is not a wall
        while True:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            if self.grid[x][y] == ' ' and (x, y) != self.player_position:
                self.grid[x][y] = 'T'  # Mark the treasure on the grid
                self.treasure_position = (x, y)
                break

    def move_player(self, direction):
        x, y = self.player_position
        if direction == 'up':
            new_position = (x - 1, y)
        elif direction == 'down':
            new_position = (x + 1, y)
        elif direction == 'left':
            new_position = (x, y - 1)
        elif direction == 'right':
            new_position = (x, y + 1)
        else:
            print("Invalid move! Use 'up', 'down', 'left', or 'right'.")
            return

        # Check if the new position is within bounds and not a wall
        if (0 <= new_position[0] < self.size and
                0 <= new_position[1] < self.size and
                self.grid[new_position[0]][new_position[1]] != '#'):
            self.player_position = new_position
            self.check_treasure()
        else:
            print("Invalid move! You hit a wall or the boundary.")

    def check_treasure(self):
        if self.player_position == self.treasure_position:
            print("Congratulations! You've found the treasure!")
            self.display_grid()
            exit()
        else:
            print("Keep searching!")

    def display_grid(self):
        # Print top border
        print('+' + '-' * self.size + '+')
        for i in range(self.size):
            print('|', end=' ')
            for j in range(self.size):
                if (i, j) == self.player_position:
                    print('P', end=' ')
                else:
                    print(self.grid[i][j], end=' ')
            print('|')  # End of row
        # Print bottom border
        print('+' + '-' * self.size + '+')
        print()

    def play(self):
        print("Welcome to the Treasure Hunt Game!")
        print("You can move using 'up', 'down', 'left', 'right'. Type 'exit' to quit.")
        while True:
            self.display_grid()
            move = input("Enter your move: ").strip().lower()
            if move == 'exit':
                print("Thanks for playing!")
                break
            self.move_player(move) 

    def setup(self):
        # here you will setup your Game
        # places
        home = Place('Home', 10)
        bedroom = Place('Bedroom', 5)
        bathroom = Place('Bathroom', 4, True) # bathroom is locked
        garden = Place('Garden', 15)
        shed = Place('Shed', 3)
        cave = Place('Cave', 50)
        
        home.add_next_place(garden)
        home.add_next_place(bedroom)
        bedroom.add_next_place(bathroom)
        garden.add_next_place(shed)
        # etc. 
        
        # items
        hammer = Item('Hammer',"Tool")
        pen = Item('Pen',"Tool")

        home.add_item(hammer)
        bedroom.add_item(pen)

        # home will be our starting place
        self.current_place = home
        
        # finish the setup function...

    def start(self):
        print("Welcome to my game...")
        print("Storyline...")
        print("You can move using 'up', 'down', 'left', 'right'. Type 'exit' to quit.")
        name = input("Enter player name: ")
        player = Player(name)

        print("You are currently in " + self.current_place.name)
        self.current_place.show_next_places()
        opt = input("""
What would you like to do?
1. Go to a place
2. Pickup item
3. Check inventory
etc.      
""")
        while True:
            self.display_grid()
            move = input("Enter your move: ").strip().lower()
            if move == 'exit':
                print("Thanks for playing!")
                break
            self.move_player(move) 
        
        if opt == "1":
            choice=input("Where would you like to go?")
            if choice=="Garden":
                self.current_place="Garden"
            elif choice=="Bedroom":
                self.current_place="Bedroom"
            pass
        elif opt == "2":
            
            pass
        elif opt == "3":
            print(Player.inventory)
            pass
            
game=Game(size=11)
game.setup()
game.start()
game.play()