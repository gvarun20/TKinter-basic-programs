import tkinter as tk

class CurrencyConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")

        self.amount_var = tk.DoubleVar()
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.result_var = tk.StringVar()

        # Exchange rates (sample rates)
        self.exchange_rates = {
            'USD': {'EUR': 0.85, 'INR': 75.0},
            'EUR': {'USD': 1.18, 'INR': 88.5},
            'INR': {'USD': 0.013, 'EUR': 0.0113}
        }

        # GUI components
        tk.Label(root, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.amount_var).grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="From Currency:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.from_currency_var).grid(row=1, column=1, padx=10, pady=10)

        tk.Label(root, text="To Currency:").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(root, textvariable=self.to_currency_var).grid(row=2, column=1, padx=10, pady=10)

        tk.Button(root, text="Convert", command=self.convert_currency).grid(row=3, column=0, columnspan=2, pady=10)

        tk.Label(root, text="Result:").grid(row=4, column=0, padx=10, pady=10)
        tk.Label(root, textvariable=self.result_var).grid(row=4, column=1, padx=10, pady=10)

    def convert_currency(self):
        amount = self.amount_var.get()
        from_currency = self.from_currency_var.get().upper()
        to_currency = self.to_currency_var.get().upper()

        try:
            rate = self.exchange_rates[from_currency][to_currency]
            result = amount * rate
            self.result_var.set(f"{amount} {from_currency} = {result:.2f} {to_currency}")
        except KeyError:
            self.result_var.set("Error: Invalid currency pair")

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverterApp(root)
    root.mainloop()
