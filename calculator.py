import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("380x400")

# Input field
entry = tk.Entry(window, width=16, font=('Arial', 30), bd=8, relief='ridge', justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Button click function
def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == '=':
        tk.Button(window, text=text, width=5, height=2, command=calculate).grid(row=row, column=col)
    else:
        tk.Button(window, text=text, width=5, height=2, command=lambda val=text: click(val)).grid(row=row, column=col)

# Clear button
tk.Button(window, text='C', width=5, height=2, command=clear).grid(row=5, column=0, columnspan=4, sticky="we")

# Run the app
window.mainloop()








  



