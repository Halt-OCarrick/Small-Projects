from tkinter import *
from tkinter.ttk import *
from functools import partial
import math


class HitDiceCalculator:
    def __init__(self):
        self.hit_die = 0
        self.con_mod = 0
        self.hp_range = (0, 0)
        self.possible_outputs = []
        self.output = ""

    def assign(self, con, size, cr):
        modifiers = {
            -3: -6,
            -2: -4,
            -1: -4,
            0: -5,
            1: -5,
            2: -4,
            3: -4,
            4: -3,
            5: -3,
            6: -2,
            7: -2,
            8: -1,
            9: -1,
            10: 0,
            11: 0,
            12: 1,
            13: 1,
            14: 2,
            15: 2,
            16: 3,
            17: 3,
            18: 4,
            19: 4,
            20: 5,
            21: 5,
            22: 6,
            23: 6,
            24: 7,
            25: 7,
            26: 8,
            27: 8,
            28: 9,
            29: 9,
            30: 10
        }
        die_size = {
            "Tiny": 4,
            "Small": 6,
            "Medium": 8,
            "Large": 10,
            "Huge": 12,
            "Gargantuan": 20
        }
        hp_range = {
            0: (1, 6),
            0.125: (7, 35),
            0.25: (36, 49),
            0.5: (50, 70),
            1: (71, 85),
            2: (86, 100),
            3: (101, 115),
            4: (116, 130),
            5: (131, 145),
            6: (146, 160),
            7: (161, 175),
            8: (176, 190),
            9: (191, 205),
            10: (206, 220),
            11: (221, 235),
            12: (236, 250),
            13: (251, 265),
            14: (266, 280),
            15: (281, 295),
            16: (296, 310),
            17: (311, 325),
            18: (326, 340),
            19: (341, 355),
            20: (356, 400),
            21: (401, 445),
            22: (446, 490),
            23: (491, 535),
            24: (536, 580),
            25: (581, 625),
            26: (626, 670),
            27: (671, 715),
            28: (716, 760),
            29: (761, 805),
            30: (806, 850)
        }

        self.con_mod = modifiers[int(con)]
        self.hit_die = die_size[str(size)]
        self.hp_range = hp_range[float(cr)]

    def calculate(self):
        avg = float((self.hit_die + 1) / 2)
        num_hit_dice = 0
        total_hp = (num_hit_dice * avg) + (num_hit_dice * self.con_mod)

        while total_hp < self.hp_range[1]:
            num_hit_dice += 1
            total_hp = math.ceil((num_hit_dice * avg) + (num_hit_dice * int(self.con_mod)))
            if self.hp_range[0] <= total_hp <= self.hp_range[1]:
                self.possible_outputs.append(num_hit_dice)

    def to_string(self):
        list_out = []
        avg = float((self.hit_die + 1) / 2)
        for i in range(len(self.possible_outputs)):
            n = self.possible_outputs[i]
            average = math.ceil((n * float(avg)) + (n * int(self.con_mod)))
            str_out = "(" + str(average) + ")" + " " + str(n) + "d" + str(self.hit_die) + " + " + str(self.con_mod * n)
            list_out.append(str_out)

        self.output = "Hit Point Range: " + str(self.hp_range[0]) + "-" + str(self.hp_range[1]) + "\n"
        for i in range(len(list_out)):
            self.output += list_out[i] + "\n"

        self.possible_outputs.clear()

    def on_click(self, con_text, size_combo, cr_text, output_lbl):
        self.assign(con_text.get(), size_combo.get(), cr_text.get())
        self.calculate()
        self.to_string()
        output_lbl.config(text=self.output)

    def create_gui(self):
        root = Tk()
        root.title("DM Tools")
        root.geometry("350x200")

        # size drop down menu
        size_lbl = Label(root, text="Size: ")
        size_lbl.grid(sticky="w", row=0, column=0)

        size_combo = Combobox(root)
        size_combo['values'] = ("Tiny", "Small", "Medium", "Large", "Huge", "Gargantuan")
        size_combo.current(0)
        size_combo.grid(sticky="e", row=0, column=1)

        # CON score text box
        con_lbl = Label(root, text="CON Score: ")
        con_lbl.grid(sticky="w", row=1, column=0)

        con_text = Entry(root, width=10)
        con_text.insert(END, '16')
        con_text.grid(sticky="e", row=1, column=1)

        # CR text box
        cr_lbl = Label(root, text="Monster CR: ")
        cr_lbl.grid(sticky="w", row=2, column=0)

        cr_text = Entry(root, width=10)
        cr_text.insert(END, '5')
        cr_text.grid(sticky="e", row=2, column=1)

        output_lbl = Label(root, text="")
        output_lbl.grid(sticky="w", row=4, column=0)

        on_click_partial = partial(self.on_click, con_text=con_text, size_combo=size_combo, cr_text=cr_text,
                                   output_lbl=output_lbl)

        confirm = Button(root, text="Calculate", command=on_click_partial)
        confirm.grid(sticky="w", row=3, column=0)

        root.mainloop()


if __name__ == '__main__':
    monster = HitDiceCalculator()
    monster.create_gui()
