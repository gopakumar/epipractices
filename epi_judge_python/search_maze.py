import collections
import copy
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

class graph:
    def __init__(self):
        self.result = False
        self.path = list()
        self.e = None
    def dfs(self,maze,s,e):
        path = [] #[None] * len(maze[0])*len(maze)
        visited = dict()
        visited[s] = 1
        path.append(s)
        for x in self.listofadjs(maze,s):
            self.dfsutils(maze,path,visited,x)

    def dfsutils(self,maze,path,visited,x):
        if(self.result == True): # we already got the result 
            return 
        visited[x] = 1
        path.append(x)
        #print(path)
        if (x == self.e):
            #print('**********')
            self.result = True
            self.path = list(path)
            #print(path)
            return
        for adjs in self.listofadjs(maze,x):
            if not (adjs in visited):
                #print(x,adjs)
                self.dfsutils(maze,path,visited,adjs)
        path.pop()
    def listofadjs(self,maze,node):
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


        
        
def search_maze(maze, s, e):
    # TODO - you fill in here.
    
    #print (maze)
    g= graph()
    g.e= e
    g.dfs(maze,s,e)
    #print (s)

    #print (len(maze[1]))
    #print(g.path)
    return  g.path


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))
