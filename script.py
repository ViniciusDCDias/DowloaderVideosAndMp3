import customtkinter as ctk
from tkinter import messagebox
import yt_dlp

# Configuração do tema
ctk.set_appearance_mode("Dark")       # "Light", "Dark" ou "System"
ctk.set_default_color_theme("blue")


def baixar_video():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return

    try:
        ydl_opts = {
            "format": "best",
            "outtmpl": "./downloads/%(title)s.%(ext)s"
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Sucesso", "Download concluído!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


def baixar_mp3():
    url = url_entry.get().strip()

    if not url:
        messagebox.showerror("Erro", "Por favor, insira uma URL válida.")
        return

    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": "./downloads/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        messagebox.showinfo("Sucesso", "Download concluído!")

    except Exception as e:
        messagebox.showerror("Erro", str(e))


janela = ctk.CTk()
janela.geometry("500x320")
janela.title("Baixador de Videos - Equipe Lessa")
janela.iconbitmap("./images/icone.ico")

titulo = ctk.CTkLabel(
    janela,
    text="Insira o link do vídeo",
    font=("Arial", 20, "bold")
)
titulo.pack(pady=(25, 15))


url_entry = ctk.CTkEntry(
    janela,
    width=360,
    height=40,
    corner_radius=15,
    placeholder_text="https://..."
)
url_entry.pack()


botao_video = ctk.CTkButton(
    janela,
    text="Baixar Vídeo",
    width=180,
    height=40,
    corner_radius=15,
    command=baixar_video,
    fg_color="red",
    hover_color="#640000"
)
botao_video.pack(pady=(25, 10))


botao_mp3 = ctk.CTkButton(
    janela,
    text="Baixar MP3",
    width=180,
    height=40,
    corner_radius=15,
    fg_color="green",
    hover_color="#006400",
    command=baixar_mp3
)
botao_mp3.pack()


janela.mainloop()