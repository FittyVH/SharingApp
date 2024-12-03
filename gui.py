from tkinter import *
import socket
from tkinter import filedialog
from tkinter import messagebox
import os

root = Tk()
root.geometry("450x560+500+200")
root.title("ShareKro")
root.configure(bg="#f4fdfe")
root.resizable(False, False)

def Send():
    window = Toplevel(root)
    window.geometry("450x560+500+200")
    window.title("Send")
    window.configure(bg="#f4fdfe")
    window.resizable(False, False)

    def SelectFile():

        # global means that this variable is applicable to full code and not just this function
        global filename

        # open window to select file 
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                            title='Select file',
                                            filetype=(('file_type', '*.txt'), ('jpgs', '*.jpg'), ('pngs', '*.png'), ('all_files', '*.*')))
        
    def Sender():

        # server creation
        s = socket.socket()
        host = socket.gethostbyname(socket.gethostname())
        port = 8080
        s.bind((host, port))
        s.listen(1)

        print(host)
        print("Waiting for connections...")

        # communication socket
        comm, address = s.accept()

        # open file
        # 'rb',read binary, is used to set the file opening mode to binary(imp for sharing over network)
        file = open(filename, 'rb')

        # specify size
        fileData = file.read(1024)

        # send data
        comm.send(fileData)
        print("Data transmitted")




    #add bg image here

    Mbg = PhotoImage(file="GUI/id.png")
    Label(window, image=Mbg, bg="#f4fdfe").place(x=100, y=260)

    Button(window, text="+ select file", width=10, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=SelectFile).place(x=160, y=150)
    Button(window, text="SEND", width=8, height=1, font='arial 14 bold', bg="#fff", fg="#000", command=Sender).place(x=300, y=150)

    # get host username
    host = socket.gethostname()
    Label(window, text=f'IP: {host}', font=('Arial', 14), bg='white', fg='black').place(x=225, y=290)

    window.mainloop()

def Recv():
    main = Toplevel(root)
    main.geometry("450x560+500+200")
    main.title("Receive")
    main.configure(bg="#f4fdfe")
    main.resizable(False, False)

    def Receiver():

        # receive text entered by user in the senderID Entry
        ID = senderID.get()

        # receive text entered by user in the incomingFile Entry
        filename1 = incomingFile.get()

        # client creation
        s = socket.socket()
        port = 8080
        s.connect((ID, port))
        
        # 'wb', write binary, used to write binary files
        file = open(filename1, 'wb')
        fileData = s.recv(1024)

        # will open file which is already opened in binary write mode 
        file.write(fileData)
        
        file.close()
        print("file received :)")

    # add bg

    logo = PhotoImage(file="GUI/profile.png")
    Label(main, image=logo, bg="#f4fdfe").place(x=10, y=240)

    Label(main, text='Receive', font=('arial', 20), bg="#f4fdfe").place(x=110, y=270)

    Label(main, text='Input sender ID', font=('arial', 15, 'bold'), bg="#f4fdfe").place(x=20, y=340)
    senderID = Entry(main, width=25, fg='black', border=2, bg='white', font=('arial', 15))
    senderID.place(x=20, y=370)
    senderID.focus()
    
    Label(main, text='filename for incoming file:', font=('arial', 15, 'bold'), bg="#f4fdfe").place(x=20, y=420)
    incomingFile = Entry(main, width=25, fg='black', border=2, bg='white', font=('arial', 15))
    incomingFile.place(x=20, y=450)

    rr = Button(main, text="Receive", compound=LEFT, bg="#1fff96", fg='black', font="arial 14 bold", command=Receiver)
    rr.place(x=20, y=500)

    main.mainloop()

Label(root, text="File Share", font=('Acumin Variable Concept', 20, 'bold'), bg="#f4fdfe").place(x=20, y=30)
Frame(root, width=400, height=2, bg="#f3f5f6").place(x=25, y=80)

sendImage = PhotoImage(file="GUI/send.png")
send = Button(root, image=sendImage, bg="#f4fdfe", bd=0, command=Send)
send.place(x=50, y=100)

recvImage = PhotoImage(file="GUI/recv.png")
recv = Button(root, image=recvImage, bg="#f4fdfe", bd=0, command=Recv)
recv.place(x=300, y=100)

Label(root, text="Send", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=65, y=200)
Label(root, text="Receive", font=('Acumin Variable Concept', 17, 'bold'), bg="#f4fdfe").place(x=300, y=200)

root.mainloop()