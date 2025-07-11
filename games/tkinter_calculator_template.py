# Sample template to work on https://dailypythonprojects.substack.com/p/python-project-build-a-calculator
import tkinter as tk

class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        # Creating a list of buttons
        self.button_lst = ["7", "8", "9", "/", "4", "5", "6", "*",
                           "1", "2", "3", "-", "0", ".", "=", "+"]
        # Display a title
        self.main_window.title('Calculator')

        # Create the top frame with the entry field
        self.top_frame = tk.Frame(self.main_window)
        self.calc_field = tk.Entry(self.top_frame, width=55)
        self.calc_field.pack(side='left')

        # Create the bottom frame to hold buttons
        self.bottom_frame = tk.Frame(self.main_window)
        self.last_frame = tk.Frame(self.main_window)

        # Total buttons 17 last one on a separate frame
        total_buttons = 17
        count = 0
        for i in range(total_buttons):
            if i < total_buttons - 1:
                button = tk.Button(self.bottom_frame, text=self.button_lst[i], width=10, height=1)
                row = i // 4
                col = i % 4
                button.grid(row=row, column=col, padx=5, pady=5)
                count += 1
            else:
                button = tk.Button(self.last_frame, text="C", width=30, height=1)
                button.grid(row=4, column=0, padx=5, pady=5)

        # Pack the three frames
        self.top_frame.pack(pady=10)
        self.bottom_frame.pack()
        self.last_frame.pack(side='left')

        tk.mainloop()

if __name__ == '__main__':
    my_gui = MyGUI()
