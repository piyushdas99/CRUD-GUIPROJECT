import mysql.connector as mysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg

class tkinter_db(Tk):
    def __init__(self):
        super().__init__()
        self.maxsize(width=700,height=600)
        self.title("CRUD operations")
        self.create_label()
        self.create_label_for_crud()
        self.list = Listbox(self)
        self.list.grid(row=3, column=3,padx=10,pady=8)
        self.butt = ttk.Button(self,text='delete',command=self.dele)
        self.butt.grid(row =4,column=3 )
    def dele(self):
        self.list.delete(ANCHOR)

    def show(self):

        conn = mysql.connect(host="localhost", user="root", password="root", database='classicmodels')
        c = conn.cursor()

        c.execute(f"SELECT * FROM student;")
        rows = c.fetchall()
        self.list.delete(0,self.list.size())
        for row in rows:
            self.list.insert(END, row[1])
        conn.close()





    def create_label(self):
        self.label = ttk.LabelFrame(self,text='CRUD operations', )
        self.label.grid(row=0,column=0)

        self.labelID = ttk.Label(self.label,text='enter ID')
        self.labelID.grid(row=0,column=0 )

        self.entry = ttk.Entry(self.label,width=20)
        self.entry.grid(row=0,column=1,padx=5,pady=5)

        self.labelName = ttk.Label(self.label, text='enter Name')
        self.labelName.grid(row=1, column=0)

        self.entry2 = ttk.Entry(self.label, width=20)
        self.entry2.grid(row=1, column=1,padx=5,pady=5)


        self.labelPhone = ttk.Label(self.label, text='enter PhoneNumber')
        self.labelPhone.grid(row=2, column=0)

        self.entry3 = ttk.Entry(self.label, width=20)
        self.entry3.grid(row=2, column=1,padx=5,pady=5)


    def insert_db(self):
        id = self.entry.get()
        name = self.entry2.get()
        phone = self.entry3.get()
        if (id  =='' or name == '' or phone == ''):
            msg.showinfo("message","this will be recoded")
        else:
            conn = mysql.connect(host="localhost",user="root",password="root",database='classicmodels')
            c=conn.cursor()

            c.execute(f"INSERT INTO student VALUES({id}, '{name}', '{phone}');")

            c.execute('commit')
            self.entry.delete(0,'end')
            self.entry2.delete(0,'end')
            self.entry3.delete(0,'end')
            self.show()
            msg.showinfo('inserted','values were inserted')

            conn.close()



    def create_label_for_crud(self):
        self.lebl2 = ttk.LabelFrame(self,text='insert/update/delete/get')
        self.lebl2.grid(row=3,column=0)




        self.insert_n = ttk.Button(self.lebl2,text='insert', command=self.insert_db)
        self.insert_n.grid(column=0,row=0,padx=5,pady=5)
        self.delete_n = ttk.Button(self.lebl2, text='delete',command = self.delete_db)
        self.delete_n.grid(column=2, row=0,padx=5,pady=5)
        self.update_n = ttk.Button(self.lebl2, text='update',command= self.update)
        self.update_n.grid(column=0, row=2,padx=5,pady=5)
        self.get_n = ttk.Button(self.lebl2, text='get',command=self.get)

        self.get_n.grid(column=2, row=2,padx=5,pady=5)

    def insert(self):
        pass

    def delete_db(self):
        if (self.entry.get() == ''):
            msg.showinfo('incoreect','IT is compulsory to add an ID')
        else:
            conn = mysql.connect(host="localhost", user="root", password="root", database='classicmodels')
            c = conn.cursor()

            c.execute(f"DELETE FROM student  WHERE id = {self.entry.get()};")

            c.execute('commit')
            self.entry.delete(0, 'end')
            self.entry2.delete(0, 'end')
            self.entry3.delete(0, 'end')
            msg.showinfo('deleted', 'values were deleted')
            self.show()
            conn.close()


        pass

    def update(self):

        id = self.entry.get()
        name = self.entry2.get()
        phone = self.entry3.get()
        if (id == '' or name == '' or phone == ''):
            msg.showinfo("Fill Everithing", "All details are important")
        else:
            conn = mysql.connect(host="localhost", user="root", password="root", database='classicmodels')
            c = conn.cursor()

            c.execute(f"UPDATE student  set name = '{name}', phone = '{phone}' where id = {id};")

            c.execute('commit')
            self.entry.delete(0, 'end')
            self.entry2.delete(0, 'end')
            self.entry3.delete(0, 'end')
            msg.showinfo('UPDATED', 'values were updated succesfully')
            self.show()
            conn.close()

        pass


    def get(self):
        if (self.entry.get() == ''):
            msg.showinfo('REMINDER','IT is compulsory to add an ID if you want to get anything')
        else:
            conn = mysql.connect(host="localhost", user="root", password="root", database='classicmodels')
            c = conn.cursor()

            c.execute(f"SELECT * FROM student  WHERE id = {self.entry.get()};")

            rows = c.fetchall()
            for row in rows:
                self.entry2.insert(0,row[1])
                self.entry3.insert(0, row[2])

            c.execute('commit')
            # self.entry.delete(0, 'end')
            # self.entry2.delete(0, 'end')
            # self.entry3.delete(0, 'end')

            msg.showinfo('GOT?', 'I SUPPOSE YOU GOT WHAT YOU WERE LOOKING FOR')
            self.show()
            conn.close()

        pass







window = tkinter_db()
window.mainloop()




