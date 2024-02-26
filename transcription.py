import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

def buildTranscript(argsL):
    toReturn = f"- Mentions : <@&1066482648186372166>\n- BDA : <#{argsL[0]}>\n- TAG / ID : <@{argsL[1]}> | ID IG : `{argsL[2]}`\n- *{argsL[3]}*"
    return toReturn

def submit():
    argsList = [entry.get() for entry in entries]
    result = buildTranscript(argsList)
    output_text.configure(state=ctk.NORMAL)
    output_text.delete(1.0, ctk.END)
    output_text.insert(ctk.END, result)
    output_text.configure(state=ctk.DISABLED)

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(output_text.get(1.0, tk.END))
    app.update()


ctk.set_appearance_mode("System")
 

app = ctk.CTk()
app.geometry("550x420")
app.resizable(False, False)
app.title("Helper.gg") 

app.iconbitmap("ico.ico")
maFont = ctk.CTkFont(family="Tahoma", size=14)

labels = ["ID BDA", "ID DISCORD USER", "ID IG", "Raison"]
entries = []
for i, label_text in enumerate(labels):
    label = ctk.CTkLabel(app, text=label_text, font=maFont)
    label.grid(row=i, column=0, padx=5, pady=5, sticky="e")
    entry = ctk.CTkEntry(app)
    entry.grid(row=i, column=1, padx=5, pady=5, sticky="w")
    entries.append(entry)

submit_button = ctk.CTkButton(app, font=maFont, text="Soumettre", command=submit, fg_color="#DB9E56", hover_color="#966c39")  # changement de la couleur du bouton et de la couleur de survol
submit_button.grid(row=len(labels), columnspan=2, pady=10)

output_text = ctk.CTkTextbox(app, height=15, width=60)
output_text.grid(row=len(labels)+1, columnspan=2, padx=5, pady=5, sticky="nsew")
output_text.configure(state=ctk.DISABLED)

copy_button = ctk.CTkButton(app, font=maFont, text="Copier dans le presse-papiers", command=copy_to_clipboard, fg_color=("#DB9E56"), hover_color="#966c39")  # changement de la couleur du bouton et de la couleur de survol
copy_button.grid(row=len(labels)+2, columnspan=2, pady=5)

app.grid_rowconfigure(len(labels)+1, weight=1)
app.grid_columnconfigure(1, weight=1)

app.mainloop()
