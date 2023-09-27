#!/bin/python3

import random
import time

def get_neighbors(n, m, x, y):
    neighbors = []

    # Define relative coordinates for all possible neighbors, including diagonals
    relative_coords = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]

    for dx, dy in relative_coords:
        neighbor_x = x + dx
        neighbor_y = y + dy

        # Check if the neighbor is within the grid boundaries
        if 0 <= neighbor_x < n and 0 <= neighbor_y < m:
            neighbors.append([neighbor_x, neighbor_y])

    return neighbors

def spiral_iteration(n, m, start_x, start_y):
    total_pixels = n * m
    count = 0
    x, y = start_x, start_y

    yield x, y  # Yield the starting point

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    direction_index = 0  # Start with the first direction (right)
    steps_until_direction_change = 1  # Number of steps to take in the current direction

    steps_taken_in_direction = 0  # Counter for the steps taken in the current direction
    steps_in_current_direction = 1  # Number of steps to take in the current direction before changing direction

    while True:
        dx, dy = directions[direction_index]

        for _ in range(steps_in_current_direction):
            x += dx
            y += dy
            steps_taken_in_direction += 1

            if steps_taken_in_direction == steps_until_direction_change:
                direction_index = (direction_index + 1) % 4  # Change direction
                steps_taken_in_direction = 0  # Reset steps taken
                if direction_index % 2 == 0:  # Increase steps until direction change every 2 directions
                    steps_until_direction_change += 1
            
            
            
            if count == total_pixels - 1:
                return
            
            if 0 <= x < width and 0 <= y < height:
                yield x, y
                count += 1
            else:
                continue
        

def count_element(matrix, target_element):
    count = 0

    # Iterate through each row
    for row in matrix:
        # Iterate through each element in the row
        for element in row:
            if element == target_element:
                count += 1

    return count

class Biome_Base:
    def __init__(self, name, description):
        self.name = name                    # Biome name (e.g., "Forest")
        self.description = description      # Biome description (e.g., "Grassland", "Forest", "Desert")

    def __str__(self):
        return f"Biome: {self.name}\nTerrain: {self.terrain}\nVegetation: {self.vegetation}\nTemperature: {self.temperature}°C\nPrecipitation: {self.precipitation} mm/year"

class Mountain_Biome(Biome_Base):
    def __init__(self, mtn_density):
        super().__init__("Mountains", "A mountanous region")
        self.mtn_density = mtn_density

    def __str__(self):
        return super().__str__() + f"\nElevation: {self.elevation} meters"

    def generate_tile(self, width, height):
        total_tiles = height * width
        tile = [[' ' for _ in range(width)] for _ in range(height)]

        x, y = random.randint(0, width - 1), random.randint(0, height - 1)
        n = width
        m = height
        
        tile[y][x] = 'M'
        
        count = 0
        
        for x, y in spiral_iteration(width, height, x, y):
            count += 1
            if count != 1:
                neighbors = get_neighbors(width, height, x,y)
                neighboring = False
                for neighbor in neighbors:
                    if tile[neighbor[1]][neighbor[0]] == 'M':
                        neighboring = True
                        break                        
                
                prob = count_element(tile, 'M')/(height*width)
                    
                num = random.randint(0,100)
                
                if num < 100-(prob*100/self.mtn_density):
                    gen_mtn = True
                else:
                    gen_mtn = False
                    
                if neighboring and prob <= self.mtn_density and gen_mtn:
                    tile[y][x] = 'M'
                else:
                    tile[y][x] = '.'

        return tile

def print_tile(tile):
    for row in tile:
        print(''.join(row))
    print()

if __name__ == "__main__":
    width = 128
    height = 32

    mountains = Mountain_Biome(mtn_density=0.8)

    generated_tile = mountains.generate_tile(width, height)
    print_tile(generated_tile)
