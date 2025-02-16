import tkinter as tk
from tkinter import messagebox
from tkinter import PhotoImage
import ttkbootstrap as tb
import hashlib
from zxcvbn import zxcvbn

def analyze_password():
    password = entry_password.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return
    
    analysis = zxcvbn(password)
    strength = analysis['score']
    suggestions = analysis['feedback']['suggestions']
    entropy = analysis['guesses_log10']
    
    strength_labels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
    label_strength.config(text=f"Strength: {strength_labels[strength]}")
    label_entropy.config(text=f"Entropy: {entropy:.2f} bits")
    
    hash_value = hashlib.sha256(password.encode()).hexdigest()
    label_hash.config(text=f"SHA-256 Hash: {hash_value[:20]}...")
    
    if suggestions:
        label_suggestions.config(text=f"Suggestions: {', '.join(suggestions)}")
    else:
        label_suggestions.config(text="Suggestions: Your password is strong!")

def clear_fields():
    entry_password.delete(0, tk.END)
    label_strength.config(text="Strength: ")
    label_entropy.config(text="Entropy: ")
    label_hash.config(text="SHA-256 Hash: ")
    label_suggestions.config(text="Suggestions: ")

# GUI Setup
root = tb.Window(themename="cyborg")
root.title("Password Strength Analyzer")
root.geometry("500x350")

# Load background image
bg_image = PhotoImage(file="background.png")
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

frame = tb.Frame(root, padding=20)
frame.pack(expand=True)

label_title = tb.Label(frame, text="Enter Password:", font=("Arial", 12))
label_title.pack(pady=5)

entry_password = tb.Entry(frame, show="*", width=30, font=("Arial", 12))
entry_password.pack(pady=5)

btn_analyze = tb.Button(frame, text="Analyze", command=analyze_password, bootstyle="primary")
btn_analyze.pack(pady=5)

btn_clear = tb.Button(frame, text="Clear", command=clear_fields, bootstyle="danger")
btn_clear.pack(pady=5)

label_strength = tb.Label(frame, text="Strength: ", font=("Arial", 12))
label_strength.pack(pady=5)

label_entropy = tb.Label(frame, text="Entropy: ", font=("Arial", 12))
label_entropy.pack(pady=5)

label_hash = tb.Label(frame, text="SHA-256 Hash: ", font=("Arial", 10))
label_hash.pack(pady=5)

label_suggestions = tb.Label(frame, text="Suggestions: ", font=("Arial", 10))
label_suggestions.pack(pady=5)

root.mainloop()
