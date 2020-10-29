import tkinter as tk

def calculate():
    print("Show GCD!!!")

root = tk.Tk()
root.title("GCD")
root.geometry('300x200')

root.Btn1 = tk.Button(root)
root.Btn1["text"] = "Calculate GCD"
root.Btn1.pack(side = "bottom", pady = 20)
root.Btn1["command"] = calculate

root.Txt1 = tk.
