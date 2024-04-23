# We have following number of swags that need to be distributed to employees:
# 1. 25 Tumblers
# 2. 3 small size shirt
# 3. 10 medium size shirt
# 4. 5 large size shirt
# 5. 20 backpacks
# 
# Need to have a N x M matrix where N is number of rows and M is number of columns. In each cell, the following needs to be satisfied:
# 1. Each cell is represented as a locker
# 2. Each locker needs to have a locker code that is randomly generated integers and has length 4 

import random
import numpy as np

def generate_locker_code():
    code = str(random.randint(1000, 9999))
    special_char = random.choice(['*', '#'])
    position = random.randint(0, len(code))
    return code[:position] + special_char + code[position:]

# Function to generate locker matrix
def generate_locker_matrix(rows, cols):
    locker_matrix = np.zeros((rows, cols))
    for i in range(rows):
        for j in range(cols):
            locker_matrix[i][j] = generate_locker_code()
    return locker_matrix

def distribute_swags():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    locker_matrix = generate_locker_matrix(rows, columns)
    print(locker_matrix)
    
distribute_swags()

