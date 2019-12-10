from tkinter import *

def encryption():
    enc=Toplevel(root)
    enc.geometry("400x300")
    enc.config(background="black")

    path=StringVar()
    message=StringVar()

    lbl1 = Label(enc, text=" ", background="black")
    lbl1.pack(fill=X)

    lbl2 = Label(enc, text="Encrypt your Message", background="black", fg="red", font="TkFixedFont")
    lbl2.pack(fill=X)

root=Tk()
root.geometry("600x500")
root.config(background="black")

lbl1=Label(root,text=" ",background="black")
lbl1.pack(fill=X)

lbl2=Label(root,text=" ",background="black")
lbl2.pack(fill=X)

lbl3=Label(root,text=" ",background="black")
lbl3.pack(fill=X)

lbl4=Label(root,text=" ",background="black")
lbl4.pack(fill=X)

lbl5=Label(root,text=" ",background="black")
lbl5.pack(fill=X)

lbl6=Label(root,text=" ",background="black")
lbl6.pack(fill=X)

lbl7=Label(root,text=" ",background="black")
lbl7.pack(fill=X)

lbl8=Label(root,text=" ",background="black")
lbl8.pack(fill=X)

but1=Button(root,text="Encryption",background="black",fg="white",font="TkFixedFont", command=encryption)
but1.pack(fill=X)

lbl9=Label(root,text=" ",background="black")
lbl9.pack(fill=X)

lbl10=Label(root,text=" ",background="black")
lbl10.pack(fill=X)

but2=Button(root,text="Decryption",background="black",fg="white",font="TkFixedFont", command=decryption)
but2.pack(fill=X)

root.mainloop()