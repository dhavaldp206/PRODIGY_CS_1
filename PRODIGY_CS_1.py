import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def encrypt_message():
    message = message_entry.get()
    shift = int(shift_entry.get())
    encrypted_message = caesar_cipher(message, shift, 'encrypt')
    result_label.config(text="Encrypted Message: " + encrypted_message)

def decrypt_message():
    message = message_entry.get()
    shift = int(shift_entry.get())
    decrypted_message = caesar_cipher(message, shift, 'decrypt')
    result_label.config(text="Decrypted Message: " + decrypted_message)

def copy_to_clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text"))
    messagebox.showinfo("Copied", "Text copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x400")
root.configure(bg="#1e1e1e")

# Custom fonts and colors for the hacker theme
hacker_font = ("Courier New", 14, "bold")
text_color = "#00ff00"

# Create and place the widgets with hacker theme styling
title_label = tk.Label(root, text="Caesar Cipher Encryption/Decryption", font=("Courier New", 16, "bold"), bg="#1e1e1e", fg=text_color)
title_label.pack(pady=10)

message_label = tk.Label(root, text="Enter your message:", font=hacker_font, bg="#1e1e1e", fg=text_color)
message_label.pack(pady=5)

message_entry = tk.Entry(root, width=50, font=hacker_font, bg="#333333", fg=text_color, insertbackground=text_color)
message_entry.pack(pady=5)

shift_label = tk.Label(root, text="Enter the shift value:", font=hacker_font, bg="#1e1e1e", fg=text_color)
shift_label.pack(pady=5)

shift_entry = tk.Entry(root, width=5, font=hacker_font, bg="#333333", fg=text_color, insertbackground=text_color)
shift_entry.pack(pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt_message, font=hacker_font, bg="#444444", fg=text_color, activebackground="#555555", activeforeground=text_color)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt_message, font=hacker_font, bg="#444444", fg=text_color, activebackground="#555555", activeforeground=text_color)
decrypt_button.pack(pady=10)

result_label = tk.Label(root, text="", font=hacker_font, bg="#1e1e1e", fg=text_color)
result_label.pack(pady=10)

# Bind right-click event to the result label
result_label.bind("<Button-3>", copy_to_clipboard)

# Start the GUI event loop
root.mainloop()
