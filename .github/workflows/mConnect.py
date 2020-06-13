from tkinter import *
#import numpy as n
#import cv2 as cv
#import requests as r
import pyttsx3

#created by Morphine
engine = pyttsx3.init()
#creating screen
root = Tk()
root.geometry("500x400+400+90")
root.title("mConnect")
root.resizable(0,0)
root.configure(background="powder blue")



def version():
    root = Tk()
    root.title("Version")
    root.geometry("400x50")
    root.config(bg="purple")
    li = Label(root,text="45.01.5",font=("san serif",30,"bold"),bg="purple",fg="white")
    li.pack()
def about_bar():
    root = Tk()
    root.title("About")
    root.geometry("1000x100")
    root.config(bg="purple")
    li = Label(root,text="This software was developed by gideoniceboy in 2020.",font=("san serif",20,"bold"),bg="purple",fg="white")
    li.pack()
    lj = Label(root,text="For more feeds or updates based on this software visit http://giarts.ml.",font=("san serif",20,"bold"),bg="purple",fg="white")
    lj.pack()
def turk():
    root.config(bg="#33FF33")
    e.config(bg="#0F0F0F", fg="#33FF33",insertbackground="#33FF33")
    btn1.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    btn.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    btn3.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    f.config(bg="indigo")
    c.config(bg="#33FF33")
    c1.config(bg="#33FF33")
    l1.config(bg="#33FF33",fg="indigo")
    l2.config(bg="#33FF33",fg="indigo")
    l3.config(bg="indigo",fg="white")
def default():
    root.config(bg="powder blue")
    e.config(bg="powder blue", fg="blue",insertbackground="#33FF33")
    btn1.config(bg="steel Blue", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    btn.config(bg="steel Blue", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    btn3.config(bg="steel Blue", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    f.config(bg="steel Blue")
    c.config(bg="powder blue")
    c1.config(bg="powder blue")
    l1.config(bg="powder blue",fg="white")
    l2.config(bg="steel Blue",fg="white")
    l3.config(bg="steel Blue",fg="white")
def hacker_theme():
    root.config(bg="#0F0F0F")
    e.config(bg="#0F0F0F", fg="#33FF33",insertbackground="#33FF33")
    btn1.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    btn.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    btn3.config(bg="#0F0F0F", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    f.config(bg="#0F0F0F")
    c.config(bg="#0F0F0F")
    c1.config(bg="#0F0F0F")
    l1.config(bg="#0F0F0F",fg="#FFFFFF")
    l2.config(bg="#0F0F0F",fg="#FFFFFF")
    l3.config(bg="#0F0F0F",fg="#FFFFFF")
    
def morphix():
    root.config(bg="indigo")
    e.config(bg="indigo", fg="violet",insertbackground="indigo")
    btn1.config(bg="indigo", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    btn.config(bg="indigo", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    btn3.config(bg="indigo", fg="#FFFFFF", activebackground="#0F0F0F", activeforeground="#FFFFFF")
    f.config(bg="purple")
    c.config(bg="purple")
    c1.config(bg="purple")
    l1.config(bg="indigo",fg="#FFFFFF")
    l2.config(bg="purple",fg="#FFFFFF")
    l3.config(bg="purple",fg="#FFFFFF")

#menu bar
menu_bar = Menu(root,tearoff=0)
file_menu = Menu(menu_bar,tearoff=0)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=exit)
menu_bar.add_cascade(label="File",menu=file_menu)
#configure
settings = Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Configure",menu=settings)

#about
about = Menu(menu_bar,tearoff=0)
about.add_command(label="Version",command=version)
about.add_command(label="About",command=about_bar)
menu_bar.add_cascade(label="Help",menu=about)

#Themes 1. hacker theme
hacker = Menu(menu_bar,tearoff=0)
hacker.add_command(label="Morphix",command=morphix)
hacker.add_command(label="Hacker",command=hacker_theme)
hacker.add_command(label="Turk",command=turk)
hacker.add_command(label="Default",command=default)
settings.add_cascade(label="Theme",menu=hacker)




root.config(menu=menu_bar)
#function
def onclick():
    #ip="http://"+str(e.get())+"/shot.jpg"

    running = True
    #while running:
        #btn.config(text="Connect")
        #img = r.get(ip)
        #video = n.array(bytearray(img.content),dtype = n.uint8)
        #render = cv.imdecode(video,-1)
        #if running:
         #   cv.imshow('Connected',render)
          #  btn.config(text="Connected")
        #else:
         #   cv.imshow('Lost connections',render)
          #  btn.config(text="Disconnected")
        #if(cv.waitKey(1) and 0xFF == ord('q')):
            
         #   break
def how():
    #creating screen
    root = Tk()
    root.geometry("650x150+300+10")
    root.title("Help")
    root.resizable(0,0)
    root.configure(background="powder blue")

    f = Frame(root,width=800,height=100,bg="steel Blue")
    f.place(relwidth=0.85,relheight=0.85,relx=0.1,rely=0.1)

    li=Label(f,text="First: download and install an ip webcam app on your mobile.",bg="steel Blue",fg="white",font=("arial",10,"bold"))
    li.grid(row=1,column=0)
    
    lj=Label(f,text="Second: connet your mobile hotspot to pc.",bg="steel Blue",fg="white",font=("arial",10,"bold"))
    lj.grid(row=2,column=0)
    
    lk=Label(f,text="Third: Open ip webcam app and press 'Start server'.",bg="steel Blue",fg="white",font=("arial",10,"bold"))
    lk.grid(row=3,column=0)

    ll=Label(f,text="Fourth: Enter the ip address you see on your mobile and enter it on mConnect.",bg="steel Blue",fg="white",font=("arial",10,"bold")) 
    ll.grid(row=4,column=0)

    lm=Label(f,text="Last: press connect button and enjoy.",bg="steel Blue",fg="white",font=("arial",10,"bold"))
    lm.grid(row=5,column=0)
    
    #engine.say("First: download and install an ip webcam app on your mobile. Second: connet your mobile hotspot to pc. Third: Open ip webcam app and press 'Start server'. Fourth: Enter the ip address you see on your mobile and enter it on mConnect. Last: press connect button and enjoy. Check out the tips, Powered by Morphine")
    #engine.runAndWait()
    root.config(menu=menu_bar)






#canvas
c = Canvas(root,width=500,height=500,bg="powder blue")
c.pack()
c1 = Canvas(root,width=500,height=500,bg="powder blue")
c1.pack()

#bottom frame
f = Frame(root,width=500,height=100,bg="steel Blue")
f.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

l1=Label(c,text="Smart Android Webcam Connect",bg="powder blue",fg="white",font=("arial",10,"bold"))
l1.grid(row=0,column=0)

l2=Label(f,text="Powered by @morphine",bg="steel Blue",fg="white",font=("arial",10,"italic"))
l2.pack(side=BOTTOM)



btn = Button(f,text="Connect",fg="white",bg="steel Blue",padx=70,pady=70,command=onclick,font=("arial",10,"bold"))
btn.place(relx=0.25,rely=0.25)

btn1 = Button(f,text="Exit the Program",fg="white",bg="steel Blue",padx=10,pady=10,command=exit,font=("arial",6,"bold"))
btn1.place(relx=0.75,rely=0.85)

btn3 = Button(f,text="How Do i Connect?",fg="white",bg="steel Blue",padx=10,pady=10,command=how,font=("arial",6,"bold"))
btn3.place(relx=0.02,rely=0.85)

e = Entry(f,bd=10,bg="powder blue",fg="blue",font=("arial",10,"bold"))
e.pack()

l3=Label(f,text="Enter Your IP address here",bg="steel Blue",fg="white",font=("arial",10,"bold"))
l3.pack()

root.mainloop()


