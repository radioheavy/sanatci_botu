import tkinter as tk
from tkinter import filedialog
from art_generator import generate_ascii_art

class ArtGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sanatçı Botu")

        self.label = tk.Label(root, text="Metin girin:")
        self.label.pack(pady=10)

        self.text_entry = tk.Entry(root, width=50)
        self.text_entry.pack(pady=10)

        self.generate_button = tk.Button(root, text="ASCII Sanatı Oluştur", command=self.generate_art)
        self.generate_button.pack(pady=10)

        self.save_button = tk.Button(root, text="Kaydet", command=self.save_art)
        self.save_button.pack(pady=10)

        self.art_text = tk.Text(root, height=20, width=80)
        self.art_text.pack(pady=10)

    def generate_art(self):
        user_input = self.text_entry.get()
        ascii_art = generate_ascii_art(user_input)
        self.art_text.delete(1.0, tk.END)
        self.art_text.insert(tk.END, ascii_art)

    def save_art(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.art_text.get(1.0, tk.END))

if __name__ == "__main__":
    root = tk.Tk()
    app = ArtGeneratorApp(root)
    root.mainloop()
