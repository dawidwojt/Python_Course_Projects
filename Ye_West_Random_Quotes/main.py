from tkinter import *
import requests
return_quote = "Click Kanye face to generate Kanye quote"


def get_quote():
    global return_quote
    response = requests.get(url="https://api.kanye.rest")
    quote = response.json()
    return_quote = quote["quote"]
    canvas.itemconfig(quote_text, text=return_quote)


# def change_quote():
#     canvas.config(quote_text, text=get_quote())


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text=return_quote, width=250, font=("Arial", 20, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
