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
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_neighbors(current_vertex, matrix):
    neighbors = set()
    row = current_vertex[0]
    col = current_vertex[1]

    # check north direction
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.add((row-1, col))
    # check south direction
    if row < len(matrix) - 1 and matrix[row+1][col] == 1:
        neighbors.add((row+1, col))
    # check west / left direction
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.add((row, col-1))
    # check east / right direction
    if col < len(matrix[row]) - 1 and matrix[row][col+1] == 1:
        neighbors.add((row, col+1))

    return neighbors

def dft(row_index, col_index, matrix, visited_vertices):
    # traverse the "graph" starting at row_i and col_i
    if (row_index, col_index) in visited_vertices:
        return 

    neighbors_to_visit = Stack()
    neighbors_to_visit.push((row_index, col_index))

    while neighbors_to_visit.size() > 0:
        # pop the first vertex on stack off
        current_vertex = neighbors_to_visit.pop()
        # check if it hasn't been visited yet
        if current_vertex not in visited_vertices:
            # mark it as visited
            visited_vertices.add(current_vertex)
            # push all neighbors up to stack
            for neighbor in get_neighbors(current_vertex, matrix):
                neighbors_to_visit.push(neighbor)
    return visited_vertices

def island_counter(matrix):
    # keep track of visited vertices
    visited_vertices = set()
    island_count = 0
    # go through the matrix of island data
    for row_index in range(len(matrix)):
        for col_index in range(len(matrix[row_index])):
            # if we see a 1, and it's not visited
            if (row_index, col_index) not in visited_vertices and matrix[row_index][col_index] == 1:
                # do a DFT / BFT
                visited_vertices = dft(row_index, col_index, matrix, visited_vertices)
                # once DFT is done, add 1 to our island count
                island_count += 1
    return island_count


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))

islands = [[1, 0, 0, 1, 1, 0, 1, 1, 0, 1],
           [0, 0, 1, 1, 0, 1, 0, 0, 0, 0],
           [0, 1, 1, 1, 0, 0, 0, 1, 0, 1],
           [0, 0, 1, 0, 0, 1, 0, 0, 1, 1],
           [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
           [0, 1, 0, 1, 1, 1, 0, 1, 0, 0],
           [0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
           [1, 0, 1, 1, 0, 0, 0, 1, 1, 0],
           [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 1, 0, 0, 1, 0]]

print(island_counter(islands))