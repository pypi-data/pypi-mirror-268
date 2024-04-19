# Functions 

def calculate_area(shape):
    try:
        return shape.calc_area()
    except AttributeError:
        print("The shape Object missing calc_area() method.")
        return None

def calculate_perimeter(shape):
    try:
        return shape.calc_perimeter()
    except AttributeError:
        print("The shape Object missing calc_perimeter() method.")
        return None