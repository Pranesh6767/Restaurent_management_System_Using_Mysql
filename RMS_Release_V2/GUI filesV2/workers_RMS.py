#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 6.0
#  in conjunction with Tcl version 8.6
#    Nov 29, 2020 01:51:56 PM IST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import workers_RMS_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    workers_RMS_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    workers_RMS_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("1425x690+66+171")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1,  1)
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.008, rely=0.217, relheight=0.742
                , relwidth=0.613)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#8e8eff")

        self.listbox_UI = tk.Listbox(self.Frame1)
        self.listbox_UI.place(relx=0.011, rely=0.137, relheight=0.834
                , relwidth=0.977)
        self.listbox_UI.configure(background="white")
        self.listbox_UI.configure(font="TkFixedFont")
        self.listbox_UI.configure(selectbackground="blue")
        self.listbox_UI.configure(selectforeground="white")

        self.Frame2 = tk.Frame(top)
        self.Frame2.place(relx=0.636, rely=0.029, relheight=0.586
                , relwidth=0.353)
        self.Frame2.configure(relief='groove')
        self.Frame2.configure(borderwidth="2")
        self.Frame2.configure(relief="groove")
        self.Frame2.configure(background="#ff80ff")

        self.Label2 = tk.Label(self.Frame2)
        self.Label2.place(relx=0.171, rely=0.025, height=46, width=318)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(background="#fb173f")
        self.Label2.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Label2.configure(text='''Add Worker''')

        self.Label3 = tk.Label(self.Frame2)
        self.Label3.place(relx=0.085, rely=0.297, height=37, width=152)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(font="-family {Segoe UI} -size 16")
        self.Label3.configure(text='''Last Name :''')

        self.add_submit_UI = tk.Button(self.Frame2)
        self.add_submit_UI.place(relx=0.278, rely=0.866, height=43, width=196)
        self.add_submit_UI.configure(background="#008200")
        self.add_submit_UI.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.add_submit_UI.configure(foreground="#ffffff")
        self.add_submit_UI.configure(pady="0")
        self.add_submit_UI.configure(text='''SUBMIT''')

        self.Label7 = tk.Label(self.Frame2)
        self.Label7.place(relx=0.099, rely=0.421, height=36, width=142)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(font="-family {Segoe UI} -size 16")
        self.Label7.configure(text='''Role  :''')

        self.Label8 = tk.Label(self.Frame2)
        self.Label8.place(relx=0.085, rely=0.173, height=36, width=152)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(font="-family {Segoe UI} -size 16")
        self.Label8.configure(text='''First Name :''')

        self.Label9 = tk.Label(self.Frame2)
        self.Label9.place(relx=0.08, rely=0.569, height=36, width=152)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(font="-family {Segoe UI} -size 16")
        self.Label9.configure(text='''Experience :''')

        self.Label10 = tk.Label(self.Frame2)
        self.Label10.place(relx=0.08, rely=0.718, height=36, width=163)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(font="-family {Segoe UI} -size 16")
        self.Label10.configure(text='''Salary in Rs. :''')

        self.add_fname_UI = tk.Entry(self.Frame2)
        self.add_fname_UI.place(relx=0.449, rely=0.173, height=34
                , relwidth=0.386)
        self.add_fname_UI.configure(background="white")
        self.add_fname_UI.configure(font="TkFixedFont")
        self.add_fname_UI.configure(selectbackground="blue")
        self.add_fname_UI.configure(selectforeground="white")

        self.add_lname_UI = tk.Entry(self.Frame2)
        self.add_lname_UI.place(relx=0.449, rely=0.297, height=34
                , relwidth=0.386)
        self.add_lname_UI.configure(background="white")
        self.add_lname_UI.configure(font="TkFixedFont")
        self.add_lname_UI.configure(selectbackground="blue")
        self.add_lname_UI.configure(selectforeground="white")

        self.add_role_UI = tk.Entry(self.Frame2)
        self.add_role_UI.place(relx=0.457, rely=0.421, height=34, relwidth=0.386)

        self.add_role_UI.configure(background="white")
        self.add_role_UI.configure(font="TkFixedFont")
        self.add_role_UI.configure(selectbackground="blue")
        self.add_role_UI.configure(selectforeground="white")

        self.add_experience_UI = tk.Entry(self.Frame2)
        self.add_experience_UI.place(relx=0.457, rely=0.569, height=34
                , relwidth=0.386)
        self.add_experience_UI.configure(background="white")
        self.add_experience_UI.configure(font="TkFixedFont")
        self.add_experience_UI.configure(selectbackground="blue")
        self.add_experience_UI.configure(selectforeground="white")

        self.add_salary_UI = tk.Entry(self.Frame2)
        self.add_salary_UI.place(relx=0.457, rely=0.718, height=34
                , relwidth=0.386)
        self.add_salary_UI.configure(background="white")
        self.add_salary_UI.configure(font="TkFixedFont")
        self.add_salary_UI.configure(selectbackground="blue")
        self.add_salary_UI.configure(selectforeground="white")

        self.Frame3 = tk.Frame(top)
        self.Frame3.place(relx=0.636, rely=0.652, relheight=0.3, relwidth=0.35)
        self.Frame3.configure(relief='groove')
        self.Frame3.configure(borderwidth="2")
        self.Frame3.configure(relief="groove")
        self.Frame3.configure(background="#a6a653")

        self.Label4 = tk.Label(self.Frame3)
        self.Label4.place(relx=0.146, rely=0.097, height=46, width=338)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(background="#fb173f")
        self.Label4.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Label4.configure(text='''Delete Worker''')

        self.Label5 = tk.Label(self.Frame3)
        self.Label5.place(relx=0.088, rely=0.435, height=36, width=182)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(background="#80ffff")
        self.Label5.configure(font="-family {Segoe UI} -size 15")
        self.Label5.configure(text='''Worker's ID  :''')

        self.del_submit_UI = tk.Button(self.Frame3)
        self.del_submit_UI.place(relx=0.281, rely=0.676, height=43, width=196)
        self.del_submit_UI.configure(background="#008200")
        self.del_submit_UI.configure(font="-family {Segoe UI} -size 18 -weight bold")
        self.del_submit_UI.configure(foreground="#ffffff")
        self.del_submit_UI.configure(pady="0")
        self.del_submit_UI.configure(text='''SUBMIT''')

        self.del_id_UI = tk.Entry(self.Frame3)
        self.del_id_UI.place(relx=0.581, rely=0.435, height=34, relwidth=0.349)
        self.del_id_UI.configure(background="#80ffff")
        self.del_id_UI.configure(font="TkFixedFont")
        self.del_id_UI.configure(selectbackground="blue")
        self.del_id_UI.configure(selectforeground="white")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.028, rely=0.014, height=86, width=338)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(background="#c0c0c0")
        self.Label1.configure(font="-family {Segoe UI} -size 24 -weight bold")
        self.Label1.configure(foreground="#99004d")
        self.Label1.configure(text='''WORKERS''')

        self.back_UI = tk.Button(top)
        self.back_UI.place(relx=0.028, rely=0.145, height=43, width=116)
        self.back_UI.configure(background="#ef053a")
        self.back_UI.configure(font="-family {Segoe UI} -size 17 -weight bold")
        self.back_UI.configure(pady="0")
        self.back_UI.configure(text='''BACK''')

        self.Frame4 = tk.Frame(top)
        self.Frame4.place(relx=0.274, rely=0.014, relheight=0.181
                , relwidth=0.341)
        self.Frame4.configure(relief='groove')
        self.Frame4.configure(borderwidth="2")
        self.Frame4.configure(relief="groove")
        self.Frame4.configure(background="#ffff80")
        self.Frame4.configure(highlightbackground="#c0c0c0")

        self.Label11 = tk.Label(self.Frame4)
        self.Label11.place(relx=0.021, rely=0.08, height=35, width=163)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(background="#ff0000")
        self.Label11.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.Label11.configure(text='''Attendance''')

        self.att_reset_UI = tk.Button(self.Frame4)
        self.att_reset_UI.place(relx=0.741, rely=0.08, height=43, width=112)
        self.att_reset_UI.configure(background="#008040")
        self.att_reset_UI.configure(cursor="fleur")
        self.att_reset_UI.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.att_reset_UI.configure(foreground="#ffffff")
        self.att_reset_UI.configure(pady="0")
        self.att_reset_UI.configure(text='''Reset''')

        self.Label12 = tk.Label(self.Frame4)
        self.Label12.place(relx=0.041, rely=0.56, height=31, width=154)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(background="#80ff80")
        self.Label12.configure(font="-family {Segoe UI} -size 20")
        self.Label12.configure(text='''Worker ID''')

        self.att_submit_UI = tk.Button(self.Frame4)
        self.att_submit_UI.place(relx=0.741, rely=0.56, height=43, width=112)
        self.att_submit_UI.configure(background="#008040")
        self.att_submit_UI.configure(font="-family {Segoe UI} -size 20 -weight bold")
        self.att_submit_UI.configure(foreground="#ffffff")
        self.att_submit_UI.configure(pady="0")
        self.att_submit_UI.configure(text='''Submit''')

        self.att_workerid_UI = tk.Entry(self.Frame4)
        self.att_workerid_UI.place(relx=0.412, rely=0.56, height=30
                , relwidth=0.276)
        self.att_workerid_UI.configure(background="white")
        self.att_workerid_UI.configure(font="TkFixedFont")
        self.att_workerid_UI.configure(selectbackground="blue")
        self.att_workerid_UI.configure(selectforeground="white")

        self.att_resetmonth_UI = tk.Button(self.Frame4)
        self.att_resetmonth_UI.place(relx=0.412, rely=0.08, height=43, width=112)

        self.att_resetmonth_UI.configure(activebackground="#f9f9f9")
        self.att_resetmonth_UI.configure(background="#008040")
        self.att_resetmonth_UI.configure(font="-family {DejaVu Sans} -size 10 -weight bold")
        self.att_resetmonth_UI.configure(foreground="#ffffff")
        self.att_resetmonth_UI.configure(pady="0")
        self.att_resetmonth_UI.configure(text='''Reset Month''')

if __name__ == '__main__':
    vp_start_gui()





