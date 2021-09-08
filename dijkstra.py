import math
def distance(p1,p2):
   return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
def dijkstra(node, dist, path, VE):
    points, edges = VE[0], VE[1]
    rank = {tuple(x): [[], -1] for x in points}
    xs, ys = node[0], node[1]
    for x,y in points:
        if [xs,x,ys,y] in edges:
          if rank[(x,y)][1] == -1 or rank[(x,y)][1] > distance(node, (x,y)) + dist:
            rank[(x,y)][1] = distance(node, (x,y)) + dist
            newpath = path + [x,y]
            rank[(x, y)][0] = newpath
            dijkstra((x,y),distance(node, (x,y)) + dist, newpath, VE)
    return rank