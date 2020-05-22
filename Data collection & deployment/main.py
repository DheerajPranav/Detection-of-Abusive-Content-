import tkinter as tk
from models import predict
from sklearn.tree import DecisionTreeClassifier
from PIL import ImageTk, Image
root = tk.Tk()
root.geometry("1280x720+30+0")
root.config(bg = "white")
root.title("Detecting abusive content")
root.resizable(False, False)
# from models import prediction


def prediction(frame,answer, name):
    x = name.get()
    name.delete(0, "end")

    if len(x) == 0 or x == "None":
        answer.config(text="please fill every field", fg="red")
    else:
        out = predict(x)
        # out = x

        if out == 1:
            answer.config(text="ABUSIVE", fg="red")

        else:
            answer.config(text="NON ABUSIVE", fg="green")


class gui:
    head_font = ("Arial", 36, "bold")
    font = ("Arial", 20, "bold")
    font2 = ("Arial", 16)
    values = range(1,11)
    ex1 = 50
    ex2 = 200
    ex3 = 620
    ex4 = 950

    def __init__(self,root):
        frame = tk.Frame(root, bg = "light yellow")
        frame.place(x = 0, y = 0, width = 1280, height = 720)
        self.img = ImageTk.PhotoImage(Image.open("pics'.jpg"))
        tk.Label(frame, image=self.img).place(x=1050, y=10)

        tk.Label(frame, text = "Detecting abusive content", font = self.head_font, bg = "white", borderwidth=2, relief="solid").place(x = 230, y = 50)
        tk.Label(frame, text = "Enter text", font = self.font, bg = "white").place(x = self.ex1, y = 250)
        name = tk.Entry(frame, font = self.font2, bg = "silver")
        name.place(x = self.ex2, y = 160, height = 100, width = 385)
        name.focus()

        answer = tk.Label(frame, font = self.head_font, fg = "green", bg = "white")
        answer.place(x = self.ex1 , y = 500)
        predict = tk.Button(frame, text = "Detect", fg = "green", borderwidth=2, relief="raised", font = self.head_font, command = lambda : prediction(frame, answer, name))
        predict.place(x = 970, y = 420, width = 250, height = 250)




GUI = gui(root)
root.mainloop()
