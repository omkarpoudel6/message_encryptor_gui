from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from stegano import lsb


def browse():
    global filename
    # filename=filedialog.askopenfile(initialdir="/r",title="Select File",filetypes=("image files",".jpg"))
    filename = filedialog.askopenfilename(initialdir="/root/Desktop",filetypes=(("png files","*.png"),("jpg files","*.jpg"),("jpeg files","*.jpeg")))
    path = filename

def final_encryption(path,message):
    p=path
    m=message
    secret_message=lsb.hide(p,m)
    secret_message.save("/root/Desktop/images/encrypted_images/secret_message.png")
    messagebox.showinfo("Saved","Encryped file stored in /root/Desktop/images/encrypted_images")


def encryption(filename):

    enc=Toplevel(root)
    enc.geometry("800x400")
    enc.config(background="black")

    path=StringVar()
    message=StringVar()
    f_name=StringVar()
    path=filename

    lbl1 = Label(enc, text=" ", background="black")
    lbl1.pack(fill=X)

    lbl2 = Label(enc, text="Encrypt your Message", background="black", fg="red", font="TkFixedFont")
    lbl2.pack(fill=X)

    lbl3 = Label(enc, text=" ", background="black")
    lbl3.pack(fill=X)

    lbl4 = Label(enc, text="Image Path", background="black",fg="red",font="TkFixedFont")
    lbl4.pack(fill=X)

    lbl5 = Label(enc, text=" ", background="black")
    lbl5.pack(fill=X)

    pathlabel=Label(enc,text=filename,background="black",fg="red",font="TkFixedFont")
    pathlabel.pack(fill=X)

    lbl6 = Label(enc, text=" ", background="black")
    lbl6.pack(fill=X)

    lbl7 = Label(enc, text="Enter your message below ", background="black", fg="red", font="TkFixedFont")
    lbl7.pack(fill=X)

    lbl8 = Label(enc, text=" ", background="black")
    lbl8.pack(fill=X)

    ent2 = Entry(enc, textvariable=message, background="black", fg="red", font="TkFixedFont")
    ent2.pack(fill=X)

    lbl9 = Label(enc, text=" ", background="black")
    lbl9.pack(fill=X)

    lbl11 = Label(enc, text=" ", background="black")
    lbl11.pack(fill=X)

    lbl12 = Label(enc, text=" ", background="black")
    lbl12.pack(fill=X)

    but2 = Button(enc, text="Encrypt", background="black", font="TkFixedFont", fg="red",command=lambda:final_encryption(filename,message.get()))
    but2.pack()

    enc.mainloop()


def decryption(filename):
    dec_message = lsb.reveal(filename)
    decmessage = dec_message
    dec = Toplevel(root)

    dec.geometry("800x300")
    dec.config(background="black")

    path = StringVar()
    message = StringVar()
    message=decmessage

    lbl1 = Label(dec, text=" ", background="black")
    lbl1.pack(fill=X)

    lbl2 = Label(dec, text="Your Message", background="black", fg="green", font="TkFixedFont")
    lbl2.pack(fill=X)

    lbl3 = Label(dec, text=" ", background="black")
    lbl3.pack(fill=X)

    lbl4 = Label(dec, text=" ", background="black")
    lbl4.pack(fill=X)

    pathdec=Label(dec,text="Image path",background="black",fg="green",font="TkFixedFont")
    pathdec.pack(fill=X)

    lbl5 = Label(dec, text=" ", background="black")
    lbl5.pack(fill=X)

    pathlbl=Label(dec,text=filename,background="black",fg="green",font="TkFixedFont")
    pathlbl.pack(fill=X)

    lbl6 = Label(dec, text=" ", background="black")
    lbl6.pack(fill=X)

    lbl7 = Label(dec, text="Extracted message from image", background="black", fg="green", font="TkFixedFont")
    lbl7.pack(fill=X)

    lbl8 = Label(dec, text=" ", background="black")
    lbl8.pack(fill=X)


    lbl9 = Label(dec, text=message, background="black",fg="white")
    lbl9.pack(fill=X)


    dec.mainloop()


root=Tk()
root.geometry("600x500")
root.config(background="black")

path=StringVar()

lbl1=Label(root,text=" ",background="black")
lbl1.pack(fill=X)

lbl2=Label(root,text=" ",background="black")
lbl2.pack(fill=X)

lbl3=Label(root,text=" ",background="black")
lbl3.pack(fill=X)

lbl4=Label(root,text=" ",background="black")
lbl4.pack(fill=X)


lbl5=Label(root,textvariable=path,background="black",fg="white",font="Monospaced")
lbl5.pack(fill=X)

lbl6=Label(root,text=" ",background="black")
lbl6.pack(fill=X)

but0=Button(root,text="Browse Image",background="black",fg="white",font="TkFixedFont",command=browse)
but0.pack()

lbl7=Label(root,text=" ",background="black")
lbl7.pack(fill=X)

lbl8=Label(root,text=" ",background="black")
lbl8.pack(fill=X)

but1=Button(root,text="Encryption",background="black",fg="white",font="TkFixedFont", command=lambda:encryption(filename))
but1.pack(fill=X)

lbl9=Label(root,text=" ",background="black")
lbl9.pack(fill=X)

lbl10=Label(root,text=" ",background="black")
lbl10.pack(fill=X)

but2=Button(root,text="Decryption",background="black",fg="white",font="TkFixedFont", command=lambda:decryption(filename))
but2.pack(fill=X)
root.mainloop()
