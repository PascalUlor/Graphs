from util import Stack, Queue
from graph import Graph


def earliest_ancestor(ancestors, starting_node):
    # pass
    # 1. loop through and find all pairs with start_node/input as child
    # 2. for each pair with start node as child get the parent
        # a. if child has two parent return the least parent
        # b. if input has no parent return -1
    # 3. while parents exist repeat steps 1 and 2 for each resulting parent
    """
    Graph = {1: {3}, 2: {3}, 3: {6}, 4: {5, 8}, 5: {6,7}, 6: {}, 
            7: {}, 8: {9}, 9: {}, 10: {1}, 11: {8}}

            actual = {1: {10}, 3: {1, 2}, 2: set(), 6: {3, 5}, 5: 
{4}, 7: {5}, 4: set(), 8: {11, 4}, 9: {8}, 11: set()
, 10: set()}


error = {1: {3}, 3: {6}, 2: {3}, 6: set(), 5: {6, 7},
 7: set(), 4: {8, 5}, 8: {9}, 9: set(), 11: {8}, 10:
 {1}}
    """
    # Plot Graph
    gplot = Graph()

    # Plot vertices
    for parent, child in ancestors:
        gplot.add_vertex(parent)
        gplot.add_vertex(child)
        gplot.add_edge(child, parent)
        
    # Do a BFS (with paths)
    # create a queue
    q = Queue()
    # enqueue starting node inside a list
    q.enqueue([starting_node])
    # set a max path length to 1
    max_path_length = 1
    # set initial earlyest ancestor
    earliest_ancestor = -1
    # while queue has contents
    while q.size() > 0:
        # dequeue the path
        path = q.dequeue()
        # get the last vert
        vert = path[-1]
        # if path is longer or equal and the value is smaller, or if the path is longer
        if (len(path) >= max_path_length and vert < earliest_ancestor) or (len(path) > max_path_length):
            # set the earliest ancestor to the vert
            earliest_ancestor = vert
            # set the max path length to the len of the path
            max_path_length = len(path)
        # loop over each neighbor in the graphs vertices at index of vert
        for neighbor in gplot.vertices[vert]:
            # make a copy of the path
            path_copy = list(path)
            # append neighbor to the coppied path
            path_copy.append(neighbor)
            # then enqueue the copied path
            q.enqueue(path_copy)
    # return earliest ancestor
    return earliest_ancestor


    # print('======',gplot.vertices)
    # print('+++++++',gplot.vertices[-4])
    # root = []
    # for i in range(0, len(ancestors)):
    #     for j in range(0, len(ancestors[0])):
    #         if starting_node == ancestors[i][j] and ancestors[i][-1] == ancestors[i][j]:
    #             fam = list()
    #             fam.append(ancestors[i])
    #             print('found', ancestors[i][-1])
    #             s = Stack()
    #             visited = set()
    #             s.push(starting_node)
    #             while s.size() > 0:
    #                 vertex = s.pop()
    #                 if ancestors[i][-1] == vertex and vertex not in visited:
    #                     visited.add(vertex)
    #                     s.push(ancestors[i][0])
    #                 elif ancestors[i][-1] != vertex and vertex in visited:
    #                     return root.append(vertex)
    # return root[0]
