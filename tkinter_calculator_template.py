# Sample template to work on https://dailypythonprojects.substack.com/p/python-project-build-a-calculator
import tkinter as tk

class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()

        # Display a title
        self.main_window.title('Calculator')

        # Create the top frame with the entry field
        self.top_frame = tk.Frame(self.main_window)
        self.calc_field = tk.Entry(self.top_frame, width=55)
        self.calc_field.pack(side='left')

        # Create the bottom frame to hold buttons
        self.bottom_frame = tk.Frame(self.main_window)
        self.last_frame = tk.Frame(self.main_window)

        # Add 17 buttons in a 4-column grid
        total_buttons = 17
        for i in range(total_buttons):
            if i != 16:
                button = tk.Button(self.bottom_frame, text=str(i+1), width=10, height=1)
                row = i // 4
                col = i % 4
                button.grid(row=row, column=col, padx=5, pady=5)
            else:
                button = tk.Button(self.last_frame, text="C", width=30, height=1)
                button.grid(row=4, column=0, padx=5, pady=5)

        # Pack the three frames
        self.top_frame.pack(pady=10)
        self.bottom_frame.pack()
        self.last_frame.pack(side='left', pady=10)

        tk.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
