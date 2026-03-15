class Rectangle:
    def __init__(self,height,width):
        self._height = height #internal/private variable(underscore)
        self._width = width

    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm" 
    
    @width.setter
    def width(self,new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
    @height.setter
    def height(self,new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be grater than 0")
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
    
rectangle = Rectangle(3,4)
print(rectangle.height)
print(rectangle._width)#private variable is not meant to be used outside of class constr