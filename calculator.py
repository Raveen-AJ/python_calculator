import customtkinter
from display import Display
from number_pad import NumberPad


class Calculator(customtkinter.CTkFrame):
    def __init__(self, app, display_height):
        super().__init__(master=app)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.display = Display(cal=self, height=display_height)
        self.display.grid(row=0, column=0, padx=10, pady=10, sticky="nwne")

        self.number_pad = NumberPad(cal=self, callback=self._number_pad_callback)
        self.number_pad.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.number_pad.configure(fg_color="transparent")

    def _number_pad_callback(self, x):
        print(x)
