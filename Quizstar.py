import json
import tkinter
from tkinter import *
import random


#    "How many states and union territories in India ?",
#    "How is the PM of India ?",
#    "Which editor is mainly use for c programming?",
#    "Which two states share their capital ?",
#    "Jupter notebooks is which type of editor  ?",
#    "Where the Taj Mahal is located ?",
#    "Which youtuber got 100million subscribers first in the world ?",
#    "Which operating syestem is the best for gaming ?",
#    "Which is the best gaming graphics card ?",
#]

#answers_choice = [
#    ["Jaipur","Delhi","Chandigarh","Goa"],
#    ["Amit Shah","Rahul Gandhi","Narenda Modi","Sonia Gandhi"],
#    ["Sublime Text 3","visual studio code","Turbo C++","atom"],
#    ["Rajasthan and Gurjarat","Telegana and Andhra Pradesh ","Himachal Pradesh and Uttharkand","Chandigarh and Haranya"],
#    ["-","-","offine","online"],
#    ["Cocomelon","T series","Pwediepie","Mrbeast"],
#    ["steamOS","Linux","Windows","macOS",],
#    ["RTX 2080ti","GTX 1660ti","AMD Radeaon 5700xt","AMD Radeaon Vega 86"],
#]

with open('./question.json', encoding="utf8") as f:
    data = json.load(f)

questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [3,1,2,2,3,3,2,1,2,0]

user_answer = []


indexes = []
def gen():
    global indexes
    while(len(indexes) < 5):
        x = random.randint(0,9)
        indexes.append(x)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def showresult(score):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()
    labelimage = Label(
        root,
    )
    labelimage.pack()
    labelresulttext = Label(
        root,
        font = ("Times",20),
    )
    labelresulttext.pack()
    if score >= 20:
        img = PhotoImage(file="great.png")
        labelimage.configure(image = img)
        labelimage.image = img
        labelresulttext.configure(text ="You are Excellent!!")


def calc():
    global indexes,user_answer,answers
    x = 0
    score = 0
    for i in indexes:
        if user_answer[x] == answers[i]:
            score = score + 5
        x += 1
        print(score)
        showresult(score)





ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 5:
        lblQuestion.config(text=questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()





def startquiz():
    global lblQuestion,r1,r2,r3,r4
    lblQuestion = Label(
        root,
        text = questions[indexes[0]],
        font = ("Consolas", 16),
        width = 500,
        justify = "center",
        wraplength = 400,
        background = "#ffffff",
    )
    lblQuestion.pack(pady=(100,30) )

    global radiovar

    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][0],
        font = ("Times",12),
        value = 0,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r1.pack(pady=5)

    r2 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][1],
        font = ("Times",12),
        value = 1,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r2.pack(pady=5)

    r3 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][2],
        font = ("Times",12),
        value = 2,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r3.pack(pady=5)

    r4 = Radiobutton(
        root,
        text = answers_choice[indexes[0]][3],
        font = ("Times",12),
        value = 3,
        variable = radiovar,
        command = selected,
        background = "#ffffff",
    )
    r4.pack(pady=5)

def startIspressed():
    labelimage.destroy()
    labeltext.destroy()
    lblInstruction.destroy()
    lblRule.destroy()
    btnStart.destroy()
    gen()
    startquiz()



root = tkinter.Tk()
root.title("Quizstar")
root.geometry("700x600")
root.config(background="#ffffff")


img1 = PhotoImage(file="TransparentGradHat.png")

labelimage = Label(
    root,
    image = img1,
    background="#ffffff",
)
labelimage.pack(pady=(40,0))

labeltext = Label(
    root,
    text = "Quizstar",
    font = ("Comic sans MS",24,"bold"),
    background = "#ffffff",
)
labeltext.pack(pady=(0))

img2 = PhotoImage(file="StartButton.png")

btnStart = Button(
    root,
    image = img2,
    relief = FLAT,
    border = 0,
    command = startIspressed,
)
btnStart.pack(pady=(10,30))

lblInstruction = Label(
    root,
    text = "Read The Rules And\nClick Start Once You Are ready",
    background = "#ffffff",
    font = ("Times New Roman",14),
    justify = "center",
)
lblInstruction.pack()

lblRule = Label(
    root,
    text = "This Quiz contains 10 Question.\nGive answer of each Question Correctly.\nAnd main rule enjoy the Quiz.\nAlso you will get 20 seconds to solve a question\nOnce you will select a radio button that will be a final.\n hence think before selecting a radio button. ",
    width = "100",
    font = ("Times",20),
    background = "#000000",
    foreground = "#FACA2F",
)
lblRule.pack()



root.mainloop()
