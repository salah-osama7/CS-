import tkinter as tk
from tkinter import messagebox
from gtts import gTTS
import os

window = tk.Tk()
window.title("Text To Speech")
window.geometry("400x200")

tk.Label(window, text="project", font=("Arial", 16)).pack(pady=10)


entry = tk.Entry(window, width=40, font=("Arial", 14))
entry.pack(pady=10)


def play_text():
    text = entry.get()
    if text.strip():
        
        tts = gTTS(text=text, lang='en')
        tts.save("speech.mp3")
        os.system("start speech.mp3")
    else:
        messagebox.showwarning("تحذير", "يرجى إدخال نص للتحويل إلى صوت!")


def clear_text():
    entry.delete(0, tk.END)


def exit_app():
    window.destroy()

btn_play = tk.Button(window, text="Play", font=("Arial", 12), bg="gray", command=play_text)
btn_play.pack(side=tk.LEFT, padx=10, pady=20)

btn_exit = tk.Button(window, text="Exit", font=("Arial", 12), bg="red", fg="white", command=exit_app)
btn_exit.pack(side=tk.LEFT, padx=10)

btn_set = tk.Button(window, text="Set", font=("Arial", 12), bg="blue", fg="white", command=clear_text)
btn_set.pack(side=tk.LEFT, padx=10)

window.mainloop()