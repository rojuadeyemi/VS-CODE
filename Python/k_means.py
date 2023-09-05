class Point:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __repr__(self):
		return f"Point({self.x}, {self.y})"
	
	def __add__(self, other):
		return Point(self.x +other.x, self.y+other.y)
	def __neg__(self):
		return Point(-self.x, -self.y)
		
	def __sub__(self, other):
		new = other.__neg__()
		return self.__add__(new)
		
	def __mul__(self, other):
		if isinstance(other, (int, float)):
			return Point(self.x *other, self.y *other)
		else: # dot product
			return self.x*other.x + self.y*other.y
			
	def distance(self, other):
		p = self - other
		return (p.x**2 +p.y**2)**0.5

class Cluster(object):
		
		def __init__(self, x, y):
			self.center = Point(x, y)
			self.points = []
		
		def update(self):
			
			x_c = sum([point.x for point in self.points])/len(self.points)
			y_c = sum([point.y for point in self.points])/len(self.points)
			
			self.center = Point(x_c, y_c)
			self.points = []
			
		def add_point(self, point):
			self.points.append(point)
			
def kmean(pointss):
			points = [Point(*point) for point in pointss]
			c1 = Cluster(1,0)
			c2 = Cluster(-1,0)
			c1_old = []
			for _ in range(10000):
				for point in points:
					if point.distance(c1.center)<point.distance(c2.center):
						c1.add_point(point)
					else:
						c2.add_point(point)
						
				if c1_old == c1:
					break
				else:
					c1_old = c1
					c1.update()
					c2.update()
			cluster1 = [(a.x, a.y) for a in c1.points]
			cluster2= [(a.x, a.y) for a in c2.points]
			return f""" From the points {pointss}
					C1 = {cluster1}
					centroid: ({c1.center.x},{c1.center.y})
					
					
					C2 = {cluster2} 
					centroid: ({c2.center.x},{c2.center.y})"""
					
			
p = [(4,1),(3,-2), (-1,-4),(-5,6),(3,8),(1,2),(8,1),(-3,4),(-2,5),(8,-5),(11,-3),(1,1),(-3,7),(-3,1),(1,2),(0,-1),(-4,-2)]

print(kmean(p))