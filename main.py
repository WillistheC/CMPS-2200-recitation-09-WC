from collections import defaultdict
from heapq import heappush, heappop 
from math import sqrt

def prim(graph):
    """
    ### TODO:
    Update this method to work when the graph has multiple connected components.
    Rather than returning a single tree, return a list of trees,
    one per component, containing the MST for each component.

    Each tree is a set of (weight, node1, node2) tuples.    
    """
    def prim_helper(visited, frontier, tree):
        if len(frontier) == 0:
            return tree
        else:
            weight, node, parent = heappop(frontier)
            if node in visited:
                return prim_helper(visited, frontier, tree)
            else:
                print('visiting', node)
                # record this edge in the tree
                tree.add((weight, node, parent))
                visited.add(node)
                for neighbor, w in graph[node]:
                    heappush(frontier, (w, neighbor, node))    
                    # compare with dijkstra:
                    # heappush(frontier, (distance + weight, neighbor))                

                return prim_helper(visited, frontier, tree)
        
    # pick first node as source arbitrarily
    visited = set()
    trees = []
    for source in graph:
        if source not in visited:
            frontier = []
            heappush(frontier, (0, source, source))
            tr = set()
            prim_helper(visited, frontier, tr)
            trees.append(tr)
    return trees

def mst_from_points(points):
    graph = {name: [] for name, x, y in points}
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            name1, x1, y1 = points[i]
            name2, x2, y2 = points[j]
            weight = sqrt((x2 - x1)**2 +(y2 - y1)**2)
            graph[name1].append((name2, weight))
            graph[name2].append((name1, weight))
    trees = prim(graph)
    return trees[0]   

def euclidean_distance(p1, p2):
    return sqrt((p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)

def test_euclidean_distance():
    assert round(euclidean_distance(('a', 5, 10), ('b', 7, 12)), 2) == 2.83
