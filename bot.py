import customtkinter
from tkinter import *
import string

from tkinter import messagebox


customtkinter.set_appearance_mode("light")
customtkinter.set_default_color_theme("green")
app = customtkinter.CTk()
app.geometry('750x350')
app.title("Шифратор")
app.resizable(width=FALSE, height=FALSE)


def optionmenu_callback(choice):
    if choice in "Светлая":
        customtkinter.set_appearance_mode("light")

    if choice in " Темная":
        customtkinter.set_appearance_mode("dark")


def select_language():
    global selected_language
    selected_language = language.get()

def copy_to_clipboard():
    app.clipboard_clear()
    app.clipboard_append(str(result))
def zxc():
    text = app.selection_get(selection = 'CLIPBOARD')
    message_entry.delete(0, END)
    message_entry.insert(0, text)



def encrypt(message, key):
    global result
    message = message.lower()
    result = ''
    if int(key_entry.get()) > 32:
        messagebox.showerror('Ошибка', 'Ключ должен быть меньше 32!')
    if selected_language == 'английский':
        alphabet = string.ascii_lowercase
    elif selected_language == 'русский':
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    else:
        alphabet = ""

    for letter in message:
        try:
            letter_index = alphabet.index(letter)
            new_index = (letter_index + key) % len(alphabet)
            result += alphabet[new_index]
        except ValueError:
            result += letter

    return result

def decrypt(message, key):
    message = message.lower()
    result = ''

    if selected_language == 'английский':
        alphabet = string.ascii_lowercase
    elif selected_language == 'русский':
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    else:
        alphabet = ""

    for letter in message:
        try:
            letter_index = alphabet.index(letter)
            new_index = (letter_index - key) % len(alphabet)
            result += alphabet[new_index]
        except ValueError:
            result += letter

    return result


frame_1 = customtkinter.CTkFrame(master=app)
frame_1.pack(pady=20, padx=60, fill="both", expand=True)
optionmenu = customtkinter.CTkOptionMenu(master=frame_1, values=["Светлая", "Темная"],
                                         command=optionmenu_callback, fg_color="#6495ED")\
                                        .place(x=455, y=10)
language_label = customtkinter.CTkLabel(master=frame_1, text='Выберите язык')
language_label.grid(row=0, column=0, pady=10)
language = StringVar()
english_switch = customtkinter.CTkRadioButton(master=frame_1, text="Английский", variable=language, value="английский", command=select_language)
english_switch.grid(row=0, column=1, padx=30, pady=5)
russian_switch = customtkinter.CTkRadioButton(master=frame_1, text="Русский", variable=language, value="русский", command=select_language)
russian_switch.grid(row=0, column=2, padx=20, pady=5)

message_label = customtkinter.CTkLabel(master=frame_1, text="Введите текст")
message_label.grid(row=1, column=0, pady=10)
message_entry = customtkinter.CTkEntry(master=frame_1)
message_entry.grid(row=1, column=1, columnspan=2, pady=5)


copy_label = customtkinter.CTkButton(master=frame_1, text='Копировать результат', command=copy_to_clipboard)
copy_label.grid(row=5,column=1, columnspan=1, pady=5)

btn = customtkinter.CTkButton(master=frame_1, text='Вставить', command=zxc)
btn.grid(row=5,column=2, columnspan=3, pady=5)

key_label = customtkinter.CTkLabel(master=frame_1, text="Введите ключ")
key_label.grid(row=2, column=0, pady=15)
key_entry = customtkinter.CTkEntry(master=frame_1)
key_entry.grid(row=2, column=1, columnspan=2, pady=5)


result_label = customtkinter.CTkLabel(master=frame_1, text="Вывод")
result_label.grid(row=3, column=0, pady=10)
result_entry = customtkinter.CTkEntry(master=frame_1)
result_entry.grid(row=3, column=1, columnspan=2, pady=5)

encrypt_button = customtkinter.CTkButton(master=frame_1, text="Зашифровать", command=lambda :result_entry.delete(0, END) or result_entry.insert(0, encrypt(message_entry.get(), int(key_entry.get()))))
encrypt_button.grid(row=4, column=1, padx=20, pady=10)
decrypt_button = customtkinter.CTkButton(master=frame_1, text="Расшифровать", command=lambda :result_entry.delete(0, END) or result_entry.insert(0, decrypt(message_entry.get(), int(key_entry.get()))))
decrypt_button.grid(row=4, column=2, padx=20, pady=10)

master=app.mainloop()