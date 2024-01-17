import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import requests
import json

root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.resizable(0, 0)
root.configure(background="#232323")

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = from_currency_input.get()
    to_currency = to_currency_input.get()

    try:
        # Make a request to the API
        response = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_00dKIlcSwaCIPME3BV6BeSpuec83nhWjPUjqCYfb")
        response.raise_for_status()  # Raise an exception for non-2xx status codes

        data = response.json()
        print(data)

        if response.status_code == 200:
            conversion_rate = data['data'][to_currency]
            converted_amount = round(amount * conversion_rate, 2)
            result_input.config(text=f"{amount} {from_currency} = {converted_amount} {to_currency}")
        else:
            messagebox.showerror("Error", "Failed to retrieve conversion rates.")
    except (requests.exceptions.RequestException, json.JSONDecodeError) as e:
        messagebox.showerror("Error", str(e))

    # retrieveconversion rates from the API
    conversion_rates = data.get('data', {})

    # conversion rates to a JSON file
    with open("conversion_rates.json", "w") as file:
        json.dump(conversion_rates, file)

def clear_fields():
    amount_entry.delete(0, tk.END)
    from_currency_input.set("")
    to_currency_input.set("")
    result_input.config(text="")

def exit_app():
    root.destroy()


# top for the background of the title
top = tk.Frame(root, bg="#028a0f", width=500, height=79)
top.grid()

# title
title = tk.Label(root, text="EXCHANGE RATES",  font=("Courier", 28, "bold"), fg="#FFD700", bg="#028a0f") 
title.place(x=85, y=15)

# label and entry for the amount
amount_label = tk.Label(root, text="Enter Amount:", font=("Courier", 12), fg="#ffffff", bg="#232323")
amount_label.place(x=195, y=90)
amount_entry = tk.Entry(root, width=16, font=("Courier", 12))
amount_entry.place(x=175, y=115)

# from currency label and input
from_currency_label = tk.Label(root, text="From:", font=("Courier", 12), fg="#ffffff", bg="#232323")
from_currency_label.place(x=55, y=155)
from_currency_input = ttk.Combobox(root, width=12, font=("Courier", 12))
from_currency_input['values'] = ['CAD', 'EUR', 'GBP', 'HKD', 'INR', 'JPY', 'KRW', 'PHP', 'USD']
from_currency_input.place(x=110, y=155)

# to currency label and input
to_currency_label = tk.Label(root, text="To:", font=("Courier", 12), fg="#ffffff", bg="#232323")
to_currency_label.place(x=265, y=155)
to_currency_input = ttk.Combobox(root, width=12, font=("Courier", 12))
to_currency_input['values'] = ['CAD', 'EUR', 'GBP', 'HKD', 'INR', 'JPY', 'KRW', 'PHP', 'USD']
to_currency_input.place(x=300, y=155)

# convert, clear, result, exit button
convert = tk.Button(root, width=12, font=("Courier", 12), text="Convert", bg="blue", fg="#ffffff", command=convert_currency)
convert.place(x=190, y=210)
clear = tk.Button(root, width=12, font=("Courier", 12), text="Clear", bg="orange", fg="#ffffff", command=clear_fields)
clear.place(x=190, y=250)
result_input = tk.Label(root, text="", font=("Courier", 12), fg="#ffffff", bg="#232323")
result_input.place(x=150, y=290)
exit = tk.Button(root, text="Exit", width=12, font=("Courier", 12), bg="red", fg="#ffffff", command=exit_app)
exit.place(x=190, y=330)

# credit of my full name
credit = tk.Label(root, text="Made by: Errol Renselle B. Caranza", font=("Courier", 10), fg="#ffffff", bg="#232323")
credit.place(x=135, y=375)

root.mainloop()