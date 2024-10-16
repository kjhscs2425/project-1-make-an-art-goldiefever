import turtle

turtle.speed(300)

def draw_shape(number_of_sides):
        turtle.up()
        turtle.goto(0,1000/(number_of_sides)) 
        turtle.down()
        for i in range(number_of_sides):
            turtle.forward(1000/number_of_sides)
            turtle.right(180-(((number_of_sides-2)*180)/number_of_sides))
                         
draw_shape(8)

turtle.exitonclick()