import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException


DetectorFactory.seed = 0

translator = Translator()

def translate_text(text, target_lang):
    try:
        translation = translator.translate(text, dest=target_lang)
        return translation.text
    except Exception as e:
        return f"Error: {e}"

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except LangDetectException:
        return "unknown"

def on_translate():
    text = input_text.get("1.0", tk.END).strip()
    target_lang = lang_var.get()

    if not text:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    if not target_lang:
        messagebox.showwarning("Selection Error", "Please select a target language.")
        return

    detected_lang = detect_language(text)
    translation = translate_text(text, target_lang)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, f"Detected Language: {detected_lang}\nTranslated Text: {translation}")

# GUI Setup
root = tk.Tk()
root.title("Translation Tool")

# Input Text
input_label = ttk.Label(root, text="Input Text:")
input_label.grid(row=0, column=0, padx=10, pady=10)
input_text = tk.Text(root, height=10, width=50)
input_text.grid(row=1, column=0, padx=10, pady=10)

# Target Language Selection
lang_label = ttk.Label(root, text="Select Target Language:")
lang_label.grid(row=2, column=0, padx=10, pady=10)
lang_var = tk.StringVar()
lang_combobox = ttk.Combobox(root, textvariable=lang_var)
lang_combobox['values'] = list(LANGUAGES.values())
lang_combobox.grid(row=3, column=0, padx=10, pady=10)

# Translate Button
translate_button = ttk.Button(root, text="Translate", command=on_translate)
translate_button.grid(row=4, column=0, padx=10, pady=10)

# Output Text
output_label = ttk.Label(root, text="Translated Text:")
output_label.grid(row=5, column=0, padx=10, pady=10)
output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=6, column=0, padx=10, pady=10)

root.mainloop()
