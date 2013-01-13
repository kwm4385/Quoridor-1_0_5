"""
Quoridor II: Student Computer Engine

A sample class you may use to hold your state data
Author: Adam Oest (amo9149@rit.edu)

Author: Kevin Moses
"""

import itertools

class EngineData(object):
    
    __slots__ = ('logger', 'config', 'model', 'cells', 'walls')
    
    def __init__(self, logger, config, model):
        """
            Constructs and returns an instance of EngineData
        """
        
        self.logger = logger
        self.config = config
        self.model = model
        self.walls = []
        
        self.cells = []
        for r in range(9):
            self.cells.append([])
            for c in range(9):
                self.cells[r].append(Cell(r, c))
        for r in range(9):
            for c in range(9):
                if r - 1 >= 0:
                    self.cells[r][c].addNeighbor(Cell.NORTH, self.cells[r-1][c])
                if r + 1 < 9:
                    self.cells[r][c].addNeighbor(Cell.SOUTH, self.cells[r+1][c])
                if c - 1 >= 0:
                    self.cells[r][c].addNeighbor(Cell.WEST, self.cells[r][c-1])
                if c + 1 < 9:
                    self.cells[r][c].addNeighbor(Cell.EAST, self.cells[r][c+1])
        
    def __str__(self):
        """
        __str__: EngineData -> string
        Returns a string representation of the EngineData object.
            self - the EngineData object
        """
        result = "EngineData= " \
                    + "logger: " + str(self.logger) \
                    + ", config: " + str(self.config) \
                    + ", model: " + str(self.model)
                
        return result
    
    def addWall(self, wall):
        """
        Adds a wall to the board and updates the neighbors of surrounding cells and necessary.
        :param wall: The wall to add containing start and end coordinates.
        :type wall: Wall
        """
        if wall.start[0] == wall.end[0]:
            #Horizontal wall
            self.cells[wall.start[0]][wall.start[1]].removeNeighbor(Cell.NORTH)
            self.cells[wall.end[0]][wall.end[1] + (-1 if wall.end[1] > wall.start[1] else 1)].removeNeighbor(Cell.NORTH)
            
            self.cells[wall.start[0] - 1][wall.start[1]].removeNeighbor(Cell.SOUTH)
            self.cells[wall.end[0] - 1][wall.end[1] + (-1 if wall.end[1] > wall.start[1] else 1)].removeNeighbor(Cell.SOUTH)
        else:
            #Vertical wall
            self.cells[wall.start[0]][wall.start[1]].removeNeighbor(Cell.WEST)
            self.cells[wall.end[0] + (-1 if wall.end[0] > wall.start[0] else 1)][wall.end[1]].removeNeighbor(Cell.WEST)
            
            self.cells[wall.start[0]][wall.start[1] - 1].removeNeighbor(Cell.EAST)
            self.cells[wall.end[0]  + (-1 if wall.end[0] > wall.start[0] else 1)][wall.end[1] - 1].removeNeighbor(Cell.EAST)
    
class Cell(object):
    
    (NORTH, SOUTH, EAST, WEST) = range(4)
    
    __slots__ = ('r', 'c', 'neighbors')
    
    def __init__(self, r, c):
        """
        Constructs and returns an instance of Cell.
        :param r: The row coordinate
        :type r: Integer
        :param c: The column coordinate
        :type c: Integer
        """
        self.neighbors = {Cell.NORTH:None, Cell.SOUTH:None, Cell.EAST:None, Cell.WEST:None}
        self.r = r
        self.c = c
        
    def __str__(self):
        """
            Returns a string representation of the cell.
        """
        return self.__class__.__name__ + ' with ' + \
            str(len([x for x in self.neighbors.values() if x != None])) + \
            ' neighbors'
    
    def __repr__(self):
        """
            Returns a string representation of the cell.
        """
        return self.__str__()
    
    def addNeighbor(self, direction, cell):
        """
        Adds a neighbor to the cell.
        :param direction: The direction relative to the cell to the neighbor (0-3).
        :type direction: Integer
        :param cell: The cell to add as a neighbor.
        :type cell: Cell
        """
        if not isinstance(cell, Cell):
            raise TypeError('Neighbor must be of type Cell.')
        if direction in range(4):
            self.neighbors[direction] = cell
        else:
            raise ValueError('Invalid direction.')
        
    def removeNeighbor(self, direction):
        """
        Removes a neighbor from the cell.
        :param direction: The direction relative to the cell to the neighbor (0-3).
        :type direction: Integer
        """
        if direction in range(4):
            self.neighbors[direction] = None
        else:
            raise ValueError('Invalid direction.')
    
    def getNeighbor(self, direction):
        """
        Gets a neighbor of the cell.
        :param direction: The direction relative to the cell to the neighbor (0-3).
        :type direction: Integer
        """       
        if direction in range(4):
            return self.neighbors[direction]
        else:
            raise ValueError('Invalid direction.')
        
    def getAllNeighbors(self):
        """
            Returns a list of all cells that are neighbors to this.
        """
        return [x for x in self.neighbors.values() if x != None]
                
class Wall(object):
    
    __slots__ = ('start', 'end')
    
    def __init__(self, start, end):
        """
        Constructs and returns and instance of Wall.
        :param start: The start coordinate of the wall. [r, c]
        :type start: List
        :param end:The ending coordinate of the wall. [r, c]
        :type end: List
        """
        self.start = start
        self.end = end
        
    def __str__(self):
        """
            Returns a string representation of the wall.
        """
        return self.__class__.__name__ + ' from ' + str(self.start) + ' to ' + str(self.end)
    
    def __repr__(self):
        """
            Returns a string representation of the wall.
        """
        return self.__str__()
      
      
#====================================================================================
# Tests
#====================================================================================

if __name__ == "__main__":
    data = EngineData(None, None, None)
    print(len(data.cells[0][8].getAllNeighbors()))
    print([len(n.getAllNeighbors()) for n in itertools.chain(*data.cells)])
    print([(c.r, c.c) for c in data.cells[5][2].getAllNeighbors()])
            