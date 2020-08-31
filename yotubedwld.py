from tkinter import *
from pytube import *
from tkinter.filedialog import*
from tkinter.messagebox import*
file_size=0
def StartDownload():
    global file_size
    try:
        url=urlfield.get()
        dbtn.config(text="Please Wait.....")
        dbtn.config(state=DISABLED)
        path_to_save_video = askdirectory()
        if path_to_save_video is None:
            return
        # creating youtube ob with url
        ob = YouTube(url)
        strm = ob.streams.first()
        file_size = strm.filesize
        print(file_size)
        vTitle.config(text=strm.title)
        vTitle.place(x=100,y=650)

        strm.download(path_to_save_video)
        print("done...")
        dbtn.config(text="Start Download")
        dbtn.config(state=NORMAL)
        showinfo("Download Finished","download it succesfully")
        urlfield.delete(0,END)
        vTitle.pack_forget()

    except Exception as e:
        print(e)
        print("some error")
from PIL import ImageTk,Image
root=Tk()
root.title("Download vedios")
root.geometry('1280x720+0+0')
image =Image.open('C:\\Users\\chyas\\PycharmProjects\\youtube\\yout.png')
image1 = ImageTk.PhotoImage(image)
w = image1.width()
h = image1.height()
root.geometry('%dx%d+0+0' % (w,h))
frame = Label(root, image=image1)
frame.place(x=0,y=0)
textenter=Label(frame,text="Enter the Url here  ",font=("verdana",18,'bold'),bg='#df1828',fg='White')
textenter.place(x=50,y=400)
urlfield=Entry(frame,font=("verdana",18),width=50)
urlfield.place(x=50,y=435)
dbtn=Button(frame,text="Start download",font=("verdana",15),fg='white',bg='grey',command=StartDownload,relief=GROOVE,bd=6)
dbtn.place(x=200,y=550)
vTitle=Label(frame, text="video title",font=('Arial Black',10),bg='#df1828',fg='white')
root.mainloop()
