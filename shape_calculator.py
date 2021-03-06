class Rectangle:
  def __init__(self, width=None, height=None):
    self.height = height
    self.width = width
    self.area = None
    self.perimeter = None
    self.diagonal = None
    self.side = None

  def set_attributes(self, new_width=None, new_height=None):  # This function will set new height and width attributes overwriting the previous ones. 
    if new_width is None: # The self.side parts are mainly for the subclass Square below.
      self.side = new_height
      return self.side
    elif new_height is None:
      self.side = new_width
      return self.side
    else:
      self.width = new_width
      self.height = new_height
      return self.width, self.height

  def set_width(self, new_width): # This function will set a new width overwriting the previous one.
    self.width = new_width
    return self.width

  def set_height(self, new_height): # This function will set a new height overwriting the previous one.
    self.height = new_height
    return self.height

  def get_area(self): # This funtions will get the area and is able to be used for square or rectangle.
    if self.side is not None:  # The self.side parts are mainly for the subclass Square below.
      self.area = (self.side ** 2)
      return self.area
    else:
      self.area = (self.width * self.height)
      return self.area

  def get_perimeter(self):# This funtions will get the perimeter and is able to be used for square or rectangle.
    if self.side is not None: # The self.side parts are mainly for the subclass Square below.
      self.perimeter = (self.side * 4)
      return self.perimeter
    else:
      self.perimeter = ((2 * self.height) + (2 * self.width))
      return self.perimeter

  def get_diagonal(self): # This funtions will get the diagonal length and is able to be used for square or rectangle.
    if self.side is not None: # The self.side parts are mainly for the subclass Square below.
      self.diagonal = ((self.side ** 2) * 2) ** 0.5
      return self.diagonal
    else:
      self.diagonal = (self.height ** 2 + self.width ** 2)**0.5
      return self.diagonal

  def get_amount_inside(self, x): # x is the object/class being called to see how many can fit inside the object you are using to call this method. 
    self.get_area() # I had to add the get_area() methods inside this function to make sure you don't have to use them prior to the get_amount_inside() method.
    x.get_area()
    self.amount_inside = int(self.area/x.area) # Using int() automatically rounds down the function to the whole number.
    return self.amount_inside

  def get_picture(self): # It shows the object via "*". So if you have a square side is 5, it'll print out 5 rows and columns of astericks. 
    try:  # The try is for the rectangles becuase when I added the self.side to the if statement it'd give me a None type error for certain scenarios. So, the except is if the try fails it'll go as a Square. 
      if self.width > 50 or self.height > 50:
        return "Too big for picture."
      else:
        self.picture = []
        for x in range(self.height):
          x = self.width * "*"
          self.picture.append(x + '\n')
        return ''.join(self.picture)
    except:
      if self.side > 50:
        return "Too big for picture."
      else:
        self.picture = []
        for x in range(self.side):
          x = self.side * "*"
          self.picture.append(x + '\n')
        return ''.join(self.picture)

  def __repr__(self):
    rectangle = ["Rectangle" + "(width=" + str(self.width), ", height=" + str(self.height) + ")"]
    return "".join(rectangle)


class Square(Rectangle): # This subclass inherits all of the Rectangle class's methods.
  def __init__(self, side=None):
    self.side = side
  # The next 3 methods below are for you decide to call the side height or width instead of side. 
  def set_side(self, new_side):
    self.side = new_side
    return self.side
  def set_width(self, new_width):
    self.side = new_width
    return self.side
  def set_height(self, new_height):
    self.side = new_height
    return self.side

  def __repr__(self):
    square = ["Square" + "(side=" + str(self.side) + ")"]
    return "".join(square)
