from tkinter import *
import util
global quiz_window_var
global main_window_var
global questions_var
global quiz_var 
global answer_var
global question_status_var


#Created Main Window
def main_wnd_start():
    global quiz_window_var
    quiz_window_var.destroy()
    quiz_window_var = None
    #print(keys_elm.get(1.0, "end-1c"))
    main_window = Tk()
    global main_window_var
    main_window_var = main_window
    main_window.title("Meta Scripts - Quiz System - metascripts.org")
    main_window.configure(background="#232323")
    main_window.geometry("440x460")
    photo = PhotoImage(file = "quiz/metalogo.png")
    main_window.iconphoto(False, photo)

    l_1 = Label(main_window,text="Write question and answer \n(Who is Writer this system = Meta Scripts -Beyonder,1+1 = 2, 2+2 = 4, 255 Red + 255 Blue + 255 Green = White )",background="#232323",fg="#FFFFFF")
    l_1.pack(padx = 10,pady=15,anchor="w")
    
    questions = Text(main_window,height=20,width=110,fg='#7F7FFF',bg="#232323")
    questions.pack(padx = 10,pady=1,anchor="w")
    questions.insert("end-1c", util.last_question)
    global questions_var 
    questions_var = questions


    btn_start_quiz = Button(main_window,width=110,bg="#111111",fg='#7F7FFF',command=quiz_window,text="Start Quiz")
    btn_start_quiz.pack(padx = 10,pady=1,anchor="w")


#Created Quiz Window
def quiz_window():
    util.save_settings()
    global main_window_var
    main_window_var.destroy()
    main_window_var = None

    global quiz_window_var
    quiz_window = Tk()
    quiz_window_var = quiz_window

    quiz_window.title("Meta Scripts - Quiz System - metascripts.org")
    quiz_window.configure(background="#232323")
    quiz_window.geometry("440x250")
    photo = PhotoImage(file = "quiz/metalogo.png")
    quiz_window.iconphoto(False, photo)

    #questions label
    quiz = Label(quiz_window,text="Quiz",background="#232323",fg="#FFFFFF")
    quiz.pack(padx = 10,pady=15,anchor="w")
    global quiz_var
    quiz_var = quiz
    quiz_var.config(text="Selam")



    #answer entry
    answer = Text(quiz_window,height=4,width=110,fg='#7F7FFF',bg="#232323")
    answer.pack(padx = 10,pady=1,anchor="w")
    answer.insert("end-1c", "Answer")
    global answer_var
    answer_var  = answer

    btn_answering = Button(quiz_window,width=110,bg="#111111",fg='#7F7FFF',command=util.replied,text="Send Reply")
    btn_answering.pack(padx = 10,pady=1,anchor="w")

    btn_return_main = Button(quiz_window,width=110,bg="#111111",fg='#7F7FFF',command=main_wnd_start,text="Return Menu")
    btn_return_main.pack(padx = 10,pady=1,anchor="w")

    #questions count true and false count

    question_status = Label(quiz_window,text="   Count = {}\nTrue = {}\nFalse = {}".format(0,0,0),background="#232323",fg="#FFFFFF")
    question_status.pack(padx = 10,pady=15,anchor="w")
    global question_status_var
    question_status_var = question_status
    util.start_quiz()





#print(keys_elm.get(1.0, "end-1c"))
main_window = Tk()
main_window_var = main_window
main_window.title("Meta Scripts - Quiz System - metascripts.org")
main_window.configure(background="#232323")
main_window.geometry("440x460")
photo = PhotoImage(file = "quiz/metalogo.png")
main_window.iconphoto(False, photo)

l_1 = Label(main_window,text="Write question and answer \n(Who is Writer this system = Meta Scripts -Beyonder,1+1 = 2, 2+2 = 4, 255 Red + 255 Blue + 255 Green = White  )",background="#232323",fg="#FFFFFF")
l_1.pack(padx = 10,pady=15,anchor="w")

questions = Text(main_window,height=20,width=110,fg='#7F7FFF',bg="#232323")
questions.pack(padx = 10,pady=1,anchor="w")
questions.insert("end-1c", "Who is Writer this system = Meta Scripts -Beyonder,1+1 = 2, 2+2 = 4, 255 Red + 255 Blue + 255 Green = White")
questions_var = questions



btn = Button(main_window,width=110,bg="#111111",fg='#7F7FFF',command=quiz_window,text="Start Quiz")
btn.pack(padx = 10,pady=1,anchor="w")

main_window.mainloop()