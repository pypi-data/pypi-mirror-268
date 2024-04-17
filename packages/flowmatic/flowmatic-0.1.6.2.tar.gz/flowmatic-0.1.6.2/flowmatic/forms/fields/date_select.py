import datetime
import tkinter as tk
from typing import Self
import tkcalendar as tkc
import customtkinter as ctk
from flowmatic import gui


class DateSelect:
    master: tk.Frame
    frame: tk.Frame
    label: str
    __value: tk.StringVar

    @property
    def value(self) -> str:
        return self.__value.get()

    @value.setter
    def value(self, value: str) -> None:
        self.__value.set(value)

    def __init__(
        self,
        label: str,
        *,
        value: str | None = None,
    ) -> None:
        self.__value = tk.StringVar(
            value=value or datetime.date.today().strftime("%d.%m.%Y")
        )
        self.label = label

    def __call__(self, master: tk.Frame) -> Self:
        self.master = master
        self.frame = ctk.CTkFrame(
            self.master,
            fg_color=ctk.ThemeManager.theme["CTkFrame"]["fg_color"],
        )
        return self

    def build(self, **kwargs) -> Self:
        self.frame.pack()
        ctk.CTkLabel(master=self.frame, text=self.label).pack(
            side=tk.LEFT, **gui.pack_defaults
        )
        calendar = tkc.Calendar(
            self.frame,
            selectmode="day",
            date_pattern="dd.mm.yyyy",
            showweeknumbers=True,
            textvariable=self.__value,
        )
        calendar.pack(side=tk.RIGHT, **gui.pack_defaults)
        return self

    def pack(self, element: tk.Widget, **kwargs) -> None:
        element.pack(**kwargs)
