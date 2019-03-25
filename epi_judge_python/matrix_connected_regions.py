from test_framework import generic_test
from collections import namedtuple

import pdb
Coordinate = namedtuple('Coordinate',('x','y'))

class graph():
    def __init__ (self):
        self.result = None
        self.x = 0
        self.y = 0
        self.color =0 
    def dfs (self,maze):
       
        start = Coordinate(x=self.x,y=self.y)
        self.dfsutils(maze,start)

    def dfsutils(self,maze,node):

        maze[node.x][node.y] = int(not(self.color))
        #print(node.x,node.y)
        #print(maze)

        for adj in self.getadjlist(maze,node):
            if( maze[adj.x][adj.y] == self.color):
                self.dfsutils(maze,adj)

    def getadjlist(self,maze,node):
        #print(node)
        adjnodes = list()
        adj = Coordinate(x= node.x-1,y=node.y)
        if(path_element_is_feasible(maze,node,adj)):
           adjnodes.append(adj)
        adj = Coordinate(x= node.x+1,y=node.y)
        if(path_element_is_feasible(maze,node,adj)):
           adjnodes.append(adj)
        adj = Coordinate(x= node.x,y=node.y+1)
        if(path_element_is_feasible(maze,node,adj)):
           adjnodes.append(adj)
        adj = Coordinate(x= node.x,y=node.y-1)
        if(path_element_is_feasible(maze,node,adj)):
           adjnodes.append(adj)
        #print(adjnodes)
        return adjnodes


        
        
def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x]))):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)

def flip_color(x, y, image):
    # TODO - you fill in here.
    g = graph()
    #pdb.set_trace()
    g.x= x
    g.y = y
    g.color = image[x][y]
    g.dfs(image)
    #print(image)
    return image


def flip_color_wrapper(x, y, image):
    flip_color(x, y, image)
    return image


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_connected_regions.py",
                                       'painting.tsv', flip_color_wrapper))
