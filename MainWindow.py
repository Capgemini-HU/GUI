from tkinter import *
from Calendar import Calendar
from datetime import date, timedelta

root = Tk()
root.title("Heatmap Application")
root.geometry("600x400")

today = date.today()
yesterday = today - timedelta(days=1)

data = {}
def datePicker(data, txt):
    cal = Tk()
    cal.title("Datepicker")
    Calendar(cal, data, txt)

def setTxt(txt):
    day = data.get("day_selected")
    month = data.get("month_selected")
    year = data.get("year_selected")
    date = str(day) + "-" + str(month) + "-" + str(year)
    data.clear()

    if txt == "from":
        txtFrom.delete(0, END)
        txtFrom.insert(0, date)
    elif txt == "to":
        txtTo.delete(0, END)
        txtTo.insert(0, date)

#Area selector
lblArea = Label(root, text="Area:")
lblArea.grid(column=0, row=0)

areaSelected = StringVar()
areaSelected.set("Livingroom")
areaOptionMenu = OptionMenu(root, areaSelected, "Livingroom", "Kitchen", "Garden")
areaOptionMenu.grid(column=1, row=0)
root.grid_columnconfigure(1, minsize=110)

lblEmpty1 = Label(root, text="")
lblEmpty1.grid(column=2, row=0)
root.grid_columnconfigure(2, minsize=20)

#From date selector
lblFrom = Label(root, text="From:")
lblFrom.grid(column=3, row=0)

txtFrom = Entry(root,width=10)
txtFrom.grid(column=4, row=0)
txtFrom.insert(0, yesterday.strftime('%d-%m-%Y'))

btnFrom = Button(root, text="Date", command=lambda : datePicker(data, "from"))
btnFrom.grid(column=5, row=0)

lblEmpty2 = Label(root, text="")
lblEmpty2.grid(column=6, row=0)
root.grid_columnconfigure(6, minsize=10)

#To date selector
lblTo = Label(root, text="To:")
lblTo.grid(column=7, row=0)

txtTo = Entry(root,width=10)
txtTo.grid(column=8, row=0)
txtTo.insert(0, today.strftime('%d-%m-%Y'))

btnTo = Button(root, text="Date", command=lambda : datePicker(data, "to"))
btnTo.grid(column=9, row=0)

lblEmpty3 = Label(root, text="")
lblEmpty3.grid(column=10, row=0)
root.grid_columnconfigure(10, minsize=20)

#Open heatmap with selected Area and Dates
btnOpenArea = Button(root, text="Open Heatmap")
btnOpenArea.grid(column=11, row=0)

#Show Image selected Area
photo = PhotoImage(file="livingroom.gif")
lblPhoto = Label(root, image=photo)
lblPhoto.grid(row=1, columnspan=13, sticky=W+E+N+S, padx=5, pady=5)

root.mainloop()