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
    """
    # Plot Graph
    gplot = Graph()

    # Plot vertices
    for parent, child in ancestors:
        gplot.add_vertex(parent)
        gplot.add_vertex(child)

    for parent, child in ancestors:
        gplot.add_edge(parent, child)

    # case where vertex does not exist
    if not gplot.vertices[starting_node]:
        return -1

    s = Stack()
    s.push(starting_node)
    


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
