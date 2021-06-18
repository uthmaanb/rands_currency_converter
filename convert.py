from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import requests

root = Tk()

# StringVar
results = StringVar()
values1 = StringVar()
values2 = StringVar()

# code to add widgets and style window will go here
root.geometry("450x550")
root.title("Currency Converter (Uthmaan Breda)")
root.config(bg='#00A868')
root.resizable(0, 0)

exchange = PhotoImage(file="exchangerate-removebg-preview.png")
img = Label(root, image=exchange)
img.place(x=10, y=0)
img.config(bg='#00A868')

information = requests.get('https://v6.exchangerate-api.com/v6/89dcd9e8cc7777ded2575ce1/latest/ZAR')
information_json = information.json()

conversion_rates = information_json['conversion_rates']

currency = []
for i in conversion_rates.keys():
    currency.append(i)


currency_cb = ttk.Combobox(root)
currency_cb['values'] = currency
currency_cb['state'] = 'readonly'
currency_cb.set('Select Currency')
currency_cb.place(x=10, y=280)

Label(root, text='Enter Amount:', bg='#00A868').place(x=65, y=330)
ent1 = Entry(root, bg='white')
ent1.place(x=200, y=330)
ent1.focus()
Label(root, text='Converted Amount:', bg='#00A868').place(x=65, y=380)
Label(root, text='', textvariable=results, bg='#00A868').place(x=200, y=380)


def convert(to_currency, amount):
    amount = round(amount * conversion_rates[to_currency], 4)
    return amount


def perform():
    try:
        amount = float(ent1.get())
        to_curr = currency_cb.get()

        converted_amount = convert(to_curr, amount)

        results.set(converted_amount)
    except ValueError:
        if ent1 != int and ent1 != float:
            messagebox.showerror('Entry not valid', 'Enter numbers only')

    except requests.exceptions.ConnectionError:
        messagebox.showerror('Internet error', 'Internet Bad')
    except KeyError:
        messagebox.showerror('ERROR!!!!!!!!!!!!!!!', 'Select Currency')


# kill program
def kill():
    return root.destroy()


# clear function
def clear():
    currency_cb.set('Select Currency')
    ent1.delete(0, END)
    ent1.focus()
    results.set('')


Button(root, text="CONVERT", borderwidth=3, bg='white', command=perform).place(x=180, y=430)
Button(root, text="EXIT", borderwidth=3, bg='white', command=kill).place(x=281, y=480)
Button(root, text="CLEAR", borderwidth=3, bg='white', command=clear).place(x=100, y=480)


root.mainloop()  # continuously runs program in window
