import customtkinter


class Display(customtkinter.CTkFrame):
    def __init__(self, cal, height):
        super().__init__(master=cal, height=height)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.label_row1 = customtkinter.CTkLabel(
            self,
            text="",
            height=height // 2,
            font=("Arial", 63),
            anchor="e"
        )
        self.label_row2 = customtkinter.CTkLabel(
            self,
            text="",
            height=height // 2,
            font=("Arial", 63),
            anchor="e"
        )
        self.label_row1.grid(row=1, column=0, sticky="se")
        self.label_row2.grid(row=0, column=0, sticky="se")

    def clear(self):
        self.label_row1.configure(text="")
        self.label_row2.configure(text="")

    def set_row1(self, text):
        self.label_row1.configure(text=text)

    def get_row2(self):
        return self.label_row2.cget("text")

    def set_row2(self, text):
        self.label_row2.configure(text=text)
