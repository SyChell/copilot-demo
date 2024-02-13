# We have following number of swags that need to be distributed to students:
# 1. 25 Tumblers
# 2. 3 small size shirt
# 3. 10 medium size shirt
# 4. 5 large size shirt
# 5. 20 backpacks
# 
# Need to have a N x M matrix where N is number of rows and M is number of columns. In each cell, the following needs to be satisfied:
# 1. Each cell is represented as a locker
# 2. Each locker needs to have a locker code that is randomly generated integers and has length 4 with minumum # or * characters
# 3. Each locker should try to have a bundle of swag items where each bundle should satisfy the following:
#   a. Each bundle should have 1 tumbler if possible as long as there are tumblers available
#   b. Each bundle should have 1 bag pack if possible as long as there are bag packs available
#   c. Each bundle should only have 1 shirt (does not matter if it is small, medium, or large) as long as there are available
# 4. Two lockers with position N = 2, M = 3 and position N = 2, M = 1 should be empty

import random
import string
import unittest

# Function to generate random locker code
def generate_locker_code():
    # Generate 3 random digits
    digits = ''.join(random.choices(string.digits, k=3))
    # Choose a random special character ('*' or '#')
    special_char = random.choice(['*', '#'])
    # Combine the digits and special character to form the locker code
    locker_code = digits + special_char
    # Randomly shuffle the characters in the locker code
    locker_code = ''.join(random.sample(locker_code, len(locker_code)))
    return locker_code

# Function to generate locker matrix
def generate_locker_matrix(n, m, swags):
    locker_matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            locker_code = generate_locker_code()
            bundle = []
            if (i, j) != (2, 3) and (i, j) != (2, 1):
                for item, count in swags.items():
                    if count > 0:
                        bundle.append(item)
                        swags[item] -= 1
            row.append((locker_code, bundle))
        locker_matrix.append(row)
    return locker_matrix

# Function to print locker matrix
def print_locker_matrix(locker_matrix):
    for i in range(len(locker_matrix)):
        for j in range(len(locker_matrix[i])):
            locker_code, bundle = locker_matrix[i][j]
            print(f"Locker {i+1},{j+1}: Code = {locker_code}, Bundle = {bundle}")

def main():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("Enter the number of columns: "))
    swags = {
        'tumbler': 25,
        'small_shirt': 3,
        'medium_shirt': 10,
        'large_shirt': 5,
        'backpack': 20
    }
    locker_matrix = generate_locker_matrix(rows, columns, swags)
    print_locker_matrix(locker_matrix)
    
    
class TestLockerCode(unittest.TestCase):
    def test_length(self):
        code = generate_locker_code()
        self.assertEqual(len(code), 4)

    def test_contains_digit(self):
        code = generate_locker_code()
        self.assertTrue(any(char.isdigit() for char in code))

    def test_contains_special_char(self):
        code = generate_locker_code()
        self.assertTrue(any(char in ['*', '#'] for char in code))


    
if __name__ == "__main__":
    main()
    unittest.main()

# Output:
# Enter the number of rows: 3   
# Enter the number of columns: 3
# ['tumbler', 'backpack', 'small_shirt'] ['tumbler', 'backpack', 'small_shirt'] ['tumbler', 'backpack', 'small_shirt']