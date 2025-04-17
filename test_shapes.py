from shapes import Rectangle, Circle

def main():
    # Create a rectangle with length 5 and width 3
    rectangle = Rectangle(5, 3)
    print(f"\nRectangle:")
    print(f"Name: {rectangle.name}")
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")

    # Create a circle with radius 4
    circle = Circle(4)
    print(f"\nCircle:")
    print(f"Name: {circle.name}")
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")

if __name__ == "__main__":
    main() 