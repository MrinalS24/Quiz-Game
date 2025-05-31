import pgzrun

WIDTH = 870
HEIGHT = 650

TITLE = "Quiz Game"

marquee_box = Rect(0,0,880,80)
question_box = Rect(0,0,650,150)
timer_box = Rect(0,0, 150, 150)
answer_box1 = Rect(0,0, 300, 150)
answer_box2 = Rect(0,0, 300, 150)
answer_box3 = Rect(0,0, 300, 150)
answer_box4 = Rect(0,0, 300, 150)
skip_box = Rect(0,0,150,330)

question_box.move_ip(20, 100)
timer_box.move_ip(700, 100)
answer_box1.move_ip(20, 270)
answer_box2.move_ip(370, 270)
answer_box3.move_ip(20, 450)
answer_box4.move_ip(370, 450)
skip_box.move_ip(700,270)

time_left = 10

answers_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    screen.clear()
    screen.fill(color= "black")
    screen.draw.filled_rect(marquee_box, "black")
    screen.draw.filled_rect(question_box, "yellow")
    screen.draw.filled_rect(timer_box, "orange")
    screen.draw.filled_rect(skip_box, "blue")
    for i in answers_boxes:
        screen.draw.filled_rect(i, "pink")
    screen.draw.textbox(str(time_left), timer_box, color = "white")
    screen.draw.textbox("Skip", skip_box, color = "white")
























pgzrun.go()