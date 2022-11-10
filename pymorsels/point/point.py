class Point:
   def __init__(self, x=0, y=0, z=0):
      self.x = x
      self.y = y
      self.z = z
      
   def __repr__(self):
      return f"Point(x={self.x}, y={self.y}, z={self.z})"

   def __eq__(self, point):
      return self.x == point.x and self.y == point.y and self.z == point.z 
      
   def __add__(self, point):
      return Point(self.x + point.x, self.y + point.y, self.z + point.z)
      
   def __sub__(self, point):
      return Point(self.x - point.x, self.y - point.y, self.z - point.z)
      
   def __rmul__(self, scalar):
      # called for => scalar * Point
      return Point(self.x * scalar, self.y * scalar, self.z * scalar)

   def __mul__(self, point):
      if isinstance(point, Point):
         # called for => Point * Point
         return Point(self.x * point.x, self.y * point.y, self.z * point.z)
         
      # called for => Point * scalar   
      return Point(self.x * point, self.y * point, self.z * point)
      
   def __iter__(self):
      yield self.x
      yield self.y
      yield self.z
