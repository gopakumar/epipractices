from test_framework import generic_test

from collections import namedtuple

Node = namedtuple('Node',('x','y'))

class graph():
    def __init__(self):
        self.result = None
    def dfs(self,board):
        boundrypath = dict()
        visited = dict()
        for cell in self.getboundrycells(board):
            boundrypath [cell] = True
            #print(cell)
            self.dfsutils(board,boundrypath,cell)
        #print(boundrypath)
        row = len(board)
        col = len(board[0])
        for r in range(row):
            for c in range(col):
                node = Node(x=r,y=c)
                if(board[r][c] == 'W' and (node not in boundrypath)):
                    board[r][c] = 'B'

    def dfsutils(self,board,boundrypath,cell):
        boundrypath[cell] = True
        for adj in self.getlistofadjs(board,cell):
            if(adj not in boundrypath) and (board[adj.x][adj.y] == 'W'):
                self.dfsutils(board,boundrypath,adj)
        


    def getlistofadjs(self,maze,node):
        #print(node)
        adjnodes = list()
        adj = Node(x= node.x-1,y=node.y)
        if(path_element_is_feasible(maze,node,adj)):
           adjnodes.append(adj)
        adj = Node(x= node.x+1,y=node.y)
        if(path_element_is_feasible(maze,node,adj)):
           adjnodes.append(adj)
        adj = Node(x= node.x,y=node.y+1)
        if(path_element_is_feasible(maze,node,adj)):
           adjnodes.append(adj)
        adj = Node(x= node.x,y=node.y-1)
        if(path_element_is_feasible(maze,node,adj)):
           adjnodes.append(adj)
        #print(adjnodes)
        return adjnodes

    def getboundrycells(self,board):
        row = len(board)
        col = len(board[0])
        #print(row,col)
        boundrycells = list()
        for r in range(row):
            for c in range(col):
                if ((r==0 or r== row-1 or c == 0 or c== col-1) and (board[r][c] == 'W')):
                    boundrycells.append(Node(x=r,y=c))
        #print(boundrycells)
        return(boundrycells)
        
        
def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == 'W'):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)

                
def fill_surrounded_regions(board):
    # TODO - you fill in here.

    #print ('*********')
    #for x in range(len(board)):
        #print(board[x])
    
    #print('***********')
    g= graph()
    g.dfs(board)

    #for x in range(len(board)):
        #print(board[x])
    
    #print('***********')
    
    return board


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board

                                

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
