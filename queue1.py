import turtle
from turtle import *

turtle.clear()


turtle.title("Welcome to data structure (queue)")

turtle.home()
CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

turtle.penup()
turtle.goto(0,260)

turtle.write("REAR                  FRONT", align="center", font=("Courier", 24, "normal"))
turtle.bgcolor('white')
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.bgcolor("tan")
#insert
def insert(x,y):
    turtle.penup()
    turtle.goto(200,0)
    turtle.pendown()
    n=int(input("enter the number of node to be insert"))
    loadwindow=turtle.screensize()
    turtle.speed(2)
   
             
    for i in range(0,n):
        a=int(input("enter the number of element"))
        print(i)

      #fill colour in cell
        
        fillcolor("pink")
        begin_fill()
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        end_fill()
        turtle.stamp()
        turtle.write(a,font=('Arial',10,'normal'),align='left') #for print number in cell and draw node
        turtle.penup()
        turtle.backward(i+70)
        turtle.pendown()
        turtle.hideturtle()
       

# create insert button
button = Turtle()
button.hideturtle()
button.shape('square')
button.fillcolor('Khaki')
button.penup()
button.goto(-70, 300)
button.write("Insert", align='center', font=FONT)
button.sety(300 + CURSOR_SIZE + FONT_SIZE)
button.onclick(insert)
button.showturtle()    



#update
def update(x,y):
   
    n=int(input("enter the number of node to be update"))
    loadwindow=turtle.screensize()
    turtle.speed(2)
   
             
    for i in range(0,n):
        a=int(input("enter the number of element"))
        print(i)

      #fill colour in cell
        fillcolor("sky blue")
        begin_fill()
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        end_fill()
        turtle.stamp()
        turtle.write(a,font=('Arial',10,'normal'),align='left') #for print number in cell and draw node 
        turtle.penup()
        turtle.backward(i+70)
        turtle.pendown()
        turtle.hideturtle()
        
# create update button
button1 = Turtle()
button1.hideturtle()
button1.shape('square')
button1.fillcolor('powderblue')
button1.penup()
button1.goto(-10, 300)
button1.write("update", align='center', font=FONT)
button1.sety(300 + CURSOR_SIZE + FONT_SIZE)
button1.onclick(update)
button1.showturtle()    








#Delete
def delete(x,y):
     n=int(input("enter the number of node to be delete"))

     loadwindow=turtle.screensize()
     turtle.speed(2)
     turtle.goto(200,0)
             
     for i in range(0,n):
        a=int(input("enter the number of element"))
        print(i)

      #fill colour in cell
        fillcolor("tan")
        begin_fill()
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        turtle.forward(70)
        turtle.left(90)
        end_fill()
        turtle.stamp()
        turtle.write(a,font=('Arial',10,'normal'),align='left') #for print number in cell and draw node 
        turtle.penup()
        turtle.backward(i+70)
        turtle.pendown()
        turtle.hideturtle()
    
   
  
        
             
# create delete button
button2 = Turtle()
button2.hideturtle()
button2.shape('square')
button2.fillcolor('lightgreen')
button2.penup()
button2.goto(50, 300)
button2.write("delete", align='center', font=FONT)
button2.sety(300 + CURSOR_SIZE + FONT_SIZE)
button2.onclick(delete)
button2.showturtle()




#end
turtle.done()
turtle.exitonclick()
