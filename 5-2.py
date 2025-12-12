import turtle, random
colosrs=["red", "green", "blue", "orange", "purple", "pink", "yellow"]
painter = turtle.Turtle()
painter. pensize (3)
for i in range (100):
  color = random.choice(colors)
  painter-pencolor (color)
  painter.circle (100)
  painter.right (30)
  painter.left (60)
  painter.setposition (0, 0)
