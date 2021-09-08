import sys
import time
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt
from utils import distance, intersect
from initialize_nodes import init_nodes
sys.path.append('osr_examples/scripts/')
import environment_2d
np.random.seed(4)
def robo(env, random = False):
  start = time.process_time()
  pl.ion()

  pl.clf()
  #Initialize nodes (grid or random)
  env.plot()
  points, x_start, y_start, x_goal, y_goal, q = init_nodes(env, random)

  #Draw edges
  edges = []
  threshold = 2.5
  for S1 in points:
    for S2 in points:
      flag = 0
      for triangle in env.obs:
        T1x, T1y, T2x, T2y, T3x, T3y = triangle.x0, triangle.y0, triangle.x1, triangle.y1, triangle.x2, triangle.y2
        if S1 != S2 and distance(S1,S2) <= threshold and (not intersect(S1[0],S1[1],S2[0],S2[1],T1x,T1y,T2x,T2y)) and (not intersect(S1[0],S1[1],S2[0],S2[1],T2x,T2y,T3x,T3y)) and (not intersect(S1[0],S1[1],S2[0],S2[1],T1x,T1y,T3x,T3y)):
          continue
        else:
          flag = 1
      if flag == 0:
        edges.append([S1[0], S2[0],S1[1], S2[1]])
        pl.plot([S1[0], S2[0]], [S1[1], S2[1]], "g", linewidth=1)

  #Dijkstra
  rank = {tuple(x):[[],-1] for x in points}
  def dijkstra(node, dist, path):
    xs, ys = node[0], node[1]
    for x,y in points:
      if [xs,x,ys,y] in edges:
        if rank[(x,y)][1] == -1 or rank[(x,y)][1] > distance(node, (x,y)) + dist:
          rank[(x,y)][1] = distance(node, (x,y)) + dist
          newpath = path + [x,y]
          rank[(x, y)][0] = newpath
          dijkstra((x,y),distance(node, (x,y)) + dist, newpath)
  dijkstra((x_start,y_start),0, [])

  #Visualization
  ##Draw path
  path = rank[(x_goal,y_goal)][0]
  ###draw first path
  pl.plot([x_start,path[0]], [y_start, path[1]], "y", linewidth=2)
  ###Draw the rest
  for i in range(0,len(path)-3,2):
    pl.plot([path[i], path[i+2]], [path[i+1], path[i+3]], "y", linewidth=2)

  if q is not None:
    x_start, y_start, x_goal, y_goal = q
    env.plot_query(x_start, y_start, x_goal, y_goal)


  print("The shortest distance calculated is:" , rank[(x_goal,y_goal)][1], "in", time.process_time() - start,"seconds.")
  plt.savefig("filename.jpg")