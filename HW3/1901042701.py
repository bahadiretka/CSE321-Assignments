from re import T
from collections import defaultdict
import queue

class Graph:
    def __init__(self):
        self.edges = {}
        self.vertices = 0
    def addEdge(self, sourceNode, dest_node):
        self.edges[sourceNode].append(dest_node)

    def topologicalBFS(self):
        val_of_indegree = self.countOfVertices() * [0]

        for source_node in self.edges:
            for dest_node in self.edges[source_node]:
                val_of_indegree[self.findIndexByKey(dest_node)] += 1

        queue = []

        for i in range(self.countOfVertices()):
            if val_of_indegree[i] == 0:
                queue.append(i)

        count = 0
        o = []

        while queue:
            u = queue.pop(0)
            o.append(self.findKeyByIndex(u))

            for source_node in self.edges[self.findKeyByIndex(u)]:
                val_of_indegree[self.findIndexByKey(source_node)] -= 1

                if val_of_indegree[self.findIndexByKey(source_node)] == 0:
                    queue.append(self.findIndexByKey(source_node))

            count += 1

        if count != self.countOfVertices():
            raise Exception("Please enter an acyclic graph!")

        return o

    def topologicalDFS(self):
        o = []

        for node in self.edges:
            if node not in o:
                o = self.depthFirstSearch(node, o)

        return o[::-1]

    def addNode(self, node):
        self.edges[node] = []

    def findIndexByKey(self, key):
        if key in self.edges.keys():
            return list(self.edges.keys()).index(key)

    def findKeyByIndex(self, index):
        return list(self.edges.keys())[index]

    def countOfVertices(self):
        return len(self.edges.keys())

    def getDestinationNodes(self, node):
        return self.edges[node]

    def depthFirstSearch(self, v, o):
        for node in self.getDestinationNodes(v):
            if node not in o:
                o = self.depthFirstSearch(node, o)
        if v not in o:
            o.append(v)
        return o

def power(x, y):
 
    if(y == 0):
        return 1
    temp = power(x, int(y / 2))
 
    if (y % 2 == 0):
        return temp * temp
    else:
        if(y > 0):
            return x * temp * temp
        else:
            return (temp * temp) / x

M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
    for x in range(9):
        if grid[x][col] == num:
            return False
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False

grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
        [4, 0, 7, 0, 0, 0, 2, 0, 8],
        [0, 0, 5, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 9, 8, 1, 0, 0],
        [0, 4, 0, 0, 0, 3, 0, 0, 0],
        [0, 0, 0, 3, 6, 0, 0, 7, 2],
        [0, 7, 0, 0, 0, 0, 0, 0, 3],
        [9, 0, 3, 0, 0, 0, 6, 0, 4]]


if __name__ == '__main__':
    print("***************************************")
    print("Part 1:\n")
    graph = Graph()

    graph.addNode(102)
    graph.addNode(321)
    graph.addNode(422)
    graph.addNode(211)
    graph.addNode(241)
    graph.addNode(222)
    
    graph.addEdge(222, 321)
    graph.addEdge(321, 422)
    graph.addEdge(211, 321)
    graph.addEdge(102, 241)
    graph.addEdge(241, 222)

    print("Topological sort using dfs algorithm")
    print(graph.topologicalDFS())
    print("Topological sort using bfs algorithm")
    print(graph.topologicalBFS())
    print("***************************************")
    print("Part 2:\n")
    base = int(input("base: "))
    pow = int(input("pow: "))
    print("Result is :", power(base, pow))
    print("***************************************")
    print("Part 3:\n")
    
    print("Before solving:")
    print(grid)
    print("\nSolved table:")
    Suduko(grid,0,0)
    print(grid)


