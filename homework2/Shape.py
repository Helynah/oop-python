"""Shape module"""


class Shape:
    """Shape class"""

    def draw(self):
        """draws the shape"""
        return "Not implemented"


class Rectangle(Shape):
    """Rectangle class"""

    def __init__(self, x, y, width, height, stroke_color="blue", fill_color="blue"):
        """Initialize the attributes"""
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.stroke_color = stroke_color
        self.fill_color = fill_color

    def draw(self):
        """simulate a draw method to the command"""
        return (
            f"\n<rect x='{self.x}' y='{self.y}' width='{self.width}' height='{self.height}' "
            f"style='fill:{self.fill_color};stroke:{self.stroke_color};'/>"
        )


class Circle(Shape):
    """Circle class"""

    def __init__(
        self, cx, cy, radius, stroke_color="blue", fill_color="blue", stroke_width=2
    ):
        """Initialize the attributes"""
        self.cx = cx
        self.cy = cy
        self.radius = radius
        self.stroke_color = stroke_color
        self.fill_color = fill_color
        self.stroke_width = stroke_width

    def draw(self):
        """simulate a draw method to the command"""
        return (
            f"\n<circle cx='{self.cx}' cy='{self.cy}' r='{self.radius}' stroke='{self.stroke_color}' "
            f"stroke-width='{self.stroke_width}' fill='{self.fill_color}'/>"
        )


class Canvas(Shape):
    """Canvas class"""

    def __init__(self, width, height):
        """Initialize the attributes"""
        self.width = width
        self.height = height
        self.shape_list = []

    def add_shape(self, shape):
        """adds the specified shape object to your shape_list."""
        self.shape_list.append(shape)

    def draw(self):
        """this method will iterate through all the shape objects in your list, and call draw()
        on each of these objects."""
        svg_code = f"<svg version='1.0' xmlns='http://www.w3.org/2000/svg' width='{self.width}' "
        svg_code += f"height='{self.height}'>"
        for shape in self.shape_list:
            svg_code += shape.draw()
        svg_code += "\n</svg>"
        return svg_code


canvas = Canvas(800, 800)
rectangle0 = Rectangle(20, 20, 200, 200, stroke_color="red", fill_color="yellow")
circle0 = Circle(200, 200, 100, stroke_color="yellow", fill_color="red")
circle1 = Circle(300, 300, 50, stroke_color="yellow", fill_color="red")
canvas.add_shape(rectangle0)
canvas.add_shape(circle0)
canvas.add_shape(circle1)
print(canvas.draw())
