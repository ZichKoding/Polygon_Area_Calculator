class Rectangle:
  def __init__(self, width, height):
    self.height = height
    self.width = width
    self.area = None
    self.perimeter = None
    self.diagonal = None

  def set_attributes(self, new_width, new_height):
    self.width = new_width
    self.height = new_height
    return self.width, self.height

  def set_width(self, new_width):
    self.width = new_width
    return self.width
  
  def set_height(self, new_height):
    self.height = new_height
    return self.height

  def get_area(self):
    self.area = self.height * self.width
    return self.area

  def get_perimeter(self):
    self.perimeter = ((2 * self.height) + (2 * self.width))
    return self.perimeter

  def get_diagonal(self):
    self.diagonal = (self.height ** 2 + self.width ** 2)**0.5
    return self.diagonal

  def __repr__(self):
    self.get_area()
    self.get_perimeter()
    self.get_diagonal()
    rectangle = ["Rectangle" + "(width=" + str(self.width), ", height=" + str(self.height) + ")"]
    return "".join(rectangle)




class Square:
  def __init__(self, side):
    self.side = side
    self.area = None
    self.perimeter = None
    self.diagonal = None

  def get_area(self):
    self.area = pow(self.side, 2)
    return self.area

  def set_side(self, new_side):
    self.side = new_side
    return self.side

  def set_attributes(self, new_width, new_height):
    self.side = new_width
    self.side = new_height
    return self.side, self.side

  def set_width(self, new_width):
    self.side = new_width
    return self.side
  
  def set_height(self, new_height):
    self.side = new_height
    return self.side

  def get_perimeter(self):
    self.perimeter = self.side * 4
    return self.perimeter

  def get_diagonal(self):
    self.diagonal = (self.side ** 2 + self.side ** 2)**0.5
    return self.diagonal

  def __repr__(self):
    self.get_area()
    self.get_perimeter()
    self.get_diagonal()
    square = ["Square" + "(side=" + str(self.side) + ")"]
    return "".join(square)
