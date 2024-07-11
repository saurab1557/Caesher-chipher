import tkinter as tk
from tkinter import messagebox

def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def encrypt_text():
    message = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    encrypted_message = caesar_cipher(message, shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, encrypted_message)

def decrypt_text():
    message = input_text.get("1.0", "end-1c")
    shift = int(shift_entry.get())
    decrypted_message = caesar_cipher(message, -shift)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, decrypted_message)


root = tk.Tk()
root.title("Caesar Cipher Encryption/Decryption")


content_frame = tk.Frame(root, padx=20, pady=20)
content_frame.pack()


input_label = tk.Label(content_frame, text="Enter Message:", font=("Arial", 12))
input_label.grid(row=0, column=0, sticky="w")

input_text = tk.Text(content_frame, height=5, width=40, font=("Arial", 12))
input_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


shift_label = tk.Label(content_frame, text="Shift (0-25):", font=("Arial", 12))
shift_label.grid(row=2, column=0, sticky="w")

shift_entry = tk.Entry(content_frame, font=("Arial", 12), width=5)
shift_entry.grid(row=2, column=1, padx=10, pady=10)


encrypt_button = tk.Button(content_frame, text="Encrypt", command=encrypt_text, font=("Arial", 12), bg="#007BFF", fg="white")
encrypt_button.grid(row=3, column=0, pady=10)


decrypt_button = tk.Button(content_frame, text="Decrypt", command=decrypt_text, font=("Arial", 12), bg="#DC3545", fg="white")
decrypt_button.grid(row=3, column=1, pady=10)


output_label = tk.Label(content_frame, text="Result:", font=("Arial", 12))
output_label.grid(row=4, column=0, sticky="w")

output_text = tk.Text(content_frame, height=5, width=40, font=("Arial", 12))
output_text.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
