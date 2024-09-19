import turtle

turtle.tracer(0,0)

pea_radius = 25
pod_length = 200
right_angle = 90

f = turtle.forward
b = turtle.backward
r = turtle.right
l = turtle.left

up = turtle.up
down = turtle.down

turtle.pensize(1.5)

turtle.shape("turtle")

up()
b(pea_radius/2)
down()
l((right_angle*2)-10)

def draw_peapod():
     
     for pea in range(3):
        f(pod_length/4)
        turtle.circle(pea_radius)
     f(pod_length/4)
     l(111)
     turtle.circle(107,138)

draw_peapod()

up()
turtle.goto(((pea_radius/2)+196.9615506),(34.72963553))
turtle.setheading((right_angle*2)+10)
down()

draw_peapod()

up()
turtle.goto(-pea_radius/2,0)
turtle.setheading((right_angle*2)-10)
f(pod_length/4)
l(right_angle)
f(25)
r(right_angle*2)

def draw_eyes():
    up()
    f(pea_radius/2)
    l(right_angle)
    f(pea_radius/3)
    down()
    turtle.dot(2.5)
    up()
    r(right_angle*2)
    f(pea_radius*(2/3))
    down()
    turtle.dot(2.5)
    up()
    r(right_angle)
    f(pea_radius/2)
    r(right_angle)
    f(pea_radius/3)
    r(right_angle)

def draw_smile(size):
    l(right_angle)
    f(size/2)
    down()
    turtle.circle(-size/3, 180)

draw_eyes()

draw_smile(pea_radius)

turtle.update()

turtle.done()