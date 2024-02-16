import customtkinter


class Display(customtkinter.CTkFrame):
    def __init__(self, cal, height):
        super().__init__(master=cal, height=height)
        self.grid_rowconfigure((0, 1), weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.label_row1 = customtkinter.CTkLabel(
            self,
            text="0",
            height=height // 2,
            font=("Arial", 42)
        )
        self.label_row2 = customtkinter.CTkLabel(
            self,
            text="",
            height=height // 2,
            font=("Arial", 42)
        )
        self.label_row1.grid(row=1, column=0, sticky="se")
        self.label_row2.grid(row=0, column=0, sticky="se")

    def row1_add_char(self, char):
        if self.label_row1.cget("text") == "0":
            self.label_row1.configure(text=char)
            return
        self.label_row1.configure(text=self.label_row1.cget("text") + char)

    def clear(self):
        self.label_row1.configure(text="0")
        self.label_row2.configure(text="")

    def row1_remove_char(self):
        current = self._row1_get_current()
        new = current[:-1]
        self.label_row1.configure(text=new)

    def get_row1(self):
        return self._row1_get_current()

    def set_row1(self, text):
        self.label_row1.configure(text=text)

    def row1_set_last_char(self, char):
        current = self._row1_get_current()[:-1]
        new = current + char
        self.label_row1.configure(text=new)

    def row1_get_last_char(self):
        return self._row1_get_current()[-1]

    def _row1_get_current(self) -> str:
        return self.label_row1.cget("text")

    def set_row2(self, text):
        self.label_row2.configure(text=text)
