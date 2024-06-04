# Python-Translation-App-
This is a python translation tool , which translates from one language to another language using the google translate API

This Python code snippet demonstrates a simple translation tool using the tkinter library for creating a graphical user interface (GUI). Here’s a brief description of its functionality:

Input Text Area:
The user can enter the text they want to translate into the input text area.
The input text is obtained using input_text.get("1.0", tk.END).strip().

Target Language Selection:
The user can select the target language for translation from a dropdown menu.
The available languages are retrieved from the LANGUAGES dictionary provided by the googletrans library.
The selected target language is stored in the lang_var variable.

Translate Button:
When the user clicks the “Translate” button, the following actions occur:
The detected language of the input text is determined using the detect_language(text) function.
The input text is translated to the selected target language using the translate_text(text, target_lang) function.
The translated text is displayed in the output text area.
If no input text or target language is provided, appropriate warning messages are displayed using messagebox.showwarning().

Output Text Area:
The translated text and the detected language are displayed in the output text area.


GUI Setup:
The GUI window is created using tk.Tk().
Labels, text areas, and buttons are placed in specific rows and columns using grid().
