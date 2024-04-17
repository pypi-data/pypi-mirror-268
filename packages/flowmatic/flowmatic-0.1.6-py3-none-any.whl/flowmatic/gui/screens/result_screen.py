import asyncio
from dataclasses import dataclass
from enum import Enum
from tkinter import ttk
from typing import Any, AsyncGenerator, Callable, Self, overload

import tkinter as tk
import customtkinter as ctk
import flowmatic as fm
from flowmatic import gui

from flowmatic.gui.screens.screen import Screen


class Status(Enum):
    DEFAULT = "default"
    SUCCESS = "green"
    WARNING = "yellow"
    ERROR = "red"
    SPECIAL = "purple"


class Result:
    result: tuple[str, ...]
    status: Status

    def __init__(self, *args: str, status: Status | None = None) -> None:
        self.result = args
        self.color = status or Status.DEFAULT


class ResultScreen(Screen):
    results: list[Result]
    generator: AsyncGenerator[Result, Any] | None = None
    gen_length: int | None = None
    headers: tuple[str, ...]
    on_select: Callable[[tuple[str, ...]], None]
    show_index: bool = True
    topbar: Screen | None = None
    bottombar: Screen | None = None
    __tree: ttk.Treeview
    __progressbar: ctk.CTkProgressBar
    __progress: tk.IntVar

    @property
    def progress(self) -> float:
        if self.gen_length:
            return self.__progress.get() / self.gen_length
        return 1

    @progress.setter
    def progress(self, value: int) -> None:
        self.__progress.set(value)

    def __init__(self) -> None:
        if not hasattr(self, "results"):
            self.results = []
        self.__progress = tk.IntVar(value=0)

    def __call__(self, master: tk.Tk | tk.Frame) -> Self:
        self.master = master  # pylint: disable=attribute-defined-outside-init
        return self

    def build(self) -> None:
        frame = ctk.CTkFrame(self.master)
        frame.pack(
            **gui.pack_defaults,
            fill="both",
        )

        if self.topbar:
            top_frame = ctk.CTkFrame(frame)
            top_frame.pack()
            self.topbar(top_frame).build()  # pylint: disable=not-callable

        inner_frame = ctk.CTkFrame(frame)
        inner_frame.pack(
            **gui.pack_defaults,
            fill="both",
        )
        progress_frame = ctk.CTkFrame(inner_frame)
        self.build_progress_bar(progress_frame)
        if self.gen_length:
            progress_frame.pack()

        if self.bottombar:
            bottom_frame = ctk.CTkFrame(frame)
            bottom_frame.pack()
            self.bottombar(bottom_frame).build()  # pylint: disable=not-callable

        self.__tree = tree = ttk.Treeview(
            inner_frame,
            columns=("index", *self.headers),
            displaycolumns=(
                used_headers := ("index", *self.headers)
                if self.show_index
                else self.headers
            ),
            show="headings",
        )
        tree.bind(
            "<<TreeviewSelect>>", lambda _: self.do_selection(tree.selection()[0])
        )
        tree.tag_configure(Status.ERROR.value, background="red", foreground="black")
        tree.tag_configure(Status.SUCCESS.value, background="green", foreground="black")
        tree.tag_configure(
            Status.WARNING.value, background="yellow", foreground="black"
        )
        tree.tag_configure(
            Status.SPECIAL.value, background="purple", foreground="black"
        )
        tree.pack(fill="both", expand=True)

        for header in used_headers:
            tree.heading(header, text=header.capitalize())

        if self.results:
            for index, result in enumerate(self.results):
                tree.insert(
                    parent="",
                    index="end",
                    values=(index + 1, *result.result),
                    tags=(result.status.value,),
                )

        fm.update_gui()

        if self.generator:
            asyncio.run(self.generate_results())

    async def generate_results(self) -> None:
        if not self.generator:
            return
        async for index, result in aenumerate(
            self.generator, r_len := len(self.results) + 1
        ):
            self.results.append(result)
            self.__tree.insert(
                parent="",
                index="end",
                values=(index, *result.result),
                tags=(result.color.value,),
            )
            self.progress = index - r_len + 1
            self.__progressbar.set(self.progress)
            fm.update_gui()

    def do_selection(self, index_str: str) -> None:
        index = int(index_str[1:], base=16) - 1  # indexes in table start at 1
        self.on_select(self.results[index].result)

    def build_progress_bar(self, frame: ctk.CTkFrame) -> None:
        ctk.CTkLabel(frame, textvariable=self.__progress).pack(
            side="left", padx=(20, 0)
        )
        ctk.CTkLabel(frame, text=f" / {self.gen_length}").pack(side="left")
        self.__progressbar = ctk.CTkProgressBar(master=frame)
        self.__progressbar.pack(padx=20, pady=10, side="right")
        self.__progressbar.set(0)


async def aenumerate(
    asequence: AsyncGenerator[Result, Any], start=0
) -> AsyncGenerator[tuple[int, Result], Any]:
    """Asynchronously enumerate an async iterator from a given start value"""
    index = start
    async for elem in asequence:
        yield index, elem
        index += 1
