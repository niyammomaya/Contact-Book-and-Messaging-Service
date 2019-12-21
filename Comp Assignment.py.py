
from tkinter import *
from tkinter import messagebox
def search():
    name=d.get()
    myfile=open('contact.txt','rt+')
    t=myfile.read().split('\n')
    myfile.close()
    for i in t:
            if i.split()!=[]:
                if i.split()[0]==name:
                    text = Text(python)
                    text.insert(INSERT,"Name: "+i.split()[0]+"\nPhone number: "+i.split()[1]+"\nAddress: "+i.split()[2]+"\nDOB"+i.split()[3])
                    text.insert(END,"\n")
                    text.config(height=10,width=20)
                    text.place(x=600,y=120)
                    break
                else:
                    messagebox.showerror("Error","Contact does not exist")

def mess():
    boo=True
    name=entry_67.get()
    myfile=open('contact.txt','rt+')
    t=myfile.read().split('\n')
    myfile.close()
    count=0
    if t==['']:
        boo=False
    if boo==True:
        for i in t:
            if i.split()!=[]:
               if name!=i.split()[0]:
                    count+=1
               else:
                   break
    if count==len(t):
        messagebox.showerror("Error","contact does not exist")        
    else:
        e=entry_4.get()
        file=open('message.txt','a+')
        file.write(name+" ")
        file.write(e+"\n")
        file.close()
        file=open('message.txt','rt+')
        t=file.read().split('\n')
        file.close()
        s=''
        for i in t:
            if i.split()!=[]:
                if i.split()[0]==name:
                    s=s+i.split()[1]+'\n'
        text = Text(python)
        text.insert(INSERT,s )
        text.insert(END,"\n")
        text.config(height=10,width=20)
        text.place(x=0,y=400)
    
def save_info():
    count=0
    boo=True
    nam=name.get()
    num=number.get()
    add=address.get()
   
    dd=day.get()
    mm=month.get()
    yy=year.get()
    file=open('contact.txt','a+')
    file.close()
    myfile=open('contact.txt',"rt+")
    t=myfile.read().split('\n')
    myfile.close()
    if t==['']:
        boo=False
    if boo==True:
        for i in t:
            if i.split()!=[]:
               if nam==i.split()[0]:
                    messagebox.showerror("Error!!","Contact already exists cant write")
                    count=1
                    break
    if count==0:
        file=open('contact.txt','a+')
        file.write(nam+" ")
        file.write(num+" ")
        file.write(add+" ")
        file.write(dd+"/")
        file.write(mm+"/")
        file.write(yy+"\n")
        file.close()
        messagebox.showinfo("DONE!","user "+nam+" has been saved successfully")
python=Tk()
python.geometry('1000x2000')
python.title('Contact-Messaging Service')
python.configure(background='Grey')


name=StringVar()
number=StringVar()
address=StringVar()
message=StringVar()
day=StringVar()
month=StringVar()
year=StringVar()


label_1=Label(python,text="Enter your name   ")
entry_1=Entry(python,textvariable=name)
label_2=Label(python,text="Enter your phone number")
entry_2=Entry(python,textvariable=number)
label_3=Label(python,text="Enter your address ")
entry_3=Entry(python,textvariable=address)

label_5=Label(python,text="Date of Birth")
label_5.place(x=10,y=120)
label_6=Label(python,text="day")
label_6.place(x=100,y=120)
entry_6=Entry(python,textvariable=day,width=5)
entry_6.place(x=130,y=120)
label_7=Label(python,text="month")
label_7.place(x=160,y=120)
entry_7=Entry(python,textvariable=month,width=5)
entry_7.place(x=210,y=120)
label_8=Label(python,text="year")
label_8.place(x=250,y=120)
entry_8=Entry(python,textvariable=year,width=10)
entry_8.place(x=280,y=120)




btn_1=Button(python,text='save',command=save_info)
btn_1.place(x=10,y=150)



label_1.place(x=10,y=20)
label_2.place(x=10,y=50)
label_3.place(x=10,y=80)
entry_1.place(x=120,y=20)
entry_2.place(x=160,y=50)
entry_3.place(x=120,y=80)


label_4=Label(python,text="Enter your message to send")
label_4.place(x=600,y=400)
entry_4=Entry(python)

entry_4.place(x=600,y=430)
btn2=Button(python,text="send",command=mess)
btn2.place(x=600,y=530)

label_19=Label(python,text="Messages are end to end encrypted",bg='Orange')
label_19.place(x=700,y=530)
label_20=Label(python,text="User Information",bg='Orange')
label_20.place(x=400,y=10)
label_21=Label(python,text="Thank you",bg='Orange')
label_21.place(x=700,y=650)
label_19=Label(python,text="Enter Name")
label_19.place(x=600,y=380)
entry_67=Entry(python)
entry_67.place(x=700,y=380)

l1=Label(python,text="Name: ").place(x=600,y=40)
d=StringVar()
e1=Entry(python,textvariable=d).place(x=700,y=40)
b=Button(python,text="Search",command=search).place(x=600,y=80)

python.mainloop()
