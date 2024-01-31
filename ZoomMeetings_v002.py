import tkinter as tk
import webbrowser


class ZoomMeetings:
    def __init__(self, master):
        self.master = master
        self.file = open("C:/Users/halta/Desktop/Zoom Meeting Links.txt")

        chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
        webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
        elems = self.parse_file()
        master.title("Zoom Meetings")
        master.geometry("300x250")

        buttons = dict()
        for i in range(len(elems)):
            button = tk.Button(master, text=elems[i][0], command=lambda a=i: self.go_to_url(elems[a][1]))
            buttons[i] = button.pack(pady=5)

    def parse_file(self):
        master_list = []
        for line in self.file:
            colon = line.find(':') + 1
            master_list.append([line[0: colon], line[colon: -1].split()])
        return master_list

    @staticmethod
    def go_to_url(url):
        webbrowser.get('chrome').open_new_tab(url[0])


root = tk.Tk()
my_gui = ZoomMeetings(root)
root.mainloop()
my_gui.file.close()
