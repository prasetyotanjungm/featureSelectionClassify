import csv
import tkinter as tk
import os

os.chdir("D:/Bahan Belajar/SKRIPSI COY")
root = tk.Tk()

currencies = {}

with open("dataClass30000.csv") as f:
    next(f, None)  # Skip the header.
    reader = csv.reader(f, delimiter=',')
    for country, code in reader:
        currencies['{country} {code}'.format(country = country,code = code)] = code

listbox = tk.Listbox(root)
for key in currencies:
    listbox.insert('end', key)
listbox.grid(row=0, column=0)
listbox.bind('<Key-Return>', lambda event: print(currencies[listbox.selection_get()]))

tk.mainloop()