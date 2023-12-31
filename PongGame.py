import turtle

wn = turtle.Screen()
wn.title("Pong by PythonianPrince")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A  -   LEFT
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(5, 1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B  -   RIGHT
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(5, 1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(1, 1)
ball.penup()
ball.goto(0, 0)
ball.dx = 0.08
ball.dy = -0.08

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: 0  PlayerB: 0", align="center", font=("Courier", 24, "bold"))

# Function
def paddle_a_up():
    if paddle_a.ycor() >= 250:
        paddle_a.sety(250)
    else:
        y = paddle_a.ycor()
        y += 40
        paddle_a.sety(y)


def paddle_a_down():
    if paddle_a.ycor() <= -250:
        paddle_a.sety(-250)
    else:
        y = paddle_a.ycor()
        y -= 40
        paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() >= 250:
        paddle_b.sety(250)
    else:
        y = paddle_b.ycor()
        y += 40
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() <= -250:
        paddle_b.sety(-250)
    else:
        y = paddle_b.ycor()
        y -= 40
        paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#   Main Game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.dy *= -1

    if ball.xcor() > 415:
        ball.goto(0, 0)
        ball.dx = -0.08
        ball.dy = 0.08
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  PlayerB: {score_b}", align="center", font=("Courier", 24, "bold"))

    
    if ball.xcor() < -415:
        ball.goto(0, 0)
        ball.dx = 0.08
        ball.dy = -0.08
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  PlayerB: {score_b}", align="center", font=("Courier", 24, "bold"))


    # Paddle and ball collision checking
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1.10
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1.10