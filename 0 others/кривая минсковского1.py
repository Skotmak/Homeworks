import turtle

turtle.shape("turtle")
turtle.color("blue")
def mink_line(size, n):
  if n == 0:
     turtle.fd(size)
  else:
   a = size/4
   #while i<2
   mink_line(a, n-1)
   turtle.left(90)
   mink_line(a, n-1)
   turtle.right(90)
   mink_line(a, n-1)
   turtle.right(90)
   mink_line(a, n-1)
   mink_line(a, n-1)
   turtle.left(90)
   mink_line(a, n-1)
   turtle.left(90)
   mink_line(a, n-1)
   turtle.right(90)
   mink_line(a, n-1)


for n in range(4):
   p0 = turtle.pos()
   mink_line(300, n)
   turtle.up()
   turtle.goto(p0)
   turtle.down()
turtle.done()
