import tkinter as tk


class StackCalculator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Minecraft Stack Calculator")
        self.root.minsize(250, 50)
        self.tk_var = tk.StringVar()
        self.tk_var.set("blocks = 0 stacks and 0 blocks.")

        self.e1 = tk.Entry(self.root, width=4)
        self.e1.place(x=10, y=20)
        l1 = tk.Label(self.root, textvariable=self.tk_var)
        l1.place(x=40, y=20)

        self.update()
        self.root.mainloop()

    def update(self):
        def calculate():
            total = int(self.e1.get())
            num_stacks = int(total / 64)
            num_blocks = int(total - (num_stacks * 64))
            return num_stacks, num_blocks

        label_text = "blocks = 0 stacks and 0 blocks"

        if self.e1.get() != "":
            output = calculate()
            label_text = "blocks = " + str(output[0]) + " stacks and " + str(output[1]) + " blocks."
        self.tk_var.set(label_text)

        self.root.after(100, self.update)


SC = StackCalculator()
