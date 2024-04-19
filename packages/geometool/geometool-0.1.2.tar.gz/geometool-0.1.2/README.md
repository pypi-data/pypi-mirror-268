# Geometool - Geometric Shape Calculation Library

**```MB Task-1```**

**New: Added the ability of defining a triangle using **kwargs** 

    - Triangle(base, height) 

    - Triangle(side1, side2, angle between them in degrees)


This Python package provides functions to calculate the area and perimeter of various geometric shapes.

## Installation

You can install the package using pip:

```bash
$ pip install geometool
```

## Methods

The package provides the following functions:

- `calculate_area(shape)` : Calculates the area of a given shape. Supported shapes include:
    - Circle(radius)
    - Triangle()
- `calculate_perimeter(shape)`: Calculates the perimeter of a given shape. Supported shapes include:
    - Circle(radius)
    - Triangle()

## Classes

### Shape
Abstract base class for geometric shapes.

### Circle
- `calc_area()` to calculate the area.
- `calc_perimeter()` to calculate the perimeter.

### Triangle
- `calc_area()` to calculate the area.
- `calc_perimeter()` to calculate the perimeter.
- `is_rightangled()` to check if the triangle is right-angled.


## Usage

```bash
import geometool as g

# Declare a shape object 

s1 = g.Circle(5)
s2 = g.Triangle(6, 8, 9)

# Use calculate_area() and calculate_perimeter() to calculate the area and perimeter of the object
g.calculate_area(s1)
g.calculate_perimeter(s1)
g.calculate_area(s2)
g.calculate_perimeter(s2)
```


## Authors: 
Idris Taha
- E-mail: dri.taha24@gmail.com
- *@idristaha*