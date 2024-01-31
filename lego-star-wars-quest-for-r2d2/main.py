import sys
import os
import tkinter as tk
import subprocess
import platform


# Check for windows OS
def check_for_windows():
    platform_list = ['Windows', 'Darwin']
    system = platform.system()
    if system in platform_list:
        return system
    else:
        return "This file may not be compatible with your current OS.\nWould you like to continue?"


# Check if correct version of internet explorer exists
def check_for_internet_explorer():
    path = os.path.join(os.getcwd(), "Internet Explorer/ie.vbs")
    if os.path.exists(path):
        return 1
    else:
        return "No version of Internet Explorer installed.\nPlease install Internet explorer and try again"


# Install correct version of Unity Web Player
def install_unity_web_player():
    if os.path.exists('UnityWebPlayerDevelopment.exe'):
        os.system('UnityWebPlayerDevelopment.exe')
        return 1
    else:
        return "No file UnityWebPlayerDevelopment.exe found."


# Run unity3d file with internet explorer
def run_unity3d_file():
    game_path = os.path.abspath("Launcher.html")
    os.chdir("Internet Explorer")
    os.system( + game_path)


# GUI for errors
def gui_for_errors(error_message):
    root = tk.Tk()
    root.title = "Lego Star Wars: Quest for R2-D2 | Setup"
    root.geometry("600x300")
    root.bind('<Escape>', lambda e: exit())
    root.protocol("WM_DELETE_WINDOW", lambda: exit())

    w = tk.Label(root, text=error_message)
    w.pack()

    b = tk.Button(root, text="Quit", command=lambda: exit())
    b.pack()
    if error_message[-1] == '?':
        b2 = tk.Button(root, text="Continue", command=lambda: root.destroy())
        b2.pack()

    root.mainloop()


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    out = check_for_windows()
    if len(out) > 10:
        gui_for_errors(out)
    else:
        print("OS: " + out)

    out = check_for_internet_explorer()
    if isinstance(out, str):
        gui_for_errors(out)
    else:
        print("Found: Internet Explorer")

    out = install_unity_web_player()
    if isinstance(out, str):
        gui_for_errors(out)
    else:
        print("Installed: Unity Web Player")

    run_unity3d_file()
