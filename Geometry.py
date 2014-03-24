## File: Geometry.py
## Description: class of Point, Line and Triangle, all corner tests
##              have been passed. Each function has been commented. Time consumed 8 hours
## Author: Xiaoqin LI
## Date Created: 01/27/2014
## Date Last Modified:01/31/2014

import math

#function that tests for equality of two floating point numbers
def is_equal (a, b):
  delta = 1.0e-16
  return (abs (a - b) < delta)

tol = 1.0e-16

class Point (object):
  # constructor of Point 
  def __init__ (self, x = 0.0, y= 0.0):
    self.x = x
    self.y = y
    
  # get distance between two points
  def dist (self, p):
    return math.hypot (self.x - p.x, self.y - p.y)
  
  # string representation of a Point object
  def __str__ (self):
    return ('(' + str(self.x) + ', ' + str(self.y) + ')')
  
  # test for equality
  def __eq__ (self, p):
      if is_equal (self.x, p.x) and is_equal (self.y, p.y):
          return True
      else: return False


class Line (object):
  # constructor
  def __init__ (self, p1_x = 0.0, p1_y = 0.0, p2_x = 1.0, p2_y = 1.0):
    if is_equal(p1_x, p2_x) and is_equal(p1_y, p2_y):
      self.point1 = Point(0,0)
      self.point2 = Point(1,1)
    else:
      self.point1 = Point(p1_x,p1_y)
      self.point2 = Point(p2_x,p2_y)
        
  # determine if the line is parallel to x-axis
  def is_parallelX (self):
    if (not is_equal(self.point1.x, self.point2.x)) and (is_equal(self.point1.y, self.point2.y)): 
      return True
    else: return False
    
  # determine if the line is parallel to y-axis
  def is_parallelY (self):
    if is_equal(self.point1.x, self.point2.x) and (not is_equal(self.point1.y, self.point2.y)):  
      return True
    else: return False
        
  # get slope of line       
  def slope (self):
    if not is_equal(self.point1.x, self.point2.x):                          
      return ((self.point1.y-self.point2.y)/(self.point1.x-self.point2.x))
    else:                                                                     
      return (float('inf'))                                   # return 'inf 'if the line is parallel to Y-axis
        
  # determine if two lines are parallel
  def is_parallel (self, line1):
    if not self.is_parallelY() or not line1.is_parallelY():
      if is_equal(self.slope(), line1.slope()):
        return True
      else: return False
    else: return True
        
  # get y axis intercept if line is not parallel to the y axis
  def y_intercept(self):
    if not self.is_parallelY():
      return (self.point1.y - self.slope()*self.point1.x)
    else:
      return None                                             # return 'None' if the line is parallel to Y-axis

  # get x axis intercept if line is not parallel to the x axis
  def x_intercept(self):
    if not self.is_parallelX():
      return (-self.y_intersect() / self.slope())
    else:
      return None                                             # return 'None' if the line is parallel to X-axis

  # return intersection point if two lines are not parallel
  def intersection_point (self, line1):
    if not self.is_parallel(line1):
      inter_point = Point()     
      if self.is_parallelY():
        inter_point.x = self.point1.x
        inter_point.y = self.point1.x * line1.slope() + line1.y_intercept()
      elif line1.is_parallelY():
        inter_point.x = line1.point1.x
        inter_point.y = line1.point1.x * self.slope() + self.y_intercept()
      else:  
        inter_point.x = (line1.y_intercept() - self.y_intercept()) / (self.slope() - line1.slope())
        inter_point.y = self.slope()*inter_point.x + self.y_intercept()             
      return inter_point
    else:
      return None                                                       # return 'None' if two lines are parallel.  
                        
  # determine if two lines are perpendicular to each other
  def is_perpendicular (self, line1):
    if not self.is_parallel(line1):
      if self.is_parallelY():
        if line1.is_parallelX():        
          return True
      elif line1.is_parallelY():
        if self.is_parallelX():
          return True
      else:
        if is_equal(self.slope() * line1.slope(), -1):
          return True
        else:
          return False
      
  # determine if a point is on the line or an extension of it
  def on_line (self, p1):
    if not self.is_parallelY():
      if is_equal((p1.x * self.slope() + self.y_intercept()), p1.y):
        return True
      else:
        return False
    else:
      if is_equal(p1.x, self.point1.x):
        return True
      else:
        return False
      
  # determine the perpendicular distance of a point to the line 
  # if the point is not on the line
  def dist (self, p1):
    if self.on_line(p1):
      return 0                                            # return 0 if the point is on the line
    else:
      if self.is_parallelX():
        return abs(p1.y - self.point1.y)
      if self.is_parallelY():
        return abs(p1.x - self.point1.x)
      else:
        return(abs(self.slope()*p1.x - p1.y + self.y_intercept()) / math.sqrt(self.slope()**2 + 1))
    
  # determine if two points are on the same side of the line
  # if one or both the points are on the line return False
  def on_same_side (self, p1, p2):
    if self.on_line(p1) or self.on_line(p2):
      return False
    else:
      # delta product method
      delta = ((self.point1.y - self.point2.y) * (p1.x - self.point1.x) + (self.point2.x - self.point1.x) * (p1.y - self.point1.y )) * \
              ((self.point1.y - self.point2.y) * (p2.x - self.point1.x) + (self.point2.x - self.point1.x) * (p2.y - self.point1.y ))
      if delta > 0:
        return True
      else:
        return False     
  
  # string representation of a line
  def __str__ (self):
    if self.is_parallelY():
      return ('x = ' + str(self.point1.x))
    elif self.is_parallelX():
      return ('y = ' + str(self.point1.y))
    else:
      if self.y_intercept() < tol:
        return ('y = ' + str(self.slope()) + ' * x' + ' - ' + str(abs(self.y_intercept())))
      else:
        return ('y = ' + str(self.slope()) + ' * x' + ' + ' + str(self.y_intercept()))

  # determine if two lines are equal, have same slope and intercept
  def __eq__ (self, line1):
    if self.is_parallelY() and line1.is_parallelY():
      if (self.point1.x - line1.point1.x) < tol:
        return True
      else:
        return False
    elif (not self.is_parallelY) and (not line1.is_parallelY()):
      if (self.slope() - line1.slope() < tol ) and (self.y_intercept() - line1.y_intercept() < tol ):
        return True
      else:
        return False
    else:
      return False


class Triangle (object):
  # constructor (assign default vertices (0,0), (1,0), and (0, 1))
  # assign default vertices if user defined points do not form a triangle
  def __init__ (self, v1_x = 0, v1_y =0, v2_x = 1, v2_y = 0, v3_x = 0, v3_y = 1):
    if self.is_triangle(v1_x, v1_y, v2_x, v2_y, v3_x, v3_y):
      self.point1 = Point (v1_x,v1_y)
      self.point2 = Point (v2_x,v2_y)
      self.point3 = Point (v3_x,v3_y)
    else:
      self.point1 = Point (0,0)
      self.point2 = Point (1,0)
      self.point3 = Point (0,1)
    self.s1 = self.point1.dist(self.point2)
    self.s2 = self.point2.dist(self.point3)
    self.s3 = self.point3.dist(self.point1)
    self.line1 = Line(self.point1.x, self.point1.y, self.point2.x, self.point2.y)
    self.line2 = Line(self.point2.x, self.point2.y, self.point3.x, self.point3.y)
    self.line3 = Line(self.point3.x, self.point3.y, self.point1.x, self.point1.y)

  # determine if three points form a triangle
  # if sum of two shorter sides is greater than the longest side, it is a triangle
  def is_triangle (self, p1_x, p1_y, p2_x, p2_y, p3_x, p3_y):
    s1= math.sqrt((p1_x-p2_x)**2 + (p1_y-p2_y)**2)
    s2= math.sqrt((p2_x-p3_x)**2 + (p2_y-p3_y)**2)
    s3= math.sqrt((p3_x-p1_x)**2 + (p3_y-p1_y)**2)
    side_list = sorted([s1,s2,s3])
    if is_equal((side_list[0] + side_list[1]),side_list[2]):         
      return False
    else:
      return True
    
  # calculate area of triangle,if sides are a, b, and c, then s = (a + b + c) / 2
  # area = math.sqrt (s * (s - a) * (s -b) * (s - c))
  def area (self):
    ss = (self.s1 + self.s2 + self.s3) / 2
    return (math.sqrt (ss * (ss - self.s1) * (ss - self.s2) * (ss - self.s3)))
  
  # calculate perimeter
  def perimeter (self):
    return (self.s1 + self.s2 + self.s3)
  
  # determine if a point is inside the triangle (Utilizing Barycentric coordinates methods on triangles)
  def is_point_inside (self, point):
    alpha = ((self.point2.y - self.point3.y)*(point.x - self.point3.x) + (self.point3.x - self.point2.x)*(point.y - self.point3.y)) / \
            ((self.point2.y - self.point3.y)*(self.point1.x - self.point3.x) + (self.point3.x - self.point2.x)*(self.point1.y - self.point3.y))
    beta = ((self.point3.y - self.point1.y)*(point.x - self.point3.x) + (self.point1.x - self.point3.x)*(point.y - self.point3.y)) / \
            ((self.point2.y - self.point3.y)*(self.point1.x - self.point3.x) + (self.point3.x - self.point2.x)*(self.point1.y - self.point3.y))
    gamma = 1.0 - alpha - beta
    if (abs(alpha) < tol or alpha > 0) and (abs(beta) < tol or beta >0) and (abs(gamma) < tol or gamma > 0):
      return True
    else:
      return False
  
  # determine if the triangle is completely inside the other triangle
  def is_inside_triangle (self, triangle1):
      if triangle1.is_point_inside(self.point1) and triangle1.is_point_inside(self.point2) and triangle1.is_point_inside(self.point3):
        return True
      else:
        return False
    
  # determine if the triangle overlaps the other triangle
  # Based on Barycentric coordinates methods, beside the "one is inside another" casem
  # if the intersection point of any line in these two triangle
  # is strictly between both of end points of both edges, return true(utilizing vector dot product method)
  def does_overlap_triangle (self, triangle1):
    if self.is_inside_triangle(triangle1) or triangle1.is_inside_triangle(self): 
      return True
    for i in range(1,4):
      for j in range(1,4):
          point_intersect = eval("self.line"+str(i)+".intersection_point(triangle1.line"+str(j)+")")
          if point_intersect is not None:
            intersect_self_edge_x1 = eval("self.line"+str(i)+".point1.x")
            intersect_self_edge_x2 = eval("self.line"+str(i)+".point2.x")
            intersect_self_edge_y1 = eval("self.line"+str(i)+".point1.y")
            intersect_self_edge_y2 = eval("self.line"+str(i)+".point2.y")            
            intersect_triangle1_edge_x1 = eval("triangle1.line"+str(j)+".point1.x")
            intersect_triangle1_edge_x2 = eval("triangle1.line"+str(j)+".point2.x")
            intersect_triangle1_edge_y1 = eval("triangle1.line"+str(j)+".point1.y")
            intersect_triangle1_edge_y2 = eval("triangle1.line"+str(j)+".point2.y")
            if ((point_intersect.x - intersect_self_edge_x1) * (point_intersect.x - intersect_self_edge_x2) + \
                (point_intersect.y - intersect_self_edge_y1) * (point_intersect.y - intersect_self_edge_y2)) < 0:
                if ((point_intersect.x - intersect_triangle1_edge_x1) * (point_intersect.x - intersect_triangle1_edge_x2) + \
                (point_intersect.y - intersect_triangle1_edge_y1) * (point_intersect.y - intersect_triangle1_edge_y2)) < 0:
                    return True
                else: continue
            else: continue                        
          else: continue
      return False
      
  #determine if a line passes through the triangle even if it is one point
  def does_intersect (self, line1):
    if line1.on_line (self.point1) or (line1.on_line (self.point2) or line1.on_line (self.point3)):
      return True        
    elif line1.on_same_side(self.point1,self.point2) and (line1.on_same_side(self.point2,self.point3) and line1.on_same_side(self.point3,self.point1)):
      return False
    else:
      return True
    
  # string representation of all three vertices
  def __str__ (self):
    return (self.point1.__str__() + ', ' + self.point2.__str__() + ', ' +self.point3.__str__())
    
  # determine if two triangles are congruent: three sides of one are equal to three sides of the other
  def __eq__ (self, triangle1):
    sides_self = sorted([self.s1, self.s2, self.s3])
    sides_triangle1 = sorted([triangle1.s1, triangle1.s2, triangle1.s3])
    if (is_equal(sides_self[0], sides_triangle1[0])) and (is_equal(sides_self[1], sides_triangle1[1]) and is_equal(sides_self[2], sides_triangle1[2])):
      return True
    else:
      return False
    
def main():
  infile = open("geometry.txt","r")             # open file "geometry.txt" for reading
  two_points_data_list = [] 
  numberOfRows = 6
  numberOfColumns = 2 
  for row in range(numberOfRows):
    two_points_data_list.append([]) # Add an empty new row
    current_point_reading = infile.readline()
    current_point_reading = current_point_reading.split()
    for entry in  current_point_reading:
      two_points_data_list[row].append(float(entry))
      if len(two_points_data_list[row]) == 2:
        break
      
  pointP = Point(two_points_data_list[0][0],two_points_data_list[0][1])   # read the coordinates of the first Point P
  pointQ = Point(two_points_data_list[1][0],two_points_data_list[1][1])   # read the coordinates of the second Point Q
  pointA = Point(two_points_data_list[2][0],two_points_data_list[2][1])   # read the coordinates of the third Point A
  pointB = Point(two_points_data_list[3][0],two_points_data_list[3][1])   # read the coordinates of the fourth Point B
  pointG = Point(two_points_data_list[4][0],two_points_data_list[4][1])   # read the coordinates of the fifth Point G
  pointH = Point(two_points_data_list[5][0],two_points_data_list[5][1])   # read the coordinates of the sixth Point H
  linePQ = Line(pointP.x, pointP.y, pointQ.x, pointQ.y)
  lineAB = Line(pointA.x, pointA.y, pointB.x, pointB.y)
  lineGH = Line(pointG.x, pointG.y, pointH.x, pointH.y)

  print("Coordinates of P:", pointP)
  print("Coordinates of Q:", pointQ)
  print("Distance between P and Q:", format(pointP.dist(pointQ),'.2f'))    # print distance between P and Q
  print("Slope and Intercept of PQ:", linePQ.slope(), linePQ.y_intercept())  # print the slope and intercept of the line passing through P and Q
  print("Coordinates of A:", pointA)
  print("Coordinates of B:", pointB)
  print("Slope and Intercept of AB:", lineAB.slope(), lineAB.y_intercept()) # print the slope and intercept of the line passing through A and B
  
  if linePQ.is_parallel(lineAB):                               # print if the lines PQ and AB are parallel or not
    print("PQ is parallel to AB")
  else:
    print("PQ is not parallel to AB")

  if linePQ.is_perpendicular(lineAB):                     # print if the lines PQ and AB are perpendicular or not
    print("PQ is perpendicular to AB")
  else:
    print("PQ is not perpendicular to AB")

  print("Coordinates of intersection point of PQ and AB:", linePQ.intersection_point(lineAB))    # print if coordinates of the intersection point if PQ is not parallel to AB
  print("Coordinates of G:", pointG)
  print("Coordinates of H:", pointH)

  if linePQ.on_same_side ( pointG, pointH):               # print if the the points G and H are on the same side of PQ
    print("G and H are on the same side of PQ")
  else:
    print("G and H are not on the same side of PQ")

  if lineAB.on_same_side ( pointG, pointH):               # print if the the points G and H are on the same side of PQ
    print("G and H are on the same side of AB")
  else:
    print("G and H are not on the same side of AB")

  three_points_data_list = [] 
  numberOfRows = 2
  numberOfColumns = 2 
  for row in range(numberOfRows):
    three_points_data_list.append([]) # Add an empty new row
    current_point_reading = infile.readline()
    current_point_reading = current_point_reading.split()
    for entry in current_point_reading:
      three_points_data_list[row].append(float(entry))
      if len(three_points_data_list[row])== 6:
        break
      
  # read the coordinates of the vertices R, S, and T
  verR = Point(three_points_data_list[0][0],three_points_data_list[0][1])
  verS = Point(three_points_data_list[0][2],three_points_data_list[0][3])
  verT = Point(three_points_data_list[0][4],three_points_data_list[0][5])
  # read the coordinates of the vertices J, K, and L
  verJ = Point(three_points_data_list[1][0],three_points_data_list[1][1])
  verK = Point(three_points_data_list[1][2],three_points_data_list[1][3])
  verL = Point(three_points_data_list[1][4],three_points_data_list[1][5])
  
  triangleRST = Triangle(verR.x, verR.y, verS.x, verS.y, verT.x, verT.y)
  triangleJKL = Triangle(verJ.x, verJ.y, verK.x, verK.y, verL.x, verL.y)

  print("Vertices of triangle RST:", triangleRST)
  print("Perimeter of triangle RST:", format(triangleRST.perimeter(), '.2f'))   # print the perimeter of triangle RST
  print("Area of triangle RST:", format(triangleRST.area(), '.2f'))             # print the area of triangle RST
  
  if triangleRST.does_intersect(linePQ):                      # print if the line PQ passes through the triangle RST
    print("PQ does pass through triangle RST")
  else:
    print("PQ does not pass through triangle RST")
    
  if triangleRST.does_intersect(lineAB):                      # print if the line AB passes through the triangle RST
    print("AB does pass through triangle RST")
  else:
    print("AB does not pass through triangle RST")
    
  print("Vertices of triangle JKL:", triangleJKL)
  
  if triangleJKL.is_inside_triangle(triangleRST):              # print if triangle JKL is inside triangle RST
    print("Triangle JKL is inside triangle RST")
  else:
    print("Triangle JKL is not inside triangle RST")

  if triangleJKL.does_overlap_triangle(triangleRST):           # print("Triangle JKL overlaps to triangle RST")
    print("Triangle JKL does overlap triangle RST")
  else:
    print("Triangle JKL does not overlap triangle RST")

  if triangleJKL == triangleRST:                               # print if triangle JKL is congruent to triangle RST
    print("Triangle JKL is congruent to triangle RST")
  else:
    print("Triangle JKL is not congruent to triangle RST")
  
  infile.close()# close file "geometry.txt"

main()
