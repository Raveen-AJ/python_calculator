import re

import customtkinter

from display import Display
from number_pad import NumberPad
from utils import is_operator


class Calculator(customtkinter.CTkFrame):
    def __init__(self, app, display_height):
        super().__init__(master=app)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.display = Display(cal=self, height=display_height)
        self.display.set_row1("0")
        self.display.grid(row=0, column=0, padx=10, pady=10, sticky="nwne")

        self.number_pad = NumberPad(
            cal=self,
            callback=self._number_pad_callback
        )
        self.number_pad.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
        self.number_pad.configure(fg_color="transparent")

        self.expression = ""

    def _number_pad_callback(self, btn):
        if self.display.get_row2() != "":
            self._clear_display()

        if btn == "()":
            return
        if btn == "AC":
            self._clear_display()
            return
        if btn == "DEL":
            self._on_click_delete()
            return
        if btn == ".":
            self._on_click_dot()
            return
        if is_operator(btn):
            self._on_click_operator(btn)
            return
        if btn == "=":
            self._calculate()
            return

        self._on_click_number(btn)

    def _clear_display(self):
        self.display.clear()
        self.display.set_row1("0")
        self.expression = ""

    def _on_click_delete(self):
        if len(self.expression) == 0:
            return
        if len(self.expression) == 1:
            self.expression = ""
            self.display.set_row1("0")
            return
        self._update(self.expression[:-1])

    def _on_click_operator(self, operator):
        if self.expression == "" or self.expression[-1] == ".":
            return
        expression_last_char = self.expression[-1]
        if expression_last_char == operator:
            return
        if is_operator(expression_last_char):
            new_expression = self.expression[:-1] + operator
        else:
            new_expression = self.expression + operator
        self._update(new_expression)

    def _on_click_dot(self):
        if self.expression == "":
            return
        last_value = re.split(r'[+\-*/%]', self.expression)[-1]
        if last_value == "" or "." in last_value:
            return
        self._update(self.expression + ".")

    def _on_click_number(self, num):
        if num == "0":
            last_value = re.split(r'[+\-*/%]', self.expression)[-1]
            if last_value == "":
                return
        self._update(self.expression + num)

    def _calculate(self):
        try:
            if len(self.expression) == 0:
                return
            if self.expression[-1] == ".":
                raise SyntaxError()
            self.display.set_row1(str(eval(self.expression))[:12])
            self.display.set_row2(self.expression)
            self.expression = ""
        except SyntaxError:
            return

    def _update(self, expression):
        self.expression = expression
        self.display.set_row1(expression)
