import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self, fg_color = None, **kwargs) -> None:
        super().__init__(fg_color, **kwargs)
        ctk.set_appearance_mode("dark")
        self.create_elements()
    
    def create_elements(self) -> None:
        self.buttons = []
        for i in range(20):
            row_buttons = []
            for j in range(20):
                button = ctk.CTkButton(
                    master=self,
                    text="",
                    width=30,
                    command=lambda x=i, y=j: self.change_color(x, y),  # Pass row and column index
                    fg_color="blue",  # Initial color
                    hover_color="lightblue"  # Hover color
                )
                button.grid(row=i, column=j, padx=1, pady=1)  # Arrange in a grid
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def change_color(self, row, col):
        # Change the color of the button dynamically
        self.buttons[row][col].configure(fg_color="green")  # Change to desired color



root = App()
root.mainloop()