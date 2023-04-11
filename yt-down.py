from tkinter import *
import customtkinter
from pytube import YouTube

def main():

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    root = customtkinter.CTk()
    root.title("YouTube Vídeo Downloader")
    root.geometry("340x140")

    website_entry = customtkinter.CTkEntry(master=root, placeholder_text="URL", width=340)
    website_entry.pack(padx=10, pady=10)
    website_entry.focus()
    root.resizable(False, False)

    def link_video():
        state = website_entry.get()
        yt = YouTube(state)
        name_video = customtkinter.CTkLabel(master=root, text=yt.title)
        name_video.pack(padx=10, pady=10, anchor=SW)
        yd = yt.streams.get_highest_resolution()
        yd.download()

    button = customtkinter.CTkButton(master=root, width=36, height=36, text="Baixar Vídeo", command=link_video)
    button.pack(padx=10, pady=10)

    pb = customtkinter.CTkProgressBar(
        root,
        orientation='horizontal',
        mode='determinate',
    )

    root.mainloop()
    
if __name__ == '__main__':
    main()
