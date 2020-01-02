import turtle

turtle.shape("turtle")
turtle.color("green")
def draw(size, b):
  if b == 0:
     turtle.fd(size)
  else:
   a = size/4
   i=0
   k=0
   draw(a, b-1)
   turtle.left(90)
   while i<2:
      draw(a, b-1)
      turtle.right(90)
      i += 1
   draw(a, b-1)
   while k<2:
      draw(a, b-1)
      turtle.left(90)
      k += 1
   draw(a, b-1)
   turtle.right(90)
   draw(a, b-1)


for n in range(4):
   p0 = turtle.pos()
   draw(300, n)
   turtle.up()
   turtle.goto(-50,0)
   turtle.down()
turtle.done()
