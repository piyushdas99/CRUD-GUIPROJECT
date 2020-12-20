from tkinter import *
from tkinter import ttk

class Window(Tk):
    def __init__(self):
        super(Window,self).__init__()

        self.title('tkinter window')
        self.minsize(500,400)
        #self.create_label_frame()
        #self.add_menu()
        tab_control = ttk.Notebook(self)
        self.tab1 = ttk.Frame(tab_control)
        tab_control.add(self.tab1,text = 'first')
        self.tab2 = ttk.Frame(tab_control)
        tab_control.add(self.tab2, text='second')
        tab_control.pack(expan=1,fill='both')
        self.add_widgets()

    def add_widgets(self):
        frame= LabelFrame(self.tab1,text = 'first tab')
        frame.grid(row=0,column=0,padx=4,pady=4)
        #frame2= LabelFrame(self.tab2,text='whatsup')
        label = Label(frame,text= 'name: ')
        label.grid(row=0,column=0)

        text_edit = Entry(frame,width=25)
        text_edit.grid(row=0,column=1)
        label2 = Label(frame, text='password: ')
        label2.grid(row=2, column=0)

        text_edit2 = Entry(frame,width=25)
        text_edit2.grid(row=2, column=1)

        frame2= LabelFrame(self.tab2,text='doosra')
        frame2.grid(row=0,column=0,padx=4,pady=5)

        label2 = Label(frame2,text='enter anything')
        label2.grid(row=0,column=0)

        text2= Entry(frame2,width=20)
        text2.grid(row=0,column=1)


        label3 = Label(frame2, text='enter anything')
        label3.grid(row=1, column=0)
        text3 = Entry(frame2, width=20)
        text3.grid(row=1, column=1)

        # self.create_combp()

        #self.text_entry()



    # def exi(self):
    #     self.quit()
    #     self.destroy()
    #     exit()
    # def add_menu(self):
    #     menubar= Menu(self)
    #     self.configure(menu=menubar)
    #
    #     filemenu= Menu(menubar,tearoff=0)
    #     menubar.add_cascade(label='file',menu=filemenu)
    #     filemenu.add_command(label='open')
    #     filemenu.add_command(label='goto')
    #     filemenu.add_separator()
    #
    #     exitmenu= Menu(menubar,tearoff=0)
    #     menubar.add_cascade(label='exit',menu=exitmenu)
    #     exitmenu.add_command(label='ejjxit',command=self.exi)







    # def create_label_frame(self):
    #     self.label_frame = ttk.LabelFrame(self,text='label')
    #     self.label_frame.grid(row=2,column=0)
    #     self.label = ttk.Label(self.label_frame,text='90')
    #     self.label.grid(row=1,column=0)
    #
    #     self.label = ttk.Label(self.label_frame, text='9pi0')
    #     self.label.grid(row=2, column=0)
    #
    #     self.label = ttk.Label(self.label_frame, text='9kkn0')
    #     self.label.grid(row=3, column=0)


    # def create_combp(self):
    #     self.languages = StringVar()
    #     self.combo_box = ttk.Combobox(self,width= 20,textvariable=self.languages)
    #     self.combo_box['values'] = ('puyho','kkkn','ugugugug')
    #     self.combo_box.grid(row=0,column=1)
    #     self.label = ttk.Label(self,text='select lang')
    #     self.label.grid(column=0,row=0)

        # self.button = ttk.Button(self,text='click me')
        # self.button.grid(row=5,column=2)



    # def clik_me(self):
    #     self.label.configure(text="hello" + self.name.get())

    # def text_entry(self):
    #     self.name = StringVar()
    #     self.label = ttk.Label(self,text = "gnaan n n n nn m bol")
    #     self.label.grid(column=0,row = 0)
    #     self.textbox = ttk.Entry(self,width = 20,textvariable = self.name)
    #     self.textbox.focus()
    #     self.textbox.grid(row = 1,column=0)
    #     self.button = ttk.Button(self,text = 'click',command=self.clik_me)
    #     self.button.grid(row=2,column=0)
    #     self.button.configure(state='disabled')




        # self.label = ttk.Label(self,text='cool text')
        # self.label.grid(row=0,column=0)
        # self.button = ttk.Button(self,text = 'WHatsapp',command=self.click_me)
        # self.button.grid(row=1,column=0)

        #self.create_label()
        # self.create_layout()

    # def click_me(self):
    #     self.label.configure(text='text chaned')
    #     self.label.configure(foreground='red',background='white')
    #     self.button.configure(text='button changed')
    #
    # def create_layout(self):
    #     Label(self,text = 'pack layout example').grid(row=20,column=9)
    #     Button(self,text='test button').grid(row=49,column=23)
        # Button(self, text='test buttljojon').pack(expand = 1)
        # Button(self, text='test button').pack(side=LEFT)
        # Button(self, text='test button').pack(side=RIGHT)
        # Button(self, text='test button').pack(side = LEFT)
        # Button(self, text='test bukhktton').pack(fill=X)


    # def create_label(self):
    #     label_font = ('times',40,'bold')
    #     label = Label(self,text='tkinter label')
    #     label.config(font=label_font,bg = 'black',fg='red')
    #     label.grid(column = 0, row = 0)






window = Window()

window.mainloop()
