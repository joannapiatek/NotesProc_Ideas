class Point:
    def __init__(self, x_coor, y_coor):
        self.x_coor = x_coor
        self.y_coor = y_coor


class Pixel(Point):
    def __init__(self, x_coor, y_coor, value):
        Point.__init__(self, x_coor, y_coor)
        self.value = value


class Rectangle:
    def __init__(self, left_bott, right_bott, right_up, left_up):
        self.left_bott = left_bott
        self.right_bott = right_bott
        self.right_up = right_up
        self.left_up = left_up
