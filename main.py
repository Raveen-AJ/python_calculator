import customtkinter
from calculator import Calculator

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class Main(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("450x650")
        # self.minsize(450, 650)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.calculator = Calculator(self, 200)
        self.calculator.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")


if __name__ == "__main__":
    app = Main()
    app.mainloop()
