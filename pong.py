import turtle as t


playerA = 0
playerB = 0

window = t.Screen()
window.title("Pong")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("green")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("green")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.5
ballydirection = 0.5

pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=('Arial', 24, 'normal'))


def leftpaddleup():
    y = leftpaddle.ycor()
    y += 15
    leftpaddle.sety(y)


def leftpaddledown():
    y = leftpaddle.ycor()
    y -= 15
    leftpaddle.sety(y)


def rightpaddleup():
    y = rightpaddle.ycor()
    y += 15
    rightpaddle.sety(y)


def rightpaddledown():
    y = rightpaddle.ycor()
    y -= 15
    rightpaddle.sety(y)


window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:

    window.update()
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerA += 1
        pen.clear()
        pen.write("player A:{}    player B:{}".format(playerA, playerB), align='center', font=('Arial', 24, 'normal'))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection = ballxdirection * -1
        playerB += 1
        pen.clear()
        pen.write("player A:{}    player B:{}".format(playerA, playerB), align='center', font=('Arial', 24, 'normal'))

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ballxdirection *= -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ballxdirection *= -1
