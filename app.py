import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=500)
canvas.grid(columnspan=3, rowspan=4)

# logo
logo = Image.open('logo.png')
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image= logo)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# instructions
instructions = tk.Label(root, text="Select a PDF file on your computer to Extract all it's text", font="Raleway")
instructions.grid(columnspan=3, column=0, row=1)

# browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(root, textvariable=browse_text, command=lambda:open_file(), font="Raleway", bg="#20bebe", fg="#fff", height=2, width=10)
browse_text.set("Browse")
browse_btn.grid(column=1, row=2)


canvas = tk.Canvas(root, width=600, height=250)
canvas.grid(columnspan=3)

def open_file():
    browse_text.set("Loading...")
    file = askopenfile(parent=root, mode='rb', title="Chose a file", filetype=[("pdf file", "*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page= read_pdf.getPage(0)
        page_contect = page.extractText()
        

        # text box

        text_box = tk.Text(root, height=20, width=80, padx=15, pady=15)
        text_box.insert(1.0,page_contect)
        text_box.tag_configure("center", justify="center")
        text_box.tag_add("center", 1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")

root.mainloop() 















# learned from MariyaSha