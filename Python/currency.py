import tkinter as tk
from tkinter import ttk, messagebox

# Dictionary with currency conversion rates relative to USD
currency_rates = {
    'USD': 1.0,
    'EUR': 0.91,
    'GBP': 0.78,
    'INR': 83.15,
    'JPY': 151.72,
    'CAD': 1.35,
    'AUD': 1.53,
}

# Function to convert currency
def convert_currency():
    try:
        amount = float(entry_amount.get())  # Get the amount entered by user
        from_currency = combo_from.get()    # Get the currency to convert from
        to_currency = combo_to.get()        # Get the currency to convert to

        if from_currency == "" or to_currency == "":
            messagebox.showwarning("Selection Error", "Please select both currencies.")
            return

        # Conversion calculation
        converted = amount / currency_rates[from_currency] * currency_rates[to_currency]
        label_result.config(text=f"{amount:.2f} {from_currency} = {converted:.2f} {to_currency}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid number.")

# Main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x300")
root.resizable(False, False)

# Title label
title = tk.Label(root, text="Currency Converter", font=("Arial", 16, "bold"))
title.pack(pady=10)

# Amount entry
entry_amount = tk.Entry(root, font=("Arial", 14), justify='center')
entry_amount.pack(pady=10)
entry_amount.insert(0, "1")  # Default value

# From currency dropdown
combo_from = ttk.Combobox(root, values=list(currency_rates.keys()), font=("Arial", 12))
combo_from.set("USD")  # Default value
combo_from.pack(pady=5)

# To currency dropdown
combo_to = ttk.Combobox(root, values=list(currency_rates.keys()), font=("Arial", 12))
combo_to.set("EUR")  # Default value
combo_to.pack(pady=5)

# Convert button
btn_convert = tk.Button(root, text="Convert", font=("Arial", 12), command=convert_currency)
btn_convert.pack(pady=10)

# Result label
label_result = tk.Label(root, text="", font=("Arial", 14))
label_result.pack(pady=10)

# Start the GUI loop
root.mainloop()
