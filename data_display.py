import tkinter as tk
from tkinter import ttk
import pandas as pd

def display_dataframe(tree, dataframe):
    tree["columns"] = list(dataframe.columns)
    tree["show"] = "headings"

    # Create the column headings
    for column in dataframe.columns:
        tree.heading(column, text=column)
        tree.column(column, anchor="center", minwidth=50, stretch=True)

    # Insert the data rows
    for index, row in dataframe.iterrows():
        tree.insert("", "end", values=tuple(row))

    tree.pack(fill="both", expand=True)
