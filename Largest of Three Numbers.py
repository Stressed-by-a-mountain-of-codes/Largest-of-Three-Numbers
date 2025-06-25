import tkinter as tk
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

voice_map = {
    "Male": next((v for v in voices if "David" in v.name or "male" in v.name.lower()), voices[0]),
    "Female": next((v for v in voices if "Zira" in v.name or "female" in v.name.lower()), voices[1] if len(voices) > 1 else voices[0])
}

def speak(text):
    engine.setProperty('voice', voice_map[voice_var.get()].id)
    engine.say(text)
    engine.runAndWait()

def find_largest(event=None):
    try:
        a = float(entry1.get())
        b = float(entry2.get())
        c = float(entry3.get())

        values = {'A': a, 'B': b, 'C': c}
        max_label = max(values, key=values.get)
        max_value = values[max_label]

        result_text = f"Largest: {max_label} = {max_value}"
        result_label.config(text=result_text, fg="darkblue")

        speak(f"The largest is {max_label}, which is {max_value}")
        root.after(3000, reset)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.delete(0, tk.END)
    result_label.config(text="")

root = tk.Tk()
root.title("Largest of Three Numbers + Voice")
root.geometry("400x320")
root.resizable(False, False)

tk.Label(root, text="Enter values for A, B, and C", font=("Arial", 12)).pack(pady=10)

entry1 = tk.Entry(root, font=("Arial", 12), justify="center")
entry1.pack(pady=5)
entry1.focus()

entry2 = tk.Entry(root, font=("Arial", 12), justify="center")
entry2.pack(pady=5)

entry3 = tk.Entry(root, font=("Arial", 12), justify="center")
entry3.pack(pady=5)
entry3.bind("<Return>", find_largest)

tk.Button(root, text="Find Largest", font=("Arial", 12), command=find_largest).pack(pady=10)

voice_var = tk.StringVar(value="Female")
voice_frame = tk.Frame(root)
voice_frame.pack(pady=5)
tk.Label(voice_frame, text="Voice:").pack(side="left", padx=5)
tk.OptionMenu(voice_frame, voice_var, "Male", "Female").pack(side="left")

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()
