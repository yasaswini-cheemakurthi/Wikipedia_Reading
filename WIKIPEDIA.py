from tkinter import *
import wikipedia
from PIL import Image,ImageTk
from tkinter.messagebox import*
def show():
    ask=askquestion("confirm","Proceed To Read Wikipedia")
    try:
        if ask=='yes':
            text.insert(INSERT,wikipedia.summary(get_qts.get()))
        else:
            exit()

    except Exception as ConnectionError:
        showerror('error','some problem in connection\n         or\ncheck the spelling ')

def out():
    askto=askquestion("confirm","Want to exit!!!\nContinue Search")
    if askto=='yes':
        exit()
    else:
        pass
root=Tk()
root.title('Wikipedia ')
root.geometry("900x540+100+100")
root.maxsize(width=900, height=540)
root.minsize(width=900, height=540)
img=Image.open('stat.png')
img1=ImageTk.PhotoImage(img)
im=Image.open('wik2.png')
im1=ImageTk.PhotoImage(im)
pic=Label(root,image=img1,width=200)
pic.place(x=0,y=0)
frame=Label(root,image=im1)
frame.place(x=201,y=0)
qtn=Label(frame,text='Search Here :)',fg='grey',bg='white',font=('Bahnschrift'))
qtn.place(x=10,y=0)
get_qts=Entry(frame,bd=3,width=30,font=('Cambria',10))
get_qts.place(x=10,y=40)
submit=Button(frame,text='Search',fg='white',relief=GROOVE,bd=2,command=show,width=15,height=1,bg='#0aa395')
submit.place(x=300,y=30)
out=Button(frame,text='Exit',fg='white',relief=GROOVE,bd=2,command=out,width=15,height=1,bg='#0aa395')
out.place(x=500,y=30)
text=Text(root,bg='white',relief=GROOVE,bd=7,fg='#aa9172',font=('Arial'))
text.place(x=201,y=101,height=439,width=698)
root.mainloop()
