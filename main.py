import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
from data_import import import_csv_to_dataframe
from data_display import display_dataframe
from filtering_and_selection import filter_dataframe
from data_visualization import create_plot
from export import save_dataframe_to_pickle

# Import other necessary modules and functions as you develop the other scripts

class MainApplication(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.master = master
        self.pack()
        self.create_widgets()
        self.tree = ttk.Treeview(self)
        self.tree.pack(fill="both", expand=True)


    def create_widgets(self):
        # Create and place your widgets here, such as buttons, labels, etc.
        # For example, a button to open a file dialog for importing CSV files:
        self.import_button = tk.Button(self, text="Import CSV", command=self.import_csv)
        self.import_button.pack()
        self.filter_label = tk.Label(self, text="Filter by column 'A':")
        self.filter_label.pack()

        self.filter_entry = tk.Entry(self)
        self.filter_entry.pack()

        self.apply_filter_button = tk.Button(self, text="Apply Filter", command=self.apply_filter)
        self.apply_filter_button.pack()
        self.plot_label = tk.Label(self, text="Create Plot:")
        self.plot_label.pack()

        plot_types = ['scatter', 'line', 'bar', 'hist']
        self.plot_type_var = tk.StringVar(self)
        self.plot_type_var.set(plot_types[0])
        self.plot_option_menu = tk.OptionMenu(self, self.plot_type_var, *plot_types)
        self.plot_option_menu.pack()

        self.x_column_label = tk.Label(self, text="X Column:")
        self.x_column_label.pack()

        self.x_column_var = tk.StringVar(self)
        self.x_column_option_menu = tk.OptionMenu(self, self.x_column_var, *self.dataframe.columns)
        self.x_column_option_menu.pack()

        self.y_column_label = tk.Label(self, text="Y Column:")
        self.y_column_label.pack()

        self.y_column_var = tk.StringVar(self)
        self.y_column_option_menu = tk.OptionMenu(self, self.y_column_var, *self.dataframe.columns)
        self.y_column_option_menu.pack()

        self.create_plot_button = tk.Button(self, text="Create Plot", command=self.create_plot)
        self.create_plot_button.pack()

        self.save_button = tk.Button(self, text="Save Filtered Dataframe", command=self.save_filtered_dataframe)
        self.save_button.pack()




    def import_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.dataframe = import_csv_to_dataframe(file_path)
            display_dataframe(self.tree, self.dataframe)

    def apply_filter(self):
        filter_value = self.filter_entry.get()
        if self.dataframe is not None and filter_value:
            filters = {'A': filter_value}  # Assuming you want to filter by column 'A'
            filtered_dataframe = filter_dataframe(self.dataframe, filters)
            # Update the Treeview with the filtered_dataframe
            self.tree.delete(*self.tree.get_children())  # Remove the existing rows
            display_dataframe(self.tree, filtered_dataframe)
    
    def create_plot(self):
        plot_type = self.plot_type_var.get()
        x_column = self.x_column_var.get()
        y_column = self.y_column_var.get()

        if self.dataframe is not None and plot_type and x_column and y_column:
            create_plot(self.dataframe, plot_type, x_column, y_column)
    
    def save_filtered_dataframe(self):
        if self.filtered_dataframe is not None:  # Assuming you have saved filtered dataframe in self.filtered_dataframe
            file_path = filedialog.asksaveasfilename(defaultextension=".pkl", filetypes=[("Pickle files", "*.pkl")])
            if file_path:
                success = save_dataframe_to_pickle(self.filtered_dataframe, file_path)
                if success:
                    print("Filtered dataframe saved successfully.")
                else:
                    print("Error saving filtered dataframe.")



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Pandas Dataframe GUI")
    root.geometry("800x600")
    app = MainApplication(master=root)
    app.mainloop()
