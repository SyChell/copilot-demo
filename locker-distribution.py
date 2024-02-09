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

import numpy as np
import random

N = int(input("Enter the number of rows: "))
M = int(input("Enter the number of columns: "))

large_shirt = 5
bag_packs = 20

# Locker distribution
locker_distribution = np.empty((N, M), dtype = object)
for i in range(N):
    for j in range(M):
        locker_distribution[i][j] = "Locker" + str(random.randint(1000, 9999))

# Locker distribution with swags
for i in range(N):
    for j in range(M):
        if (i == 1 and j == 2) or (i == 2 and j == 0):
            locker_distribution[i][j] = "Empty"
        else:
            locker_distribution[i][j] = locker_distribution[i][j] + " Tumbler" + str(random.randint(1000, 9999))
            locker_distribution[i][j] = locker_distribution[i][j] + " Shirt" + str(random.randint(1000, 9999))
            locker_distribution[i][j] = locker_distribution[i][j] + " BagPack" + str(random.randint(1000, 9999))

# Print the locker distribution
locker_number = 1
for i in range(N):
    for j in range(M):
        print(f"Locker {locker_number}: {locker_distribution[i][j]}")
        locker_number += 1
