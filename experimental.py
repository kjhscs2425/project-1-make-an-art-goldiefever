import turtle

def draw_pod():
    # Draw the pod
    turtle.color("green")
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(100)
    turtle.circle(50, 180)
    turtle.forward(100)
    turtle.circle(50, 180)
    turtle.end_fill()
    turtle.right(90)

def draw_pea(x, y):
    # Draw a single pea
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("lightgreen")
    turtle.begin_fill()
    turtle.circle(15)  # Pea
    turtle.end_fill()
    
    # Draw the face
    turtle.color("black")
    # Eyes
    for eye_x in [-7, 7]:  # Adjust x-coordinates for eyes
        turtle.penup()
        turtle.goto(x + eye_x, y + 5)
        turtle.pendown()
        turtle.circle(2)  # Draw eyes
    
    # Smile
    turtle.penup()
    turtle.goto(x - 7, y - 5)
    turtle.pendown()
    turtle.setheading(-60)  # Set direction for smile
    turtle.circle(7, 120)  # Draw a smile

def main():
    turtle.speed(2)  # Set the speed of drawing
    draw_pod()
    
    # Draw three peas with faces in the pod
    for i in range(3):
        draw_pea(-20 + i * 20, 0)  # Adjust x-coordinate for spacing

    turtle.hideturtle()  # Hide the turtle cursor
    turtle.done()  # Finish the drawing

if __name__ == "__main__":
    main()