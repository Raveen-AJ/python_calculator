import customtkinter
import re
from display import Display
from number_pad import NumberPad
from utils import is_number, is_operator


class Calculator(customtkinter.CTkFrame):
    def __init__(self, app, display_height):
        super().__init__(master=app)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.display = Display(cal=self, height=display_height)
        self.display.grid(row=0, column=0, padx=10, pady=10, sticky="nwne")

        self.number_pad = NumberPad(
            cal=self,
            callback=self._number_pad_callback
        )
        self.number_pad.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.number_pad.configure(fg_color="transparent")

    def _number_pad_callback(self, x):
        if x == "()":
            return
        if x == "AC":
            self.display.clear()
            return
        if x == "X":
            self.display.row1_remove_char()
            return

        if is_operator(x):
            if self.display.row1_get_last_char() == x:
                return
            if is_operator(self.display.row1_get_last_char()):
                self.display.row1_set_last_char(x)
                return
            self.display.row1_add_char(x)
            return

        if x == "=":
            try:
                self.display.set_row2(self.display.get_row1())
                self.display.set_row1(str(eval(self.display.get_row1())))
            except SyntaxError:
                return
            return

        last_value = re.split(r'[+\-*/%]', self.display.get_row1())[-1]
        if not is_number(last_value + x):
            return

        self.display.row1_add_char(x)
