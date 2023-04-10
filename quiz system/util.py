import gui
import random
import re

#Global Arg
global questions_list
global select_answer
global question_count
global question_true
global question_false
global last_question


# ran = random.randint(0,len(questions_list)-1)

# print(questions_list[ran])

def save_settings():
    question_and_answer = gui.questions_var.get(1.0, "end-1c")
    global last_question
    last_question = question_and_answer
    value = question_and_answer.split(',')
    global  questions_list
    questions_list = []
    #counts restart
    global question_count
    global question_true
    global question_false
    question_count = 0
    question_true = 0
    question_false = 0


    for v in value:
        try:
            quiz, answer = v.split("=")
            questions_list.append([ quiz,re.sub(r'^\s', '', answer.lower())])
        except:
            print("Hatalı işlem")



#Random question
def random_question():
    global questions_list 
    rnd = random.randint(0,len(questions_list)-1)

    global select_answer
    global select_question

    select_question = questions_list[rnd][0]
    select_answer = questions_list[rnd][1]

    return questions_list[rnd][0],questions_list[rnd][1]


#start quiz function
def start_quiz():
    question, answer = random_question()
    global select_answer
    select_answer = answer
    gui.quiz_var.config(text=question)

#replied
def replied():
    new_answer = gui.answer_var.get(1.0, "end-1c")
    gui.answer_var.delete('1.0', "2.0")
    global question_count
    question_count += 1

    if new_answer.lower() == select_answer:
        global question_true
        question_true += 1
    else:
        global question_false
        question_false += 1
    type_question_count()
    start_quiz()
    

#type question count
def type_question_count():
    gui.question_status_var.config(text="   Count = {}\nTrue = {}\nFalse = {}".format(question_count,question_true,question_false))













