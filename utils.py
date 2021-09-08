import math
def ccw(Ax,Ay, Bx,By, Cx,Cy):
  return (Cy - Ay) * (Bx - Ax) > (By - Ay) * (Cx - Ax)
def intersect(Ax,Ay, Bx,By, Cx,Cy,Dx,Dy):
  return ccw(Ax,Ay, Cx,Cy, Dx,Dy) != ccw(Bx,By, Cx,Cy,Dx,Dy) and ccw(Ax,Ay, Bx,By, Cx,Cy) != ccw(Ax,Ay, Bx,By, Dx,Dy)
def distance(p1,p2):
   return math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )