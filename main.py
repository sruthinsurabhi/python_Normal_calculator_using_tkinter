import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.geometry("500x500")
        master.configure(bg='#ada692')
        master.title("Calculator")

        # Entry field for displaying the result
        self.result_display = tk.Text(master, width=20, height=3, font=('Arial', 16))
        self.result_display.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        # Create buttons for the calculator
        self.create_button("7", 2, 0)
        self.create_button("8", 2, 1)
        self.create_button("9", 2, 2)
        self.create_button("/", 2, 3)
        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)
        self.create_button("*", 3, 3)
        self.create_button("1", 4, 0)
        self.create_button("2", 4, 1)
        self.create_button("3", 4, 2)
        self.create_button("-", 4, 3)
        self.create_button("0", 5, 0)
        self.create_button(".", 5, 1)
        self.create_button("C", 5, 2)
        self.create_button("+", 5, 3)
        self.create_button("=", 6, 0, 1, 4)

    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 16), command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, padx=5, pady=5)
        button.config(bg="#a18948")

    def button_click(self, text):
        if text == "=":
            # Evaluate the expression entered by the user
            try:
                result = eval(self.result_display.get("1.0", tk.END))
            except:
                result = "Error"
            self.result_display.delete("1.0", tk.END)
            self.result_display.insert("1.0", result)
        elif text == "C":
            # Clear the entry field
            self.result_display.delete("1.0", tk.END)
        else:
            # Append the clicked button's text to the entry field
            self.result_display.insert(tk.END, text)

window= tk.Tk()
calculator = Calculator(window)
window.mainloop()
