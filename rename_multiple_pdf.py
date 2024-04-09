import os
from tkinter import Tk, Label, Entry, Button, messagebox
from tkinter import filedialog

def select_folder():
    global folder_selected
    folder_selected = filedialog.askdirectory()
    folder_path_label.config(text=folder_selected)

def rename_files():
    prefix = name_prefix.get()
    if not prefix:
        messagebox.showerror("Error", "Vui long nhap MA PROFILE")
        return
    if not folder_selected:
        messagebox.showerror("Error", "Vui long chon thu muc")
        return

    files_renamed = 0
    for index, file in enumerate(os.listdir(folder_selected), start=1):
        if file.endswith('.pdf'):
            src = f"{folder_selected}/{file}"
            dst = f"{folder_selected}/{prefix}-{index:03d}.pdf"
            os.rename(src, dst)
            files_renamed += 1
    messagebox.showinfo("Hoan tat", f"Doi ten thanh cong. {files_renamed} files da duoc doi ten.")

root = Tk()
root.geometry("800x600")
root.title('PDF Renamer')

Label(root, text="MA PROFILE:").pack()
name_prefix = Entry(root)
name_prefix.pack()

folder_select_btn = Button(root, text="Chon thu muc", command=select_folder)
folder_select_btn.pack()

folder_path_label = Label(root, text="Chua chon thu muc")
folder_path_label.pack()

run_btn = Button(root, text="Run", command=rename_files)
run_btn.pack()

folder_selected = ""

root.mainloop()
