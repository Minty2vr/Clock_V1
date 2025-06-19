#made by Minty2
import turtle as t
import datetime

loop = True

screen = t.Screen()
screen.tracer(0)
t.Screen().bgcolor("grey")
bg = t.Turtle()
clock = t.Turtle()


def bigTick(t,legth=50):
  t.left(90)
  t.penup()
  t.forward(10)
  t.pensize(10)
  t.pendown()
  t.forward(legth)
  t.bk(legth)
  t.pensize(1)
  t.penup()
  t.backward(10)
  t.right(90)

def smallTick(t,length = 25):
  t.left(90)
  t.penup()
  t.forward(20)
  t.pensize(5)
  t.pendown()
  t.forward(length)
  t.bk(length)
  t.penup()
  t.bk(20)
  t.right(90)
  
def drawHands(t,h=0,m=0,s=0):
  t.goto(0,0)
  t.pendown()
  t.pensize(1)
  t.pencolor("red")
  t.seth(90)
  t.right(360/60 * int(s)) #faces secconds
  t.forward(100) #draws the secconds hand
  t.bk(100) #returns secconds hand
  t.pencolor("black")
  t.seth(90)
  t.right(((360/12 * int(h))+360/12 * int(m)/60)+(360/12)/60 * int(s)/60) #faces hours
  t.pensize(8)
  t.forward(60) #draws hour hand
  t.bk(60) #return hour hand
  t.pensize(4)
  t.seth(90)
  t.right((360/60 * int(m))+360/60 * int(s)/60) #faces minutes
  t.forward(80) #draws minute hand
  t.backward(80) #returns minute hand
  
bg.penup()
bg.forward(200)
bg.fillcolor("white")
bg.begin_fill()
bg.left(90)
bg.pendown()
bg.circle(200)
bg.end_fill()


  
for i in range(0,60):
  bg.circle(200, 360/60)
  smallTick(bg)
  
for i in range(0,12):
  bg.circle(200, 360/12)
  bigTick(bg)

bg.penup()
bg.fillcolor("black")
bg.goto(0,100)
bg.write("XII",False,"center",("Arial",20,"normal")) #writes 12
bg.goto(60,90)
bg.write("I",False,"center",("Arial",20,"normal")) #writes 1
bg.goto(95,50)
bg.write("II",False,"center",("Arial",20,"normal")) #writes 2
bg.goto(110,-10)
bg.write("III",False,"center",("Arial",20,"normal")) #writes 3
bg.goto(95,-70)
bg.write("IV",False,"center",("Arial",20,"normal")) #writes 4
bg.goto(65,-105)
bg.write("V",False,"center",("Arial",20,"normal")) #writes 5
bg.goto(0,-125)
bg.write("VI",False,"center",("Arial",20,"normal")) #writes 6
bg.goto(-65,-110)
bg.write("VII",False,"center",("Arial",20,"normal")) #writes 7
bg.goto(-90,-75)
bg.write("VIII",False,"center",("Arial",20,"normal")) #writes 8
bg.goto(-120,-10)
bg.write("IX",False,"center",("Arial",20,"normal")) #writes 9
bg.goto(-100,55)
bg.write("X",False,"center",("Arial",20,"normal")) #writes 10
bg.goto(-60,90)
bg.write("XI",False,"center",("Arial",20,"normal")) #writes 11
bg.hideturtle()

  
while loop == True:
  clock.hideturtle()
  time = datetime.datetime.now()
  sTime = time.strftime("%S")
  mTime = time.strftime("%M")
  hTime = time.strftime("%I")
  clock.clear()
  drawHands(clock,hTime,mTime,sTime)
  screen.update()






