from Analyzer import analyzer
from tkinter import *
from tkinter.ttk import Label

def main():

    def buttonClick():

        text = inputText.get("1.0", "end-1c")
        returned = analyzer.main(text)

        if returned == "0":
            window.config(bg="#D64933")
            Label(window, text="Negative", font=("Courier", 25), justify="center").place(x=430, y=160)
        else:
            window.config(bg="#85B404")
            Label(window, text="Positive", font=("Courier", 25), justify="center").place(x=430, y=160)

    WIDTH, HEIGHT = 1000, 700

    window = Tk(className="SenPy - Text Sentiment Analysis, built using Python")

    window.config(bg="#5386E4")

    window.geometry(f"{WIDTH}x{HEIGHT}")
    window.resizable(False, False)

    Label(window, text="SenPy", font=("Courier", 30), justify="center").place(x=20, y=20)
    Label(window, text="Sentiment Analysis in Python", font=("Courier", 20), justify="center").place(x=20, y=55)

    Label(window, text="Sid R 2021", font=("Courier", 20), justify="center").place(x=850, y=20)

    Button(window, text="Analyze!", command=buttonClick, width=50, font=("Courier", 30)).place(x=20, y=100)

    inputText = Text(window, height=500, width=500)
    inputText.place(x=0, y=250)
    inputText.insert('1.0', 'Insert the text you want to analyse here!')

    window.mainloop()

main()