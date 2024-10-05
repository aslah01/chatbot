from tkinter import *
from tkinter import scrolledtext
import nltk
from nltk.chat.util import Chat,reflections

reflections = { 
"i am" : "you are",
 "i was" : "you were",
 "i" : "you",
 "i'm" : "you are",
 "i'd" : "you would", 
"i've" : "you have", 
"i'll" : "you will", 
"my" : "your", 
"you are" : "I am", 
"you were" : "I was", 
"you've" : "I have", 
"you'll" : "I will", 
"your" : "my", 
"yours" : "mine", 
"you" : "me",
 "me" : "you"
 }

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"what is your name ?",
        ["I am a bot as part of a project . you can call me crazy!",]
    ],
    [
        r"how are you ?",
        ["I'm doing good,How about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"I am fine",
        ["Great to hear that, How can I help you?",]
    ],
    [
        r"i'm (.*)  good",
        ["Nice to hear that","How can I help you?:)",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program , dude Seriously you are asking me this?",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    
 
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
    
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
   
    
    
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
    ]
]


def chat():
	user_text=entry.get()
	if user_text:
		
		text_area.insert(END, f"you> {user_text}\n")
		chat = Chat(pairs, reflections)
		bot_response = f"bot> {chat.respond(user_text)}"
		text_area.insert(END,f"{bot_response}\n")
		entry.delete(0, END)    


#For creating GUI
root = Tk()
root.title("Chat Bot")
root.geometry("600x400")


text_area =scrolledtext.ScrolledText(root,wrap = WORD,width = 55,height = 15, font = ("Times New Roman",15))
text_area.pack(padx=10,pady=10)
text_area.insert(INSERT,"Hi! I am a chatbot  for your service")

frame=Frame(root)
frame.pack(pady=10)

entry=Entry(frame,width =40)
entry.pack(side=LEFT)

button = Button(frame, text="SEND",command= chat)
button.pack(side=LEFT,padx=2)

root.mainloop()
