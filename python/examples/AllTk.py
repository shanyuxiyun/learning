from Tkinter import *


class AllTkinterWidgets:

    def __init__(self, master):
        '''
        The Frame widget is very important for the process of grouping and organizing other widgets in a somehow friendly way. It works like a container, which is responsible for arranging the position of other widgets.
        '''
        # bd  The size of the border around the indicator. Default is 2 pixels.
        # master  This represents the parent window.
        frame = Frame(master, width=500, height=400, bd=5)
        # fill: Determines whether widget fills any extra space allocated to it
        # by the packer, or keeps its own minimal dimensions: NONE (default), X
        # (fill only horizontally), Y (fill only vertically), or BOTH (fill
        # both horizontally and vertically).
        frame.pack(fill=X)
    # The relief style of a widget refers to certain simulated 3-D effects around the outside of the widget.
    # flat, groove, raised, ridge, solid, or sunken
        self.mbar = Frame(frame, relief='sunken', bd=2)
        self.mbar.pack(fill=X)

    # Create File menu
        self.filebutton = Menubutton(self.mbar, text='File')
    # Determines which side of the parent widget packs against: TOP (default),
    # BOTTOM, LEFT, or RIGHT.
        self.filebutton.pack(side=LEFT)

    # Normally, a menu can be torn off, the first position (position 0) in the
    # list of choices is occupied by the tear-off element, and the additional
    # choices are added starting at position 1. If you set tearoff=0, the menu
    # will not have a tear-off feature, and choices will be added starting at
    # position 0.
        self.filemenu = Menu(self.filebutton, tearoff=0)
    # menu To associate the menubutton with a set of choices, set this option
    # to the Menu object containing those choices. That menu object must have
    # been created by passing the associated menubutton to the constructor as
    # its first argument.
        self.filebutton['menu'] = self.filemenu

    # Populate File menu
        self.filemenu.add('command', label='Exit', command=self.quit)
        self.filemenu.add('command', label='Save', command=self.quit)

    # Create  object menu
        self.objectbutton = Menubutton(self.mbar, text='Object', )
        self.objectbutton.pack(side=LEFT)

        self.objectmenu = Menu(self.objectbutton, tearoff=0)
        self.objectbutton['menu'] = self.objectmenu

    # Populate object menu
        self.objectmenu.add('command', label='object', command=self.stub)

    # Create  edit menu
        self.editbutton = Menubutton(self.mbar, text='Edit', )
        self.editbutton.pack(side=LEFT)

        self.editmenu = Menu(self.editbutton, tearoff=0)
        self.editbutton['menu'] = self.editmenu

    # Populate edit menu
        self.editmenu.add('command', label='edit', command=self.stub)

    # Create  view menu
        self.viewbutton = Menubutton(self.mbar, text='View', )
        self.viewbutton.pack(side=LEFT)

        self.viewmenu = Menu(self.viewbutton, tearoff=0)
        self.viewbutton['menu'] = self.viewmenu

    # Populate view menu
        self.viewmenu.add('command', label='view', command=self.stub)

    # Create  tools menu
        self.toolsbutton = Menubutton(self.mbar, text='Tools', )
        self.toolsbutton.pack(side=LEFT)

        self.toolsmenu = Menu(self.toolsbutton, tearoff=0)
        self.toolsbutton['menu'] = self.toolsmenu

    # Populate tools menu
        self.toolsmenu.add('command', label='tools', command=self.stub)

    # Create  help menu
        self.helpbutton = Menubutton(self.mbar, text='Help', )
        self.helpbutton.pack(side=RIGHT)

        self.helpmenu = Menu(self.helpbutton, tearoff=0)
        self.helpbutton['menu'] = self.helpmenu

    # Populate help menu
        self.helpmenu.add('command', label='help', command=self.stub)

        iframe1 = Frame(frame, bd=2, relief=SUNKEN)

        # padx Additional padding left and right of the text.
        Button(iframe1, text='Button').pack(side=LEFT, padx=5)
        Checkbutton(iframe1, text='CheckButton').pack(side=LEFT, padx=5)

        # Anchors are used to define where text is positioned relative to a
        # reference point
        v = IntVar()
        Radiobutton(iframe1, text='Button', variable=v,
                    value=3).pack(side=RIGHT, anchor=W)
        Radiobutton(iframe1, text='Dio', variable=v,
                    value=2).pack(side=RIGHT, anchor=E)
        Radiobutton(iframe1, text='Ra', variable=v,
                    value=1).pack(side=RIGHT, anchor=W)
        iframe1.pack(expand=1, fill=X, pady=10, padx=5)

        iframe2 = Frame(frame, bd=2, relief=RIDGE)
        Label(iframe2, text='Label widget:').pack(side=LEFT, padx=5)
        t = StringVar()
        Entry(iframe2, textvariable=t, bg='white').pack(side=RIGHT, padx=5)
        t.set('Entry widget')
        iframe2.pack(expand=1, fill=X, pady=10, padx=5)

        iframe3 = Frame(frame, bd=2, relief=GROOVE)
        listbox = Listbox(iframe3, height=4)
        for line in ['Listbox Entry One',
                     'Entry Two', 'Entry Three', 'Entry Four']:
            listbox.insert(END, line)
        listbox.pack(fill=X, padx=5)
        iframe3.pack(expand=1, fill=X, pady=10, padx=5)

        iframe4 = Frame(frame, bd=2, relief=SUNKEN)
        # The Text widget is used to display text in multiple lines.
        text = Text(iframe4, height=10, width=65)
        fd = open('guido.txt')
        lines = fd.read()
        fd.close()
        text.insert(END, lines)
        text.pack(side=LEFT, fill=X, padx=5)
        # The Scrollbar widget is used to add scrolling capability to various widgets, such as list boxes.
        # Methods inherited from YView:
        #yview(self, *args)
        # Query and change the vertical position of the view.
        # command  A procedure to be called whenever the scrollbar is moved.
        sb = Scrollbar(iframe4, orient=VERTICAL, command=text.yview)
        sb.pack(side=RIGHT, fill=Y)
        text.configure(yscrollcommand=sb.set)
        iframe4.pack(expand=1, fill=X, pady=10, padx=5)

        iframe5 = Frame(frame, bd=2, relief=RAISED)
        Scale(iframe5, from_=0.0, to=50.0, label='Scale widget',
              orient=HORIZONTAL).pack(side=LEFT)
        c = Canvas(iframe5, bg='white', width=340, height=100)
        c.pack()
        for i in range(25):
            c.create_oval(5 + (4 * i), 5 + (3 * i), (5 * i) +
                          60, (i) + 60, fill='gray70')
        c.create_text(260, 80, text='Canvas', font=('verdana', 10, 'bold'))
        iframe5.pack(expand=1, fill=X, pady=10, padx=5)

        iframen = Frame(frame, bd=2, relief=FLAT)
        # This widget provides a multiline and noneditable object that displays texts, automatically breaking lines and justifying their contents.
        # Its functionality is very similar to the one provided by the Label
        # widget, except that it can also automatically wrap the text,
        # maintaining a given width or aspect ratio.
        Message(iframen, text='This is a Message widget', width=300,
                relief=SUNKEN).pack(fill=X, padx=5)
        iframen.pack(expand=1, fill=X, pady=10, padx=5)

    def quit(self):
        root.destroy()

    def stub(self):
        pass

root = Tk()
root.option_add('*font', ('verdana', 10, 'bold'))
all = AllTkinterWidgets(root)
root.title('Tkinter Widgets')
root.mainloop()
