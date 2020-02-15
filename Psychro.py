# Physchrometric Calculations
from tkinter import *
from tkinter import messagebox
from CoolProp.HumidAirProp import HAPropsSI

root = Tk()
root.geometry('400x160')
root.title('Psychrometrics')
f1 = Frame(master=root, borderwidth=2, pady=5).grid(row=0, column=0)
f2 = Frame(root, borderwidth=2).grid(row=1, column=0)
f3 = Frame(root, borderwidth=2).grid(row=2, column=0)

l1_label = Label(f1, text='Psychrometric Calculations', bg='#c3ff0f', font=("Arial Bold", 16)).grid(row=0, column=0)
f21 = Frame(f2, borderwidth=2).grid(row=1, column=0)

f22 = Frame(f2, borderwidth=2).grid(row=1, column=0)

TDB_label = Label(f21, text='Enter Dry Bulb Temperature °C ').grid(row=1, column=0, sticky=W, padx=2)
TWB_label = Label(f22, text='Enter Wet Bulb Temperature °C ').grid(row=2, column=0, sticky=W, padx=2)

TRH_label = Label(f2, text='Relative Humidity % ').grid(row=3, column=0, sticky=W, padx=2)
TAH_label = Label(f2, text='Humidity kg-water/kg-dry-air ').grid(row=4, column=0, sticky=W, padx=2)
Tdb = StringVar()
Tdb_entry = Entry(f2, width=16, textvariable=Tdb).grid(row=1, column=1,sticky=W)
Twb = StringVar()
Twb_entry = Entry(f2, width=16, textvariable=Twb).grid(row=2, column=1)
Rh = StringVar()
Rh_entry = Entry(f2, width=16, textvariable=Rh).grid(row=3, column=1)
H = StringVar()
H_entry = Entry(f2, width=16, textvariable=H).grid(row=4, column=1)


def calc_clicked():
    try:
        a = float(Tdb.get()) + 273.15
        b = float(Twb.get()) + 273.15
        H.set(HAPropsSI('W', 'T', a, 'P', 101325, 'B', b))
        Rh.set(100.0 * HAPropsSI('R', 'T', a, 'P', 101325, 'B', b))
    except ValueError:
        messagebox.showinfo('Error', 'Please enter correct values')
        Tdb.set('')
        Twb.set('')


calc_button = Button(f2, text=' Run ', padx=10, pady=4, command=calc_clicked).grid(row=5, column=0, sticky=W, padx=2)
exit_button = Button(f2, text=' Exit ', padx=10, pady=4, command=root.quit).grid(row=5, column=1, sticky=W, padx=2)

root.mainloop()
