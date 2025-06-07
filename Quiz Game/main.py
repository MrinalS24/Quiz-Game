import pgzrun

WIDTH = 870
HEIGHT = 650

TITLE = "Quiz Game"

marquee_box = Rect(0,0,1050,80)
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

question_index = 0
question_count = 0
questions = []
score = 0
game_over = False

marquee_message = ""



answers_boxes = [answer_box1, answer_box2, answer_box3, answer_box4]

def draw():
    global marquee_message, question
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

    marquee_message =f"Welcome to Quiz Game. You are at question {question_index} out of {question_count}"
    screen.draw.textbox(marquee_message, marquee_box, color = "white")

    screen.draw.textbox(question[0].strip(), question_box, color = "black")


def marquee_effect():
    marquee_box.x -= 1
    if marquee_box.right < 0:
        marquee_box.left = WIDTH


def update():
    marquee_effect()



def read_question_file():
    global questions, question_count
    q_file = open("questions.txt", "r")
    for row in q_file:
        questions.append(row)
        question_count += 1


def read_question():
    global question_index
    question_index += 1
    question_option = questions.pop(0).split(",")
    return(question_option)







read_question_file()


question = read_question()


























pgzrun.go()




#strip removes /n and spaces before and after the string