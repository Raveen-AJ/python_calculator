import customtkinter


class Display(customtkinter.CTkFrame):
    def __init__(self, cal, height):
        super().__init__(master=cal, height=height)
