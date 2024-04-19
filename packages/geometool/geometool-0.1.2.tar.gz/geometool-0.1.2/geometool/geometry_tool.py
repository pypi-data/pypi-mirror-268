from math import pi, sqrt, radians, cos
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class representing a geometric shape."""

    @abstractmethod
    def calc_area(self) -> float:
        """Calculates the area of the shape.

        Raises:
            NotImplementedError: Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclass of Shape must implement calc_area() method")

    @abstractmethod
    def calc_perimeter(self) -> float:
        """Calculates the perimeter of the shape.

        Raises:
            NotImplementedError: Must be implemented by subclasses.
        """
        raise NotImplementedError("Subclass of Shape must implement calc_perimeter() method.")


class Circle(Shape):
    """Represents a circle."""

    def __init__(self, radius: float):
        """
        Initializes a Circle object.

        Args:
            radius (float): The radius of the circle. Must be non-negative.

        Raises:
            ValueError: If the radius is negative.
        """
        if radius >= 0:
            self.radius = radius
        else:
            raise ValueError("Radius of a circle must be a non-negative number.")

    def calc_area(self) -> float:
        """Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return pi * (self.radius**2)

    def calc_perimeter(self) -> float:
        """Calculates the perimeter of the circle.

        Returns:
            float: The perimeter of the circle.
        """
        return 2 * pi * self.radius


class Triangle(Shape):
    """Represents a triangle."""

    def __init__(self, side1: float = None, side2: float = None, side3: float = None, **kwargs):
        """
        Initializes a Triangle object.

        Args:
            side1 (float, optional): Length of the first side. Defaults to None.
            side2 (float, optional): Length of the second side. Defaults to None.
            side3 (float, optional): Length of the third side. Defaults to None.
            **kwargs: Additional keyword arguments.
                - base (float): Base of the triangle (for right triangles).
                - height (float): Height of the triangle (for right triangles).
                - angle (float): Angle between two sides (in degrees).

        Raises:
            ValueError: If invalid arguments are provided or the triangle is invalid.
        """
        if side1 is not None and side2 is not None and side3 is not None:
            sides = [side1, side2, side3]
            if self._args_valid(sides):
                self.side1 = side1
                self.side2 = side2
                self.side3 = side3

        else:
            base = kwargs.get("base")
            height = kwargs.get("height")
            angle = kwargs.get("angle")

            if base is not None and height is not None:
                self.side1 = self.side2 = sqrt(base**2 + height**2)
                self.side3 = base
            elif side1 is not None and side2 is not None and angle is not None:
                angle_rad = radians(angle)
                self.side1 = side1
                self.side2 = side2
                self.side3 = sqrt(side1**2 + side2**2 - 2 * side1 * side2 * cos(angle_rad))
            else:
                raise ValueError("Invalid combination of arguments for Triangle constructor")

    def _args_valid(self, sides: list[float]) -> bool:
        """
        Validates the provided side lengths for triangle creation.

        Args:
            sides (list[float]): List of side lengths.

        Returns:
            bool: True if the side lengths are valid, False otherwise.

        Raises:
            ValueError: If a side length is negative or the triangle inequality is violated.
        """
        if not all(side > 0 for side in sides):
            raise ValueError("A Triangle side must be a positive number.")

        for i in range(3):
            other_sides = sides[:i] + sides[i + 1 :]
            if not (sum(other_sides) > sides[i]):
                raise ValueError(f"Invalid Triangle - Side lengths violate triangle inequality")

        return True
    
    
    def is_rightangled(self) -> bool:
        sides = [self.side1, self.side2, self.side3]
        sides.sort()
        
        if ( sides[0]**2 + sides[1]**2 == sides[2]**2 ):
            return True
        
        return False
        
        
    def calc_area(self) -> float:
        """Calculating the Area of the initiated Triangle object

        Returns:
            float: The Area of the triangle
                (Additionally: May return a string representing that the Triangle is rightangled)
        """
        # Finding semi-perimeter 
        sp = (self.side1 + self.side2 + self.side3) / 2
        # Calculating the area
        area = sqrt(sp * (sp - self.side1) * (sp - self.side2) * (sp - self.side3))
        # Checking if the triangle is rightangled or not
        if self.is_rightangled():
            # On True return a string represnting thet 
            return f"Triangle area is: {area}\nand the triangle is rightangled"
        # On False never mentions anything 
        # Returning the area value
        return area
    
    def calc_perimeter(self) -> float:
        """Calculates the Perimeter of the initiated Triangle object

        Returns:
            float: The perimeter of the Triangle
        """
        return self.side1 + self.side2 + self.side3




# t1 = Triangle(side1=3, side2=4, angle = 90)
# t1 = Triangle(base=3, height=4)
# print(t1.calc_area(), t1.side3)
# s1 = Circle(5)
# s2 = Triangle(3, 4, 5)
