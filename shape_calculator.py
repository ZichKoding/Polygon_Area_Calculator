class Rectangle:
    def __init__(self, width=None, height=None):
        self.height = height
        self.width = width
        self.area = None
        self.perimeter = None
        self.diagonal = None
        self.side = None

    def set_attributes(self, new_width=None, new_height=None):
        if new_width is None:
            self.side = new_height
            return self.side
        elif new_height is None:
            self.side = new_width
            return self.side
        else:
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
        if self.side is not None:
            self.area = (self.side ** 2)
            return self.area
        else:
            self.area = (self.width * self.height)
            return self.area

    def get_perimeter(self):
        if self.side is not None:
            self.perimeter = (self.side * 4)
            return self.perimeter
        else:
            self.perimeter = ((2 * self.height) + (2 * self.width))
            return self.perimeter

    def get_diagonal(self):
        if self.side is not None:
            self.diagonal = ((self.side ** 2) * 2) ** 0.5
            return self.diagonal
        else:
            self.diagonal = (self.height ** 2 + self.width ** 2)**0.5
            return self.diagonal

    def get_amount_inside(self, x):
        self.get_area()
        x.get_area()
        self.amount_inside = int(self.area/x.area)
        return self.amount_inside

    def get_picture(self):
        try:
            if self.width > 50 or int(self.height) > 50:
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
        self.get_area()
        self.get_perimeter()
        self.get_diagonal()
        rectangle = ["Rectangle" + "(width=" + str(self.width), ", height=" + str(self.height) + ")"]
        return "".join(rectangle)



class Square(Rectangle):
    def __init__(self, side=None):
        self.side = side
        self.area = None

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
