import sqlite3
from tkinter import*
from datetime import datetime, date, timedelta
#############################################################################
conn=sqlite3.connect('lms.db')
c=conn.cursor()
try:
    c.execute('''CREATE TABLE student_info(id,
                                        name,
                                        year,
                                        division,
                                        mo_no)''')
    c.execute('''CREATE TABLE book_info(id,
                                        title,
                                        author,
                                        publication,
                                        department,
                                        availablity)''')
    c.execute('''CREATE TABLE issue(book_id,
                                    student_id,
                                    issue_date,
                                    return_date,
                                    status
                                    )''')
    c.execute('''CREATE TABLE record(student,book,n)''')
    c.execute('''INSERT INTO record VALUES('1','1',1)''')
except sqlite3.OperationalError:
    pass

root=Tk()
root.geometry("900x500")
#############################################################################
#                        NEW STUDENT INFO                                
#############################################################################
def stu_info():
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    canvas=Canvas(root,bg='white')
    canvas.place(x=200,y=100,width=500,height=300)
    txt='NEW STUDENT INFORMATION'
    label= Label(root,bg='white',bd=5,text=txt,font=('',20))
    label.place(x=175,y=30,width=550)
    button=Button(root,text='BACK',font=('',12),command=back)
    button.place(x=10,y=10)
    #######             #STUDENT ENTRIES              #######################
    x1,y1,x2,y2=345,50,80,85
    entrys1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    #########################################################################
    entrys1.place(x=x1+x2,y=1*y1+y2)
    entrys2.place(x=x1+x2,y=2*y1+y2)
    entrys3.place(x=x1+x2,y=3*y1+y2)
    entrys4.place(x=x1+x2,y=4*y1+y2)
    entrys5.place(x=x1+x2,y=5*y1+y2)
    #########################################################################
    x1,y1,x2,y2=110,50,130,81
    labels1= Label(root,bg='white',bd=5,text='Student Name',font=('',15))
    labels2= Label(root,bg='white',bd=5,text='Year',font=('',15))
    labels3= Label(root,bg='white',bd=5,text='Division',font=('',15))
    labels4= Label(root,bg='white',bd=5,text='mobile number',font=('',15))
    labels5= Label(root,bg='white',bd=5,text='Student Id',font=('',15))
    #########################################################################
    labels1.place(x=x1+x2,y=1*y1+y2)
    labels2.place(x=x1+x2,y=2*y1+y2)
    labels3.place(x=x1+x2,y=3*y1+y2)
    labels4.place(x=x1+x2,y=4*y1+y2)
    labels5.place(x=x1+x2,y=5*y1+y2)
    #####################
    def inserts():
        name=entrys1.get()
        year=entrys2.get()
        division=entrys3.get()
        mo_no=entrys4.get()
        
        for i in c.execute('SELECT * FROM record'):
            id=int(i[0])
        entrys5.delete(0, END)
        entrys5.insert(0,'0'+str(id))
        ui=str(int(id)+1)
        c.execute('''UPDATE record SET student=? WHERE n=1''',(str(id+1),))
        conn.commit()
        id=str(id)
        c.execute('''INSERT INTO student_info(id,name,year,division,mo_no)
                            VALUES(?,?,?,?,?)''',(id,name,year,division,mo_no))
        conn.commit()
        txt='Your assigned ID is 0'+str(id)
        labeln=Label(root,bg='white',bd=5,text=txt,font=('',15))
        labeln.place(x=50,y=450,width=650)
    def get():
        entrys1.delete(0, END)
        entrys2.delete(0, END)
        entrys3.delete(0, END)
        entrys4.delete(0, END)
        entrys5.delete(0, END)

    #################
    button1=Button(root,text='CLEAR',font=('',12),command=get)
    button1.place(x=250,y=410)
    button2=Button(root,text='SUBMIT',font=('',12),command=inserts)
    button2.place(x=450,y=410)

#########################################################################
#########               BOOK INFO                ########################
#########################################################################
def book_info():
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    canvas=Canvas(root,bg='white')
    canvas.place(x=200,y=100,width=500,height=300)
    txt='NEW BOOK INFORMATION'
    label= Label(root,bg='white',bd=5,text=txt,font=('',20))
    label.place(x=175,y=30,width=550)
    button=Button(root,text='BACK',font=('',12),command=back)
    button.place(x=10,y=10)

    #######BOOK ENTRIES#######
    x1,y1,x2,y2=345,50,80,85
    entryb1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    ################
    entryb1.place(x=x1+x2,y=1*y1+y2)
    entryb2.place(x=x1+x2,y=2*y1+y2)
    entryb3.place(x=x1+x2,y=3*y1+y2)
    entryb4.place(x=x1+x2,y=4*y1+y2)
    entryb5.place(x=x1+x2,y=5*y1+y2)
    ##################
    x1,y1,x2,y2=110,50,130,81
    labelb1= Label(root,bg='white',bd=5,text='Title',font=('',15))
    labelb2= Label(root,bg='white',bd=5,text='Author',font=('',15))
    labelb3= Label(root,bg='white',bd=5,text='Publication',font=('',15))
    labelb4= Label(root,bg='white',bd=5,text='Department',font=('',15))
    labelb5= Label(root,bg='white',bd=5,text='Book Id',font=('',15))
    ################
    labelb1.place(x=x1+x2,y=1*y1+y2)
    labelb2.place(x=x1+x2,y=2*y1+y2)
    labelb3.place(x=x1+x2,y=3*y1+y2)
    labelb4.place(x=x1+x2,y=4*y1+y2)
    labelb5.place(x=x1+x2,y=5*y1+y2)
    #####################
    def inserts():
        name=entryb1.get()
        author=entryb2.get()
        pub=entryb3.get()
        dep=entryb4.get()
        
        for i in c.execute('SELECT * FROM record'):
            id=int(i[1])
        entryb5.delete(0, END)
        entryb5.insert(0,'1'+str(id))
        ui=str(int(id)+1)
        c.execute('''UPDATE record SET book=? WHERE n=1''',(str(id+1),))
        conn.commit()
        id=str(id)
        c.execute('''INSERT INTO book_info(id,title,author,publication,department,availablity)
                            VALUES(?,?,?,?,?,True)''',(id,name,author,pub,dep))
        conn.commit()
        txt='BOOK ID is 1'+str(id)
        labeln=Label(root,bg='white',bd=5,text=txt,font=('',15))
        labeln.place(x=50,y=450,width=650)
    def get():
        entryb1.delete(0, END)
        entryb2.delete(0, END)
        entryb3.delete(0, END)
        entryb4.delete(0, END)
        entryb5.delete(0, END)       

    
    
    #################
    
    
    button1=Button(root,text='CLEAR',font=('',12),command=get)
    button1.place(x=250,y=410)
    button2=Button(root,text='SUBMIT',font=('',12),command=inserts)
    button2.place(x=450,y=410)

##############################################################################
#                     BOOK ISSUE
#########################################################################
def issue():
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    canvas=Canvas(root,bg='white')
    canvas.place(x=25,y=100,width=850,height=300)
    txt='ISSUE BOOK'
    label= Label(root,bg='white',bd=5,text=txt,font=('',20))
    label.place(x=110,y=30,width=680)
    button=Button(root,text='BACK',font=('',12),command=back)
    button.place(x=10,y=10)
    txt='BOOK ISSUED'
    labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
    labelx.place(x=25,y=460,width=850)
    #######STUDENT ENTRIES#######
    x1,y1,x2,y2=25,50,170,85
    entrys1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    ################
    entrys1.place(x=x1+x2,y=1*y1+y2)
    entrys2.place(x=x1+x2,y=2*y1+y2)
    entrys3.place(x=x1+x2,y=3*y1+y2)
    entrys4.place(x=x1+x2,y=4*y1+y2)
    entrys5.place(x=x1+x2,y=5*y1+y2)
    ##################
    x1,y1,x2,y2=25,50,10,81
    labels1= Label(root,bg='white',bd=5,text='Student Name',font=('',15))
    labels2= Label(root,bg='white',bd=5,text='Year',font=('',15))
    labels3= Label(root,bg='white',bd=5,text='Division',font=('',15))
    labels4= Label(root,bg='white',bd=5,text='mobile number',font=('',15))
    labels5= Label(root,bg='white',bd=5,text='Student Id',font=('',15))
    ################
    labels1.place(x=x1+x2,y=1*y1+y2)
    labels2.place(x=x1+x2,y=2*y1+y2)
    labels3.place(x=x1+x2,y=3*y1+y2)
    labels4.place(x=x1+x2,y=4*y1+y2)
    labels5.place(x=x1+x2,y=5*y1+y2)
    #######BOOK ENTRIES#######
    x1,y1,x2,y2=25,50,600,85
    entryb1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    ################
    entryb1.place(x=x1+x2,y=1*y1+y2)
    entryb2.place(x=x1+x2,y=2*y1+y2)
    entryb3.place(x=x1+x2,y=3*y1+y2)
    entryb4.place(x=x1+x2,y=4*y1+y2)
    entryb5.place(x=x1+x2,y=5*y1+y2)
    ##################
    x1,y1,x2,y2=25,50,450,81
    labelb1= Label(root,bg='white',bd=5,text='Title',font=('',15))
    labelb2= Label(root,bg='white',bd=5,text='Author',font=('',15))
    labelb3= Label(root,bg='white',bd=5,text='Publication',font=('',15))
    labelb4= Label(root,bg='white',bd=5,text='Department',font=('',15))
    labelb5= Label(root,bg='white',bd=5,text='Book Id',font=('',15))
    ################
    labelb1.place(x=x1+x2,y=1*y1+y2)
    labelb2.place(x=x1+x2,y=2*y1+y2)
    labelb3.place(x=x1+x2,y=3*y1+y2)
    labelb4.place(x=x1+x2,y=4*y1+y2)
    labelb5.place(x=x1+x2,y=5*y1+y2)
    ############################################
    ###########################################
    entryx=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryx.place(x=25,y=410)
    labelx=Label(root,bg='white',bd=5,text='',font=('',15))
    labelx.place(x=25,y=460,width=850)
    def enter_data():
        txt=''
        labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
        labelx.place(x=25,y=460,width=850)
        a=entryx.get()
        if a[0]=="0":
            entrys5.delete(0, END)
            entrys5.insert(0,a[1:])
            s5=entrys5.get()
            for i in c.execute('''SELECT * FROM student_info WHERE id=?''',(s5,)):
                entrys1.delete(0,END)
                entrys2.delete(0,END)
                entrys3.delete(0,END)
                entrys4.delete(0,END)
                entrys5.delete(0,END)
                entrys1.insert(0,i[1])
                entrys2.insert(0,i[2])
                entrys3.insert(0,i[3])
                entrys4.insert(0,i[4])
                entrys5.insert(0,'0'+s5)
        elif a[0]=='1':
            entryb5.delete(0, END)
            entryb5.insert(0,a[1:])
            b5=entryb5.get()
            for i in c.execute('''SELECT * FROM book_info WHERE id=?''',(b5,)):
                entryb1.delete(0,END)
                entryb2.delete(0,END)
                entryb3.delete(0,END)
                entryb4.delete(0,END)
                entryb5.delete(0,END)
                entryb1.insert(0,i[1])
                entryb2.insert(0,i[2])
                entryb3.insert(0,i[3])
                entryb4.insert(0,i[4])
                entryb5.insert(0,'1'+b5)
        else:
            txt='Please Enter Valid ID'
            labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
            labelx.place(x=25,y=460,width=850)
        
    entryx.bind('<Return>',(lambda event:enter_data()))

    
    def submit():

        book_id=entryb5.get()[1:]
        student_id=entrys5.get()[1:]
        issue_date=str(date.today())
        return_date=str(date.today()+timedelta(days=7))
        for i in c.execute('''SELECT * FROM book_info WHERE id=?''',(book_id,)):
            if i[5]==True:   
                status='issued'
                c.execute('''INSERT INTO issue(book_id,student_id,issue_date,return_date,status)
                                    VALUES(?,?,?,?,?)''',(book_id,student_id,issue_date,return_date,status))
                for i in c.execute('''SELECT * FROM issue'''):
                    print(i)
                c.execute('''UPDATE book_info SET availablity=False WHERE id=?''',(book_id,))
                txt='BOOK ISSUED'
                labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
                labelx.place(x=25,y=460,width=850)
            else:
                txt='BOOK NOT AVAILABLE'
                labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
                labelx.place(x=25,y=460,width=850)
                
    
    buttons=Button(root,text='SUBMIT',font=('',12),command=submit)
    buttons.place(x=700,y=410)

#############################################################################
#####################    RETURN BOOK ########################################   
#############################################################################
def returnb():
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    canvas=Canvas(root,bg='white')
    canvas.place(x=25,y=100,width=850,height=300)
    txt='RETURN BOOK'
    label= Label(root,bg='white',bd=5,text=txt,font=('',20))
    label.place(x=110,y=30,width=680)
    button=Button(root,text='BACK',font=('',12),command=back)
    button.place(x=10,y=10)
    #######STUDENT ENTRIES#######
    x1,y1,x2,y2=25,50,600,60
    entrys1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entrys6=Entry(root,bd=5,bg='white',fg='black',font=(50))
    ################
    entrys1.place(x=x1+x2,y=1*y1+y2)
    entrys2.place(x=x1+x2,y=2*y1+y2)
    entrys3.place(x=x1+x2,y=3*y1+y2)
    entrys4.place(x=x1+x2,y=4*y1+y2)
    entrys5.place(x=x1+x2,y=5*y1+y2)
    entrys6.place(x=x1+x2,y=6*y1+y2)
    ##################
    x1,y1,x2,y2=25,50,450,56
    labels1= Label(root,bg='white',bd=5,text='Student Name',font=('',15))
    labels2= Label(root,bg='white',bd=5,text='Year',font=('',15))
    labels3= Label(root,bg='white',bd=5,text='Division',font=('',15))
    labels4= Label(root,bg='white',bd=5,text='mobile number',font=('',15))
    labels5= Label(root,bg='white',bd=5,text='Student Id',font=('',15))
    labels6= Label(root,bg='white',bd=5,text='Return date',font=('',15))
    ################
    labels1.place(x=x1+x2,y=1*y1+y2)
    labels2.place(x=x1+x2,y=2*y1+y2)
    labels3.place(x=x1+x2,y=3*y1+y2)
    labels4.place(x=x1+x2,y=4*y1+y2)
    labels5.place(x=x1+x2,y=5*y1+y2)
    labels6.place(x=x1+x2,y=6*y1+y2)
    #######BOOK ENTRIES#######
    #####################
    #############################
    x1,y1,x2,y2=25,50,170,60
    entryb1=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb2=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb3=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb4=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb5=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryb6=Entry(root,bd=5,bg='white',fg='black',font=(50))
    ################
    entryb1.place(x=x1+x2,y=1*y1+y2)
    entryb2.place(x=x1+x2,y=2*y1+y2)
    entryb3.place(x=x1+x2,y=3*y1+y2)
    entryb4.place(x=x1+x2,y=4*y1+y2)
    entryb5.place(x=x1+x2,y=5*y1+y2)
    entryb6.place(x=x1+x2,y=6*y1+y2)
    ##################
    x1,y1,x2,y2=25,50,10,56
    labelb1= Label(root,bg='white',bd=5,text='Title',font=('',15))
    labelb2= Label(root,bg='white',bd=5,text='Author',font=('',15))
    labelb3= Label(root,bg='white',bd=5,text='Publication',font=('',15))
    labelb4= Label(root,bg='white',bd=5,text='Department',font=('',15))
    labelb5= Label(root,bg='white',bd=5,text='Book Id',font=('',15))
    labelb6= Label(root,bg='white',bd=5,text='Issue date',font=('',15))
    ################
    labelb1.place(x=x1+x2,y=1*y1+y2)
    labelb2.place(x=x1+x2,y=2*y1+y2)
    labelb3.place(x=x1+x2,y=3*y1+y2)
    labelb4.place(x=x1+x2,y=4*y1+y2)
    labelb5.place(x=x1+x2,y=5*y1+y2)
    labelb6.place(x=x1+x2,y=6*y1+y2)
    ############################################
    ###########################################
    entryx=Entry(root,bd=5,bg='white',fg='black',font=(50))
    entryx.place(x=25,y=410)
    labelx=Label(root,bg='white',bd=5,text='',font=('',15))
    labelx.place(x=25,y=460,width=850)
    def enter_data():
        a=entryx.get()
        if a[0]=='1':
            entryb5.delete(0, END)
            entryb5.insert(0,a[1:])
        else:
            txt='Please Enter Valid ID'
            labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
            labelx.place(x=25,y=460,width=850)
        b5=entryb5.get()
        for i in c.execute('''SELECT * FROM issue WHERE book_id=?''',(entryb5.get(),)):
            entryb6.delete(0,END)
            entryb6.insert(0,i[2])
            entrys6.delete(0,END)
            entrys6.insert(0,i[3])
            b=i[0]
            for j in c.execute('''SELECT * FROM book_info WHERE id=?''',(b,)):
                entryb1.delete(0,END)
                entryb2.delete(0,END)
                entryb3.delete(0,END)
                entryb4.delete(0,END)
                entryb5.delete(0,END)
                entryb1.insert(0,j[1])
                entryb2.insert(0,j[2])
                entryb3.insert(0,j[3])
                entryb4.insert(0,j[4])
                entryb5.insert(0,'1'+b)
            s=i[1]
            for j in c.execute('''SELECT * FROM student_info WHERE id=?''',(s,)):
                entrys1.delete(0,END)
                entrys2.delete(0,END)
                entrys3.delete(0,END)
                entrys4.delete(0,END)
                entrys5.delete(0,END)
                entrys1.insert(0,j[1])
                entrys2.insert(0,j[2])
                entrys3.insert(0,j[3])
                entrys4.insert(0,j[4])
                entrys5.insert(0,'0'+s)
            
        
    entryx.bind('<Return>',(lambda event:enter_data()))
    def ret():
        book_id=entryb5.get()[1:]
        c.execute('''UPDATE issue SET status="returned" WHERE book_id=?''',(book_id,))
        c.execute('''UPDATE book_info SET availablity=True WHERE id=?''',(book_id,))
        for i in c.execute('''SELECT * FROM book_info'''):
            print(i)
        txt='BOOK RETURNED'
        labelx=Label(root,bg='white',bd=5,text=txt,font=('',15))
        labelx.place(x=25,y=460,width=850)
        
    buttonr=Button(root,text='RETURN',font=('',12),command=ret)
    buttonr.place(x=700,y=410)

###############################################################################
#                      HOME PAGE
#################################################################################
def back():
    canvas=Canvas(root,bg='SlateGray2')
    canvas.place(x=0,y=0,width=900,height=500)
    canvas=Canvas(root,bg='white')
    canvas.place(x=200,y=100,width=500,height=300)


    txt='LIBRARY MANAGEMENT SYSTEM'
    label= Label(root,bg='white',bd=5,text=txt,font=('',30))
    label.place(x=110,y=30,width=680)
    
    button1=Button(root,text='NEW STUDENT INFORMATION',font=('',12),command=stu_info)
    button1.place(x=300,y=140,width=300)
    button2=Button(root,text='NEW BOOK INFORMATION',font=('',12),command=book_info)
    button2.place(x=300,y=200,width=300)
    button3=Button(root,text='ISSUE BOOK',font=('',12),command=issue)
    button3.place(x=300,y=260,width=300)
    button4=Button(root,text='RETURN BOOK',font=('',12),command=returnb)
    button4.place(x=300,y=320,width=300)
    
back()
#################################################################################
conn.commit()
root.mainloop()






















