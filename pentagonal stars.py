import turtle

t = turtle.Turtle()
t.getscreen().bgcolor('black')
turtle.tracer(0, 0)
t.up()
t.goto(0, 40)
t.pd()
t.color('white')


def stars(size):
	if size <= 10:
		return
	else:
		t.begin_fill()
		t.fillcolor('yellow')
		for i in range(5):
			t.fd(size)
			stars(size/2)
			t.rt(144)
			t.end_fill()


stars(300)
turtle.done()
