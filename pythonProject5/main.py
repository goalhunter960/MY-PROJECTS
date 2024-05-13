import random

def create_shape(shape_type):
  """Creates a shape using dots and x's.

  Args:
    shape_type: The type of shape to create.

  Returns:
    A string representing the shape using dots and x's.
  """

  if shape_type == "square":
    return create_square()
  elif shape_type == "triangle":
    return create_triangle()
  elif shape_type == "circle":
    return create_circle()
  else:
    raise ValueError("Invalid shape type: " + shape_type)

def create_square():
  """Creates a square using dots and x's."""

  square = ""
  for i in range(4):
    square += "x" * 4
  return square

def create_triangle():
  """Creates a triangle using dots and x's."""

  triangle = ""
  for i in range(3):
    triangle += "x" + "." * (i - 1)
  return triangle

def create_circle():
  """Creates a circle using dots and x's."""

  circle = ""
  for i in range(10):
    circle += "x" if random.randint(0, 1) else "."
  return circle


def main():
  """Prints a few shapes using dots and x's."""

  print(create_shape("square"))
  print(create_shape("triangle"))
  print(create_shape("circle"))


if __name__ == "__main__":
  main()
