import pgzrun

WIDTH = 900
HEIGHT = 700

time_left = 10
question_index = 0
question_count = 0
questions = []
options_index = 0
score = 0
game_over = False
marquee_message = ""







marquee_box = Rect(0, 0, 1500, 75)
question_box = Rect(0, 0, 725, 100)
timer_box = Rect(0, 0, 100, 100)
answer_box1 = Rect(0, 0, 350, 150)
answer_box2 = Rect(0, 0, 350, 150)
answer_box3 = Rect(0, 0, 350, 150)
answer_box4 = Rect(0, 0, 350, 150)
skip_box = Rect(0, 0, 100, 300)


marquee_box.move_ip(0, 25)
question_box.move_ip(25, 125)
timer_box.move_ip(775, 125)
answer_box1.move_ip(25, 275)
answer_box2.move_ip(400, 275)
answer_box3.move_ip(25, 475)
answer_box4.move_ip(400, 475)
skip_box.move_ip(775, 300)


def draw():
    global marquee_message
    screen.clear()
    screen.fill(color = "black")
    screen.draw.filled_rect(marquee_box, (186, 255, 201))
    screen.draw.filled_rect(question_box, (224, 176, 255))
    screen.draw.filled_rect(timer_box, (186, 225, 255))
    screen.draw.filled_rect(answer_box1, (255, 179, 186))
    screen.draw.filled_rect(answer_box2, (255, 197, 208))
    screen.draw.filled_rect(answer_box3, (255, 197, 208))
    screen.draw.filled_rect(answer_box4, (255, 179, 186))
    screen.draw.filled_rect(skip_box, (255, 255, 186))

    screen.draw.textbox(str(time_left), timer_box, color = "white")
    screen.draw.textbox("Skip", skip_box, color = "white")

    marquee_message = f"Welcome to A Swiftie Quiz. You are at question {question_index} out of question {question_count}"
    screen.draw.textbox(str(marquee_message), marquee_box, color = "black")

    screen.draw.textbox(question[0].strip(), question_box, color = "white")

    screen.draw.textbox(option_1, answer_box1, color = "white")
    screen.draw.textbox(option_2, answer_box2, color = "white")
    screen.draw.textbox(option_3, answer_box3, color = "white")
    screen.draw.textbox(option_4, answer_box4, color = "white")


def marquee_effect():
    marquee_box.x -= 2
    if marquee_box.right ==0:
        marquee_box.left = WIDTH


def update():
    marquee_effect()


def read_question_file():
    global questions, question_count
    q_file = open("questions.txt", "r")
    for row in q_file:
        questions.append(row)
        question_count += 1


def read_questions():
    global question_index
    question_index += 1
    q = questions.pop(0).split(",")
    return q


read_question_file()

question = read_questions()

print(question)


def read_options():
    global options_index, option_1, option_2, option_3, option_4
    options_index += 1
    option_1 = question[1]
    option_2 = question[2]
    option_3 = question[3]
    option_4 = question[4]

read_options()




















pgzrun.go()