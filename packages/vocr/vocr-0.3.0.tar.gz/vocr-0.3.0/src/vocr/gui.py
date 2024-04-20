__all__ = ["app_run"]

from tkinter import filedialog

import customtkinter as ctk

from vocr import __gui_name__
from vocr.res import LOGO
from vocr.vocr import VALID_IMG_SUFFIX, VietOCR


class AppMainFrame(ctk.CTkFrame):
    def __init__(self, master) -> None:
        super().__init__(master)

        # Label: Name
        self.label_name = ctk.CTkLabel(
            master=self,
            text=__gui_name__,
            font=("Roboto", 13, "bold"),
        )
        self.label_name.grid(row=0, column=1)

        # Label: File supported
        self.label_fspp = ctk.CTkLabel(
            master=self,
            text=f"File supported: {' '.join(VALID_IMG_SUFFIX)}",
            font=("Roboto", 13),
        )
        self.label_fspp.grid(row=1, padx=10, pady=0)

        # Label: Status
        self.label_status = ctk.CTkLabel(
            master=self,
            text="Status: Pending",
            font=("Roboto", 13),
        )
        self.label_status.grid(row=1, column=2, padx=10, pady=0)

        _button_row = 3
        # Button: Add file
        self.button_afile = ctk.CTkButton(
            master=self,
            text="Add file",
            font=("Roboto", 13, "bold"),
            command=self.button_add_file,
        )
        self.button_afile.grid(row=_button_row, column=0, padx=10, pady=10)

        # Button: Add directory
        self.button_adir = ctk.CTkButton(
            master=self,
            text="Add directory",
            font=("Roboto", 13, "bold"),
            command=self.button_add_directory,
        )
        self.button_adir.grid(row=_button_row, column=1, padx=10, pady=10)

        # Button: Convert
        self.button_cvert = ctk.CTkButton(
            master=self,
            text="Convert",
            font=("Roboto", 13, "bold"),
            command=self.button_convert,
        )
        self.button_cvert.grid(row=_button_row, column=2, padx=10, pady=10)

    def button_add_file(self):
        self.file_path = filedialog.askopenfilename()
        self.label_status.configure(text="Status: File selected")

    def button_add_directory(self):
        self.file_path = filedialog.askdirectory()
        self.label_status.configure(text="Status: Directory selected")

    def button_convert(self):
        fp = self.__getattribute__("file_path")
        vocr = VietOCR(fp)
        vocr.ocr()
        self.label_status.configure(text="Status: Completed")


class VOCR_App(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        # Title bar
        # self.title = "Vietnamese OCR"
        self.wm_title(__gui_name__)
        # self.wm_iconbitmap(LOGO)
        _w = 580
        _h = 180
        _ws = self.winfo_screenwidth()
        _hs = self.winfo_screenheight()
        _x = (_ws / 2) - (_w / 2)
        _y = (_hs / 2) - (_h / 2)
        self.geometry(
            f"{_w}x{_h}+{int(_x)}+{int(_y)}"
        )  # Popup in the middle of the screen

        # self.logo_image = ctk.CTkImage(Image.open(LOGO), size=(26, 26))
        self.iconbitmap(LOGO)

    def add_frame(self, new_frame: ctk.CTkFrame) -> None:
        self.new_frame: ctk.CTkFrame = new_frame(self)
        self.new_frame.pack()


def app_run() -> None:
    app = VOCR_App()
    app.add_frame(AppMainFrame)
    app.mainloop()


if __name__ == "__main__":
    app_run()
