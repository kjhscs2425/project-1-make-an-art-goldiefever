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
    f(pea_radius/3)
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
    for k in range(1,3):
        r(right_angle)
        f(pea_radius/3)
    r(right_angle)

def draw_soureyes():
    up()
    l(90)
    f(10)
    r(135)
    down()
    f(8)
    l(90)
    f(8)
    up()
    r(135)
    f(20)
    down()
    r(135)
    f(8)
    l(90)
    f(8)
    up()
    r(135)
    f(10)
    r(90)

def draw_neutralmouth(size):
    up()
    b(6.25)
    down()
    l(90)
    f(size/2)
    b(size)
    f(size/2)
    up()
    r(90)
    f(6.25)

def draw_smile(size):
    up()
    for j in range(1,3):
        l(right_angle)
        f(size/(j*3))
    down()
    turtle.circle(size/3, 180)
    up()
    l(90)
    f(size/3)
    r(90)

def draw_frown(size):
    up()
    for j in range(2):
        r(right_angle)
        f(size/(3-j))
    l(180)
    down()
    turtle.circle(size/3, 180)
    up()
    l(90)
    f(size/3)
    l(90)
    f((size/3)+(size/(j*3)))

def draw_smileyface():
    up()
    draw_eyes()
    draw_smile(pea_radius*(2/3))

draw_smileyface()

up()
turtle.setheading((right_angle*2)-10)
f(pod_length/4)
r(90)

draw_soureyes()
draw_neutralmouth(12.5)

up()
turtle.setheading((right_angle*2)-10)
f(pod_length/4)
r(90)

draw_eyes()
draw_frown(pea_radius*(2/3))

up()
turtle.goto(pea_radius/2,0)
turtle.setheading(10)
f(pod_length/4)
r(right_angle)
f(25)
l(right_angle*2)

draw_soureyes()
draw_smile(pea_radius*(2/3))

up()
turtle.setheading(10)
f(pod_length/4)
l(90)

draw_eyes()
draw_neutralmouth(12.5)

up()
turtle.setheading(10)
f(pod_length/4)
l(90)

draw_soureyes()
draw_frown(pea_radius*(2/3))

up()
turtle.goto(0,0)

turtle.update()

turtle.done()