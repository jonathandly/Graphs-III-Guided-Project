"""
Write a function that takes a 2D binary array and returns
the number of 1 islands.
An island consists of 1's that are connected to the north,
south, east, or west. For example:

islands = [[0,1,0,1,0],
           [1,1,0,1,1],
           [0,0,1,0,0],
           [1,0,1,0,0],
           [1,1,0,0,0]]

island_counter(islands) # returns 4
"""

def island_counter(matrix):
    # keep track of visited vertices

    # go through the matrix of island data
    # if we see a 1, and it's not visited
        # do a DFT / BFT
            # keep marking each visited vertex as visited
        # once DFT is done, add 1 to our island count
    pass


islands = [[0,1,0,1,0],
           [1,1,0,1,1],
           [0,0,1,0,0],
           [1,0,1,0,0],
           [1,1,0,0,0]]

print(island_counter(islands))