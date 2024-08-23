import os
import tkinter as tk
from tkinter import ttk
from libs.UID import run


def get_subfolder_names(path='.'):
    return [entry for entry in os.listdir(path) if os.path.isdir(os.path.join(path, entry))]


def get_dump_inside(path='.'):
    for entry in os.listdir(path):
        full_path = os.path.join(path, entry)
        if not os.path.isdir(full_path) and full_path.endswith('.dump'):
            return full_path
    return None


main_folder = r'.\dumps'


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x300")
        self.active_path = main_folder

        self._init_top_frame()
        self._init_bottom_frame()

    def _init_top_frame(self):
        self.frm_top = tk.Frame(self)
        self.frm_top.pack(fill='both')
        self.lbl_path = tk.Label(self.frm_top, text=f'Path: {self.active_path}', justify="left")
        self.lbl_path.pack()

    def _init_bottom_frame(self):
        self.frm_bot = tk.Frame(self)
        self.frm_bot.pack(fill='both')

        self._init_uid_frame()
        self._init_folder_combobox()
        self._init_back_button()
        self._init_output_frame()
        self._init_generate_button()

    def _init_uid_frame(self):
        frm_uid = tk.Frame(self.frm_bot)
        frm_uid.grid(row=0, column=2, pady=10, padx=10, sticky='we')
        tk.Label(frm_uid, text='UID:').pack()
        self.etr_UID = tk.Entry(frm_uid, justify="center")
        self.etr_UID.pack(fill='both')

    def _init_folder_combobox(self):
        sk_folder = get_subfolder_names(main_folder)
        self.cbx_folder = ttk.Combobox(self.frm_bot, values=sk_folder)
        self.cbx_folder.grid(row=1, column=2, pady=10, padx=10, sticky='we')
        self.cbx_folder.set(sk_folder[0])
        self.cbx_folder.bind("<<ComboboxSelected>>", self.cbx_update)
        tk.Grid.columnconfigure(self.frm_bot, 2, weight=1)

    def _init_back_button(self):
        self.btn_back = tk.Button(self.frm_bot, text='<<Back', state='disabled', command=self.btn_back_action)
        self.btn_back.grid(row=2, column=2, pady=10, padx=10, sticky='we')

    def _init_output_frame(self):
        frm_output = tk.Frame(self.frm_bot)
        frm_output.grid(row=3, column=2, pady=10, padx=10, sticky='we')
        tk.Label(frm_output, text='Output File:').pack()
        self.etr_out = tk.Entry(frm_output, justify="center")
        self.etr_out.pack(fill='both')

    def _init_generate_button(self):
        self.btn_gen = tk.Button(self.frm_bot, text='Generate', state='disabled', command=self.btn_gen_action)
        self.btn_gen.grid(row=4, column=2, pady=10, padx=10, sticky='we')

    def cbx_update(self, _):
        selected_folder = os.path.join(self.active_path, self.cbx_folder.get())
        dump_file = get_dump_inside(selected_folder)

        if dump_file:
            fname = os.path.basename(dump_file)
            self.etr_out.delete(0, 'end')
            self.etr_out.insert(0, f'UID_{self.etr_UID.get()}_{fname}')
            self.btn_gen.config(state='active')
        else:
            self.active_path = selected_folder
            self.lbl_path.config(text=self.active_path)
            sk_folder = get_subfolder_names(self.active_path)
            self.cbx_folder.config(values=sk_folder)
            self.cbx_folder.set(sk_folder[0])
            self.btn_back.config(state='active')

    def btn_back_action(self):
        self.btn_gen.config(state='disabled')
        self.active_path = os.path.dirname(self.active_path)

        self.lbl_path.config(text=self.active_path)

        if not get_dump_inside(self.active_path):
            sk_folder = get_subfolder_names(self.active_path)
            self.cbx_folder.config(values=sk_folder)
            self.cbx_folder.set(sk_folder[0])
            self.btn_back.config(state='active')

        if self.active_path == main_folder:
            self.btn_back.config(state='disabled')

    def btn_gen_action(self):
        dump_path = get_dump_inside(os.path.join(self.active_path, self.cbx_folder.get()))
        run(self.etr_UID.get(), dump_path, self.etr_out.get())


if __name__ == '__main__':
    mainwindow = MainWindow()
    mainwindow.mainloop()
