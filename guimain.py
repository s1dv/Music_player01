import os
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame
import tkinter as tk
from tkinter import messagebox

FOLDER = "music"

class MusicPlayerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("My Music Player")
        self.root.geometry("400x400")

        try:
            pygame.mixer.init()
        except pygame.error as e:
            messagebox.showerror("Audio error", str(e))

        # --- song list ---
        self.mp3_files = self.load_songs()

        self.listbox = tk.Listbox(root, width=50)
        self.listbox.pack(pady=10)
        for song in self.mp3_files:
            self.listbox.insert(tk.END, song)

        # --- now playing label ---
        self.status_label = tk.Label(root, text="Nothing playing", fg="blue")
        self.status_label.pack(pady=5)

        # --- buttons ---
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Play", command=self.play_selected).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Pause", command=self.pause_music).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Resume", command=self.resume_music).grid(row=0, column=2, padx=5)
        tk.Button(button_frame, text="Stop", command=self.stop_music).grid(row=0, column=3, padx=5)

    def load_songs(self):
        if not os.path.isdir(FOLDER):
            messagebox.showerror("Error", f"Folder '{FOLDER}' not found!")
            return []
        return [f for f in os.listdir(FOLDER) if f.endswith(".mp3")]

    def play_selected(self):
        selection = self.listbox.curselection()  # returns a tuple of selected indices
        if not selection:
            messagebox.showwarning("No selection", "Pick a song first!")
            return
        song_name = self.mp3_files[selection[0]]
        file_path = os.path.join(FOLDER, song_name)

        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        self.status_label.config(text=f"Now playing: {song_name}")

    def pause_music(self):
        pygame.mixer.music.pause()
        self.status_label.config(text=self.status_label.cget("text") + " (paused)")

    def resume_music(self):
        pygame.mixer.music.unpause()

    def stop_music(self):
        pygame.mixer.music.stop()
        self.status_label.config(text="Stopped")


if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayerApp(root)
    root.mainloop()