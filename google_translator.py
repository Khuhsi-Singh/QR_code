from tkinter import *
from tkinter import ttk
# from googletrans import Translator,LANGUAGES
from deep_translator import GoogleTranslator
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Korean": "ko",
    "Russian": "ru",
    "Arabic": "ar",
}

# def change(text="type",src="en",dest="hi"):
#     text1 = text
#     src1 = src
#     dest1 = dest
#     trans = GoogleTranslator()
#     trans1 = trans.translate(text,src=src1,dest=dest1)
#     return trans1

# def data():
#     s = comb_sor.get()
#     d = comb_dest.get()
#     msg = Sor_txt.get(1.0,END)
#     textget = change(text=msg,src=s,dest=d)
#     dest_txt.delete(1.0,END)
#     dest_txt.insert(END,textget)
def change(text="type", src="en", dest="hi"):
    translator = GoogleTranslator(source=src, target=dest)  # ✅ Correctly initialize with source & target
    translation = translator.translate(text)  # ✅ No need for src= or dest= inside translate()
    return translation

def data():
    s = comb_sor.get()  # ✅ Get source language
    d = comb_dest.get()  # ✅ Get destination language
    msg = Sor_txt.get(1.0, END).strip()  # ✅ Remove extra spaces/newlines

    textget = change(text=msg, src=s, dest=d)  # ✅ Call function correctly
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)

root = Tk()
root.title("Translator")
root.geometry("500x800")
root.config(bg="pink")
lab_txt=Label(root,text="Translator",font=("Time New Roman",40,"bold"),bg="pink")
lab_txt.place(x=100,y=40, height=50,width=300)

frame = Frame(root).pack(side=BOTTOM)

lab_txt=Label(root,text="Source Text",font=("Time New Roman",20,"bold"),bg="pink",fg ="black")
lab_txt.place(x=100,y=100, height=20,width=300)

Sor_txt = Text(frame,font=("Time New Roman",20,"bold"),bg="pink",wrap = WORD)
Sor_txt.place(x=10,y=130, height=150,width=480)
list_text = list(GoogleTranslator().get_supported_languages())
comb_sor = ttk.Combobox(frame,value=list_text)
comb_sor.place(x=10,y=300,height=40, width=150)
comb_sor.set("English")

button_change =Button(frame,text = "Translate",relief=RAISED, command =data)
button_change.place(x=170, y= 300, height =40, width=150)

comb_dest = ttk.Combobox(frame,value=list_text)
comb_dest.place(x=330,y=300,height=40, width=150)
comb_dest.set("English")

lab_txt=Label(root,text="Dest Text",font=("Time New Roman",20,"bold"),bg="pink",fg ="black")
lab_txt.place(x=100,y=360, height=20,width=300)

dest_txt = Text(frame,font=("Time New Roman",20,"bold"),bg="pink",wrap = WORD)
dest_txt.place(x=10,y=400, height=150,width=480)

root.mainloop()