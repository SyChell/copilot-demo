# We have following number of swags that need to be distributed to students:
# 1. 25 Tumblers
# 2. 3 small size shirt
# 3. 10 medium size shirt
# 4. 5 large size shirt
# 5. 20 bag packs
# 
# Need to have a N x M matrix where N is number of rows and M is number of columns. In each cell, the following needs to be satisfied:
# 1. Each cell is represented as a locker
# 2. Each locker needs to have a locker code that is randomly generated integers and has length 4
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
    # Generate 5 random digits
    digits = ''.join(random.choices(string.digits, k=5))
    # Randomly choose between '*' and '#'
    special_char = random.choice(['*', '#'])
    # Combine the digits and the special character
    locker_code = digits + special_char
    # Randomly shuffle the characters in the locker code
    locker_code = ''.join(random.sample(locker_code, len(locker_code)))
    return locker_code

# Function to generate locker matrix
def generate_locker_matrix(n, m):
    # Initialize locker matrix
    locker_matrix = [[None for _ in range(m)] for _ in range(n)]
    # Initialize number of swags
    num_tumblers = 25
    num_small_shirts = 3
    num_medium_shirts = 10
    num_large_shirts = 5
    num_bag_packs = 20
    # Iterate through each cell in locker matrix
    for i in range(n):
        for j in range(m):
            # Generate locker code
            locker_code = generate_locker_code()
            # Initialize bundle
            bundle = []
            # Check if locker position is not N = 2, M = 3 and N = 2, M = 1
            if (i != 2 or j != 3) and (i != 2 or j != 1):
                # Check if there are available tumblers
                if num_tumblers > 0:
                    # Add tumbler to bundle
                    bundle.append('tumbler')
                    num_tumblers -= 1
                # Check if there are available small shirts
                if num_small_shirts > 0:
                    # Add small shirt to bundle
                    bundle.append('small shirt')
                    num_small_shirts -= 1
                # Check if there are available medium shirts
                elif num_medium_shirts > 0:
                    # Add medium shirt to bundle
                    bundle.append('medium shirt')
                    num_medium_shirts -= 1
                # Check if there are available large shirts
                elif num_large_shirts > 0:
                    # Add large shirt to bundle
                    bundle.append('large shirt')
                    num_large_shirts -= 1
                # Check if there are available bag packs
                if num_bag_packs > 0:
                    # Add bag pack to bundle
                    bundle.append('bag pack')
                    num_bag_packs -= 1
            # Assign bundle to locker matrix
            locker_matrix[i][j] = (locker_code, bundle)
    return locker_matrix


class TestLockerCode(unittest.TestCase):
    def test_generate_locker_code_length(self):
        code = generate_locker_code()
        self.assertEqual(len(code), 6)

    def test_generate_locker_code_digits(self):
        code = generate_locker_code()
        digit_count = sum(c.isdigit() for c in code)
        self.assertEqual(digit_count, 5)

    def test_generate_locker_code_special_char(self):
        code = generate_locker_code()
        special_chars = [c for c in code if c in ['*', '#']]
        self.assertEqual(len(special_chars), 1)

    def test_generate_locker_code_contains_only_valid_chars(self):
        code = generate_locker_code()
        for c in code:
            self.assertTrue(c in string.digits or c in ['*', '#'])

if __name__ == '__main__':
    unittest.main()