import os
#ignore pygame message annoying
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

#main function
def main():

    try:
        pygame.mixer.init()
    except pygame.error as e:
        print("audio initialization error", e)

    folder = "music"

    if not os.path.isdir(folder):   #checking if the music folder is inside the root dir or not.
        print(f"folder '{folder}' not found!")
        return

    #checking mp3 files

    mp3_files = [file for file in os.listdir(folder) if file.endswith(".mp3")]
    #if not mp3 files.
    if not mp3_files:
        print(" no mp3 files found")



if __name__ == "__main__":
    main()
