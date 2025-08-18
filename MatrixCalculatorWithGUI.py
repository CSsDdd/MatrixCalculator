import tkinter
import MatrixCalculaor
window1=tkinter.Tk()
window1.title("MatrixCalculator")
#width,height=window1.maxsize()
#window1.geometry(f"{int(width*0.4)}x{int(height*0.4)}+{int(width*0.3)}+{int(height*0.3)}")
message_m=tkinter.StringVar()
message_m.set("enter the M of the Matrix")
message_n=tkinter.StringVar()
message_n.set("enter the N of the Matrix")
entery1=tkinter.Entry(window1,textvariable=message_m,width=40)
entery2=tkinter.Entry(window1,textvariable=message_n,width=40)
entery1.grid(row=1,column=1)
block1=tkinter.Label(text=" ",width=5)
block1.grid(row=1,column=2)
entery2.grid(row=1,column=3)
m_Of_Matrix=int(0)
n_Of_Matrix=int(0)
def Read_M_and_N():
    entery1.destroy()
    entery2.destroy()
    button1.destroy()
    
    global m_Of_Matrix
    
    m_Of_Matrix=int(message_m.get())
    global n_Of_Matrix
    n_Of_Matrix=int(message_n.get())
    global number_message
    number_message=[]
    
    for i in range(0,m_Of_Matrix):
        number_message.append([])
        for j in range(0,n_Of_Matrix):
            tmp=tkinter.StringVar()
            tmp.set("0")
            number_message[i].append(tmp)
            tkinter.Entry(window1,textvariable=number_message[i][j],width=10).grid(row=i+1+2,column=j+1)
    tkinter.Button(window1,text="Check",command=Read_Matrix).grid(row=m_Of_Matrix+1+2,column=1)
    

def Read_Matrix():
    Matrix=[]
    for i in range(0,m_Of_Matrix):
        Matrix.append([])
        for j in range(0,n_Of_Matrix):
            Matrix[i].append(float(number_message[i][j].get()))
    
    Matrix=MatrixCalculaor.main(Matrix=Matrix,m_Of_Matrix=m_Of_Matrix,n_Of_Matrix=n_Of_Matrix)
    
    for i in range(0,m_Of_Matrix):
        for j in range(0,n_Of_Matrix):
            number_message[i][j].set(str(Matrix[i][j]))

    MatrixCalculaor.display(Matrix)


button1=tkinter.Button(text="Check",command=Read_M_and_N)
button1.grid(row=2,column=2)
window1.mainloop()

