import customtkinter


number_pad_grid = [["AC", "()", "%", "/"],
                   ["7", "8", "9", "*"],
                   ["4", "5", "6", "-"],
                   ["1", "2", "3", "+"],
                   ["0", ".", "X", "="]]


class NumberPad(customtkinter.CTkFrame):
    def __init__(self, cal, callback):
        super().__init__(master=cal)

        self.grid_columnconfigure((0, 1, 2, 3), weight=1)
        self.grid_rowconfigure((0, 1, 2, 3, 4), weight=1)

        for row in range(0, 5):
            for col in range(0, 4):
                self.button = Button(self, row, col, number_pad_grid[row][col],
                                     callback=callback)


class Button(customtkinter.CTkButton):
    def __init__(self, number_pad, row, col, text, color="gray", callback=None):
        super().__init__(master=number_pad)
        self.configure(text=text, fg_color=color)
        self.grid(row=row, column=col, padx=1, pady=1, sticky="nsew")
        self.configure(command=lambda: callback(text))
